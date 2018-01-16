#!encoding:utf-8
import json

from django.http import HttpResponse
from django.views.generic import View

from applications.custom_user.models import *
from applications.record.models import WatchRecord
from applications.tracks_learning.models import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int


@class_view_decorator(user_login_required)
class HandleWatchRecord(View):
    """增加视频的观看记录"""

    def post(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success"}
        try:
            param_dict = json.loads(request.body)
            custom_user_id = str_to_int(param_dict.get('custom_user_id', 0))  # 必填，用户ID
            course_id = str_to_int(param_dict.get('course_id', 0))  # 必填，课程ID
            video_id = str_to_int(param_dict.get('video_id', 0))  # 必填，视频ID
            real_play_video_time = str_to_int(param_dict.get('real_play_video_time', 0))  # 当前观看时间（不包含视频缓冲时间）,秒
            duration = str_to_int(param_dict.get('duration', 0))  # 当前视频的时长，秒
            status = str_to_int(param_dict.get('status', 0))  # 1：已看完；0：未看完

            if not custom_user_id or not course_id or not video_id or real_play_video_time or not duration:
                result_dict["err"] = 1
                result_dict["msg"] = "参数不全"
                return

            # 查询是否有观看记录
            watchrecords = WatchRecord.objects.filter(user__id=custom_user_id, video__id=video_id, course__id=course_id)
            if watchrecords.exists():
                update_dict = {
                    "video_process": real_play_video_time,
                    "duration": duration,
                    "status": status,
                }
                rows = watchrecords.update(**update_dict)
                if not rows:
                    result_dict["err"] = 1
                    result_dict["msg"] = "更新用户观看记录失败"
                    return
            else:
                # 用户
                user = None
                users = CustomUser.objects.filter(id=custom_user_id)
                if users.exists():
                    user = users.first()
                if not user:
                    result_dict["err"] = 1
                    result_dict["msg"] = "观看用户不存在"
                    return

                # 课程
                course = None
                courses = Course.objects.filter(id=course_id)
                if courses.exists():
                    course = courses.first()
                if not course:
                    result_dict["err"] = 1
                    result_dict["msg"] = "课程不存在"
                    return

                # 视频
                video = None
                videos = Video.objects.filter(id=video_id)
                if videos.exists():
                    video = videos.first()
                if video:
                    result_dict["err"] = 1
                    result_dict["msg"] = "视频不存在"
                    return

                create_dict = {
                    "user": user,
                    "video": video,
                    "course": course,
                    "video_process": real_play_video_time,
                    "duration": duration,
                }
                add_obj = WatchRecord.objects.create(**create_dict)
                if not add_obj:
                    result_dict["err"] = 1
                    result_dict["msg"] = "添加视频观看记录失败"
                    return
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
