#!encoding:utf-8
from __future__ import unicode_literals

from applications.custom_user.models import *


class Resume(models.Model):
    """个人简历基础信息"""
    custom_user = models.OneToOneField(CustomUser, verbose_name="用户信息", related_name="Resumes", unique=True)
    avatar = models.CharField('简历头像', max_length=255, null=True, blank=True, default='')
    name = models.CharField("姓名", max_length=255, null=True, blank=True, default="")
    sex = models.CharField("性别", max_length=2, blank=True, null=True, default="")
    birthday = models.CharField("生日", max_length=30, blank=True, null=True, default="")
    age = models.PositiveIntegerField("年龄", null=True, blank=True)
    years_of_service = models.CharField("工作年限", max_length=255, null=True, blank=True, default="")
    education = models.CharField("最高学历", max_length=255, null=True, blank=True, default="")
    status = models.CharField("在职状态", max_length=255, null=True, blank=True, default="")
    company = models.CharField("现任公司", max_length=255, null=True, blank=True, default="")
    position = models.CharField("现任职务", max_length=255, null=True, blank=True, default="")
    advantage = models.TextField("我的优势", null=True, blank=True, default="")
    career_objective = models.ForeignKey("CareerObjective", verbose_name="首要意向", related_name="Resumes", null=True,
                                         blank=True)

    def __str__(self):
        return self.custom_user.nickname

    class Meta:
        db_table = 'Resume'
        verbose_name = "个人简历基础信息"
        verbose_name_plural = "个人简历基础信息"
        index_together = ["custom_user"]


class CareerObjective(models.Model):
    """求职意向"""
    custom_user = models.ForeignKey(CustomUser, verbose_name="用户信息", related_name="careerobjective_custom_user")
    position = models.CharField("期望职位", max_length=255, null=True, blank=True, default="")
    expect_salary = models.CharField("期望薪资", max_length=255, null=True, blank=True, default="")
    city = models.CharField("期望城市", max_length=255, null=True, blank=True, default="")
    industry = models.CharField("期望行业", max_length=255, null=True, blank=True, default="")

    def __str__(self):
        return self.position

    class Meta:
        db_table = 'CareerObjective'
        verbose_name = "求职意向"
        verbose_name_plural = "求职意向"
        ordering = ['-id']
        index_together = ["custom_user"]


class WorkExperience(models.Model):
    """工作经历"""
    custom_user = models.ForeignKey(CustomUser, verbose_name="用户信息", related_name="workexperience_custom_user")
    company = models.CharField("公司名称", max_length=255, null=True, blank=True, default="")
    position = models.CharField("职位名称", max_length=255, null=True, blank=True, default="")
    start_time = models.CharField("在职起始时间", max_length=255, null=True, blank=True, default="")
    end_time = models.CharField("在职终止时间", max_length=255, null=True, blank=True, default="")
    content = models.TextField("工作内容", null=True, blank=True, default="")

    def __str__(self):
        return self.company

    class Meta:
        db_table = 'WorkExperience'
        verbose_name = "工作经历"
        verbose_name_plural = "工作经历"
        ordering = ['-id']
        index_together = ["custom_user"]


class ProjectExperience(models.Model):
    """项目经验"""
    custom_user = models.ForeignKey(CustomUser, verbose_name="用户信息", related_name="projectexperience_custom_user")
    name = models.CharField("项目名称", max_length=255, null=True, blank=True, default="")
    role = models.CharField("角色", max_length=255, null=True, blank=True, default="")
    url = models.CharField("项目链接", max_length=255, null=True, blank=True, default="")
    start_time = models.CharField("项目起始时间", max_length=255, null=True, blank=True, default="")
    end_time = models.CharField("项目终止时间", max_length=255, null=True, blank=True, default="")
    description = models.TextField("项目描述", null=True, blank=True, default="")
    performance = models.TextField("项目业绩", null=True, blank=True, default="")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ProjectExperience'
        verbose_name = "项目经验"
        verbose_name_plural = "项目经验"
        ordering = ['-id']
        index_together = ["custom_user"]


class EducationExperience(models.Model):
    """教育经历"""
    custom_user = models.ForeignKey(CustomUser, verbose_name="用户信息", related_name="educationexperience_custom_user")
    school = models.CharField("学校名称", max_length=255, null=True, blank=True, default="")
    discipline = models.CharField("所学专业", max_length=255, null=True, blank=True, default="")
    education = models.CharField("学历", max_length=255, null=True, blank=True, default="")
    start_time = models.CharField("起始时间", max_length=255, null=True, blank=True, default="")
    end_time = models.CharField("终止时间", max_length=255, null=True, blank=True, default="")
    experience = models.TextField("在校经历", null=True, blank=True, default="")

    def __str__(self):
        return self.school

    class Meta:
        db_table = 'EducationExperience'
        verbose_name = "教育经历"
        verbose_name_plural = "教育经历"
        ordering = ['-id']
        index_together = ["custom_user"]
