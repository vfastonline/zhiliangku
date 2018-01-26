#!encoding:utf-8
import json

from django.http import HttpResponse
from django.views.generic import View

from applications.personal_center.models import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import get_kwargs, str_to_int

"""我的简历"""

resume_model_dict = {
    "resume": Resume,
    "careerobjective": CareerObjective,
    "workexperience": WorkExperience,
    "projectexperience": ProjectExperience,
    "educationexperience": EducationExperience,
}


def get_resume_detail_info(custom_user_id):
    """根据用户ID，获取简历全量数据
    :param custom_user_id:
    :return:
    """
    result_dict = {
        "err": 0,
        "msg": "success",
        "data": dict(),
    }
    try:
        resumes = Resume.objects.filter(custom_user_id=custom_user_id)
        careerobjectives = list(CareerObjective.objects.filter(custom_user_id=custom_user_id).values())
        workexperiences = list(WorkExperience.objects.filter(custom_user_id=custom_user_id).values())
        projectexperiences = list(ProjectExperience.objects.filter(custom_user_id=custom_user_id).values())
        educationexperiences = list(EducationExperience.objects.filter(custom_user_id=custom_user_id).values())
        data_dict = dict()
        resume_dict = dict()

        # 基础信息
        if resumes.exists():
            resume = resumes.first()
            resume_dict["id"] = resume.id
            resume_dict["avatar"] = resume.avatar.url if resume.avatar else ""
            resume_dict["name"] = resume.name
            resume_dict["sex"] = resume.sex
            resume_dict["birthday"] = resume.birthday
            resume_dict["years_of_service"] = resume.years_of_service
            resume_dict["education"] = resume.education
            resume_dict["status"] = resume.status
            resume_dict["company"] = resume.company
            resume_dict["position"] = resume.position
            resume_dict["advantage"] = resume.advantage
            resume_dict["expect_salary"] = resume.career_objective.expect_salary if resume.career_objective else ""

        data_dict["resume"] = resume_dict
        data_dict["careerobjectives"] = careerobjectives
        data_dict["workexperiences"] = workexperiences
        data_dict["projectexperiences"] = projectexperiences
        data_dict["educationexperiences"] = educationexperiences
        result_dict["data"] = data_dict
    except:
        traceback.print_exc()
        logging.getLogger().error(traceback.format_exc())
    finally:
        return result_dict


@class_view_decorator(user_login_required)
class ResumeDetailInfo(View):
    """全量--简历信息"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": dict(),
        }
        try:
            custom_user_id = str_to_int(request.GET.get('custom_user_id', 0))  # 用户ID
            result_dict = get_resume_detail_info(custom_user_id)
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class ResumeDelete(View):
    """删除简历信息"""

    def post(self, request, *args, **kwargs):
        result_dict = {"err": 1, "msg": ""}
        try:
            param_dict = json.loads(request.body)
            resume_type = param_dict.get("resume_type", "")
            custom_user_id = str_to_int(param_dict.get("custom_user_id", 0))
            pk_id = str_to_int(param_dict.get("pk_id", 0))

            if resume_type and pk_id:
                resume_type_model = resume_model_dict.get(resume_type)
                if resume_type_model:
                    deleted, _rows_count = resume_type_model.objects.filter(id=pk_id).delete()
                    if deleted and _rows_count:
                        result_dict = get_resume_detail_info(custom_user_id)
                    else:
                        result_dict["msg"] = "未找到要删除的简历信息"
                else:
                    result_dict["msg"] = "未找到要删除的简历类型"
            else:
                result_dict["msg"] = "删除简历信息不完善，删除失败!"
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class ResumeUpdate(View):
    """修改简历信息"""

    def post(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "修改成功"}
        try:
            param_dict = json.loads(request.body)
            custom_user_id = str_to_int(param_dict.get("custom_user_id", 0))
            resume_type = param_dict.get("resume_type", "")
            pk_id = str_to_int(param_dict.get("pk_id", 0))
            resume_info_dict = param_dict.get("resume_info_dict", {})

            career_objective_id = resume_info_dict.get("career_objective_id", 0)
            if resume_type and pk_id and resume_info_dict:
                if resume_type == "resume":
                    if career_objective_id:
                        career_objective_obj = CareerObjective.objects.filter(id=career_objective_id)
                        if career_objective_obj.exists():
                            resume_info_dict["career_objective"] = career_objective_obj.first()
                resume_type_model = resume_model_dict.get(resume_type)
                if resume_type_model:
                    kwargs = get_kwargs(resume_info_dict)
                    resume_type_model.objects.filter(id=pk_id).update(**kwargs)
                else:
                    result_dict["msg"] = "未找到简历类型"
                result_dict = get_resume_detail_info(custom_user_id)
            else:
                result_dict["err"] = 1
                result_dict["msg"] = "简历修改数据不完善，修改失败!"
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class ResumeAdd(View):
    """增加不同类型简历信息"""

    def post(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "", "id": ""}
        try:
            param_dict = json.loads(request.body)
            resume_type = param_dict.get("resume_type", "")
            resume_info_dict = param_dict.get("resume_info_dict", {})
            custom_user_id = str_to_int(param_dict.get("custom_user_id", 0))

            career_objective_id = resume_info_dict.get("career_objective_id", 0)
            user_obj = None
            if custom_user_id:
                user_obj = CustomUser.objects.filter(id=custom_user_id)
            if user_obj.exists() and resume_info_dict:
                resume_info_dict["custom_user"] = user_obj.first()
                resume_type_model = resume_model_dict.get(resume_type)
                if resume_type_model:
                    if resume_type == "resume":
                        resume_obj = Resume.objects.filter(custom_user_id=user_obj)
                        if resume_obj.exists():
                            if career_objective_id:
                                career_objective_obj = CareerObjective.objects.filter(id=career_objective_id)
                                if career_objective_obj.exists():
                                    resume_info_dict["career_objective"] = career_objective_obj.first()
                            kwargs = get_kwargs(resume_info_dict)
                            resume_obj.update(**kwargs)
                        else:
                            kwargs = get_kwargs(resume_info_dict)
                            resume_type_model.objects.create(**kwargs)
                    else:
                        kwargs = get_kwargs(resume_info_dict)
                        resume_type_model.objects.create(**kwargs)
                else:
                    result_dict["msg"] = "未找到简历类型"
                result_dict = get_resume_detail_info(custom_user_id)
            else:
                result_dict["err"] = 1
                result_dict["msg"] = "未找到用户信息或简历信息为空，新增失败!"
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
