#!encoding:utf-8
from __future__ import unicode_literals

import datetime

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from lib.base_redis import redis_db
from lib.storage import ImageStorage
from lib.util import *
from lib.util import NULL_BLANK_TRUE


def upload_to(instance, fielname):
    return os.path.join("custom_user_avatar", str(instance.id), fielname)


class CustomUserClass(models.Model):
    """学生班级"""

    name = models.CharField('班级名称', max_length=255)
    technology = models.ForeignKey('tracks_learning.Technology', verbose_name="技术分类", on_delete=models.CASCADE,
                                   **NULL_BLANK_TRUE)
    invite_code = models.CharField('邀请码', max_length=5, **NULL_BLANK_TRUE)
    invalid_time = models.DateTimeField('失效时间', help_text="编辑保存触发产生新邀请码", **NULL_BLANK_TRUE)

    def __str__(self):
        return self.name

    @classmethod
    def get_invite_code(cls):
        """获取班级邀请码，不能重复"""
        invite_code = get_random_code(5)
        customuserclasss = CustomUserClass.objects.filter(invite_code=invite_code)
        if customuserclasss.exists():
            return cls.get_invite_code()
        return invite_code

    @staticmethod
    def check_invite_code(invite_code):
        """校验班级邀请码
        :param invite_code:班级邀请码
        :return:班级对象
        """

        return redis_db.get(invite_code)

    class Meta:
        db_table = 'CustomUserClass'
        verbose_name = "学生班级"
        verbose_name_plural = "学生班级"


@receiver(post_save, sender=CustomUserClass)
def add_customuser_class_event(sender, instance, **kwargs):
    """添加新班级时，生成一个新的注册码
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    try:
        invalid_time = datetime.datetime.now() + datetime.timedelta(hours=1)
        invite_code = CustomUserClass.get_invite_code()
        update_param = {
            "invalid_time": invalid_time,
            "invite_code": CustomUserClass.get_invite_code(),
        }

        CustomUserClass.objects.filter(id=instance.id).update(**update_param)

        # 将班级信息保存在redis中，设置过期时间
        redis_db.setex(invite_code, instance, (invalid_time - datetime.datetime.now()).seconds)
    except:
        traceback.print_exc()
        logging.getLogger().error(traceback.format_exc())


class CustomUser(models.Model):
    """用户基础信息 """
    ROLE = (
        (0, '学生'),
        (1, '老师'),
        (2, 'HR'),
        (3, '其他'),
    )
    GENDER_CHOICES = (
        ('M', u'男'),
        ('F', u'女'),
    )

    DEFAULT_AVATAR = "custom_user_avatar/defaultUserIcon.png"

    nickname = models.CharField('真实姓名', max_length=255, **NULL_BLANK_TRUE)
    sex = models.CharField("性别", max_length=2, choices=GENDER_CHOICES, blank=True)
    birthday = models.CharField("出生年月", max_length=30, default="", **NULL_BLANK_TRUE)
    role = models.IntegerField('角色', choices=ROLE, null=True, default=3)
    avatar = models.ImageField('头像', upload_to=upload_to, storage=ImageStorage(), max_length=256,
                               default=DEFAULT_AVATAR, **NULL_BLANK_TRUE)
    institutions = models.CharField('所在院校', max_length=255, **NULL_BLANK_TRUE)
    class_s = models.ManyToManyField(CustomUserClass, verbose_name='所在班级')
    is_computer = models.BooleanField("计算机专业", default=False)
    is_graduate = models.BooleanField("在校情况", default=False)  # False:在校，True：毕业
    education = models.CharField("学历", max_length=255, default="", **NULL_BLANK_TRUE)
    position = models.CharField('职位', max_length=255, **NULL_BLANK_TRUE)
    signature = models.TextField('个性签名', max_length=255, default="", **NULL_BLANK_TRUE)
    contact_number = models.CharField('联系电话', max_length=255, default="", **NULL_BLANK_TRUE)
    integral = models.PositiveIntegerField("积分", default=0)  # 隐藏
    receiver = models.CharField('收货人', max_length=255, default="", **NULL_BLANK_TRUE)  # 隐藏
    address = models.CharField('收货地址', max_length=255, default="", **NULL_BLANK_TRUE)  # 隐藏
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)

    def __str__(self):
        return ",".join([self.nickname, str(self.id), str(self.get_role_display())])

    class Meta:
        db_table = 'CustomUser'
        verbose_name = "基础信息"
        verbose_name_plural = "基础信息"
        ordering = ["-create_time"]


@receiver(post_save, sender=CustomUser)  # 信号的名字，发送者
def add_customuser_event(sender, instance, **kwargs):  # 回调函数，收到信号后的操作
    """注册新的用户时，默认增加一个简历信息
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    from applications.personal_center.models import Resume
    from applications.notification.models import UserNotificationsCount
    try:
        Resume.objects.get_or_create(custom_user=instance)  # 默认增加一个简历
        UserNotificationsCount.objects.get_or_create(custom_user=instance)  # 增加未读消息信息
    except:
        traceback.print_exc()
        logging.getLogger().error(traceback.format_exc())


class CustomUserAuths(models.Model):
    """用户授权信息"""
    IDENTITYTYPE = (
        ("phone", "phone"),
        ("email", "email"),
        ("weixin", "weixin"),
        ("qq", "qq"),
    )
    custom_user_id = models.ForeignKey(CustomUser, verbose_name="用户", on_delete=models.CASCADE)
    identity_type = models.CharField('登录类型', choices=IDENTITYTYPE, max_length=10, help_text="手机号、邮箱、用户名或第三方应用名称微信、微博等。")
    identifier = models.CharField('唯一标识', max_length=255, help_text="手机号、邮箱、用户名或第三方应用的唯一标识。")
    credential = models.CharField('密码凭证', max_length=255, help_text="站内的保存密码，站外的不保存或保存token。")
    status = models.BooleanField("是否激活", default=True)
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)

    def __str__(self):
        return self.identity_type

    class Meta:
        db_table = 'CustomUserAuths'
        verbose_name = "授权信息"
        verbose_name_plural = "授权信息"
        ordering = ["-create_time", "custom_user_id"]


class CustomUserProject(models.Model):
    """用户参与项目 """

    custom_user = models.ForeignKey(CustomUser, verbose_name="用户", limit_choices_to={'role': 0},
                                    help_text='只允许选择角色是”学生“的用户。', on_delete=models.CASCADE)
    project = models.ForeignKey("tracks_learning.Project", verbose_name="参与项目", on_delete=models.CASCADE, **NULL_BLANK_TRUE)
    create_time = models.DateTimeField(verbose_name='参与时间', default=timezone.now)

    def __str__(self):
        return self.custom_user.nickname

    class Meta:
        db_table = 'CustomUserProject'
        verbose_name = "参与项目"
        verbose_name_plural = "参与项目"
        ordering = ["-create_time"]


class CustomUserCourse(models.Model):
    """用户收藏课程 """

    custom_user = models.ForeignKey(CustomUser, verbose_name="用户", limit_choices_to={'role': 0},
                                    help_text='只允许选择角色是”学生“的用户。', on_delete=models.CASCADE)
    course = models.ForeignKey("tracks_learning.Course", verbose_name="课程", on_delete=models.CASCADE, **NULL_BLANK_TRUE)
    create_time = models.DateTimeField(verbose_name='收藏时间', default=timezone.now)

    def __str__(self):
        return self.custom_user.nickname

    class Meta:
        db_table = 'CustomUserCourse'
        verbose_name = "收藏课程"
        verbose_name_plural = "收藏课程"
        ordering = ["-create_time"]


class VerifyCode(models.Model):
    """短信验证码"""
    phone = models.CharField("手机号", max_length=11)
    code = models.CharField("验证码", max_length=4)
    create_time = models.DateTimeField(verbose_name='生成时间', default=timezone.now)
    expire_time = models.DateTimeField("失效时间", max_length=4)
    is_use = models.BooleanField("已使用", default=False)

    def __str__(self):
        return self.phone + ":" + self.code

    def check_is_valid(self):
        """校验验证码是否有效
        :return:
        """
        try:
            # 已经使用过
            if self.is_use:
                return 1

        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())

    class Meta:
        db_table = 'VerifyCode'
        verbose_name = "验证码"
        verbose_name_plural = "验证码"
