#!encoding:utf-8

from django.views.generic import View

from applications.custom_user.models import *
from applications.personal_center.models import Resume
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import *


@class_view_decorator(user_login_required)
class CustomUserAvatar(View):
    """设置用户头像或简历头像"""

    def post(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "avatar": "",
        }
        avatar_type_list = ["custom_user_avatar", "resume_avatar"]
        try:
            avatar = request.FILES.get('file', None)
            custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
            avatar_type = request.GET.get('avatar_type', None)  # 图片类型

            if avatar_type not in avatar_type_list:
                result_dict["err"] = 1
                result_dict["msg"] = "头像类型错误"
                return

            if not avatar:
                result_dict["err"] = 1
                result_dict["msg"] = "没有上传用户头像"
                return

            user = CustomUser.objects.filter(id=custom_user_id)
            if not user.exists():
                result_dict["err"] = 1
                result_dict["msg"] = "用户不存在"
                return

            # # 组装头像存放位置
            # destination = os.path.join(settings.MEDIA_ROOT, 'custom_user_avatar', str(custom_user_id))
            # if avatar_type == "resume_avatar":
            #     destination = os.path.join(settings.MEDIA_ROOT, 'resume_avatar', str(custom_user_id))
            #
            # # 判断路径是否存在，并创建
            # if not os.path.isdir(destination):
            #     os.system('mkdir -p %s ' % destination)
            #
            # # 组装文件名
            # fn = time.strftime('%Y%m%d%H%M%S')
            # fn = fn + '_%d' % random.randint(0, 1000)
            # filename = os.path.join(fn + '.jpg')
            #
            # headfile = open(os.path.join(destination, filename), 'wb')
            # for chunk in avatar.chunks():
            #     headfile.write(chunk)
            # headfile.close()
            #
            # headimg_url = os.path.join("custom_user_avatar", 'custom_user_avatar', str(custom_user_id), filename)
            humbnail = get_thumbnail(avatar)
            if avatar_type == "resume_avatar":
                resume_obj = Resume.objects.filter(custom_user=user).first()
                # headimg_url = os.path.join(settings.MEDIA_ROOT, 'resume_avatar', custom_user_id, filename)
                if resume_obj:
                    resume_obj.avatar = humbnail
                    resume_obj.save()
                else:
                    Resume.objects.create(custom_user=user, avatar=humbnail)
                try:
                    avatar_str = Resume.objects.get(custom_user=user).avatar.url
                except:
                    avatar_str = ""
                    traceback.print_exc()
                result_dict["avatar"] = avatar_str
            if avatar_type == "custom_user_avatar":
                user_obj = user.first()
                user_obj.avatar = humbnail
                user_obj.save()

                try:
                    avatar_str = user_obj.avatar.url
                except:
                    avatar_str = ""
                    traceback.print_exc()
                result_dict["avatar"] = avatar_str
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
