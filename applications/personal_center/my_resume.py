#!encoding:utf-8
import json

from django.http import HttpResponse
from django.views.generic import View

from applications.personal_center.models import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import get_kwargs

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
        resumes = list(Resume.objects.filter(custom_user_id=custom_user_id).values())
        careerobjectives = list(CareerObjective.objects.filter(custom_user_id=custom_user_id).values())
        workexperiences = list(WorkExperience.objects.filter(custom_user_id=custom_user_id).values())
        projectexperiences = list(ProjectExperience.objects.filter(custom_user_id=custom_user_id).values())
        educationexperiences = list(EducationExperience.objects.filter(custom_user_id=custom_user_id).values())
        data_dict = dict()

        # 基础信息
        if resumes:
            resume_dict = resumes[0]
            data_dict.update(resume_dict)
            career_objective_id = resume_dict.get("career_objective_id", 0)
            if career_objective_id:
                career_objective_list = list(
                    CareerObjective.objects.filter(id=career_objective_id).values("expect_salary_low",
                                                                                  "expect_salary_high"))
                if career_objective_list:
                    data_dict["expect_salary_low"] = career_objective_list[0].get("expect_salary_low")
                    data_dict["expect_salary_high"] = career_objective_list[0].get("expect_salary_high")

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
    """简历--基础信息"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": dict(),
        }
        try:
            custom_user_id = request.GET.get('custom_user_id', 0)  # 用户ID
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
            custom_user_id = param_dict.get("custom_user_id", 0)
            pk_id = param_dict.get("pk_id", "")
            if resume_type and pk_id:
                resume_type_model = resume_model_dict.get(resume_type)
                deleted, _rows_count = resume_type_model.objects.filter(id=pk_id).delete()
                if deleted and _rows_count:
                    result_dict = get_resume_detail_info(custom_user_id)
                else:
                    result_dict["msg"] = "未找到要删除的简历信息"
            else:
                result_dict["msg"] = "删除简历信息不完善，删除失败!"
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


# @class_view_decorator(user_login_required)
class ResumeUpdate(View):
    """修改简历信息"""

    def post(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "修改成功"}
        try:
            param_dict = json.loads(request.body)
            custom_user_id = param_dict.get("custom_user_id", 0)
            resume_type = param_dict.get("resume_type", "")
            pk_id = param_dict.get("pk_id", "")
            resume_info_dict = param_dict.get("resume_info_dict", {})
            career_objective_id = resume_info_dict.get("career_objective_id")
            if resume_type and pk_id and resume_info_dict:
                if resume_type == "resume":
                    career_objective_obj = CareerObjective.objects.filter(id=career_objective_id)
                    if career_objective_obj.exists():
                        resume_info_dict["career_objective"] = career_objective_obj.first()
                resume_type_model = resume_model_dict.get(resume_type)
                kwargs = get_kwargs(resume_info_dict)
                resume_type_model.objects.filter(id=pk_id).update(**kwargs)
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
            custom_user_id = resume_info_dict.get("custom_user_id")
            career_objective_id = resume_info_dict.get("career_objective_id")
            user_obj = CustomUser.objects.filter(id=custom_user_id)
            if user_obj.exists() and resume_info_dict:
                resume_info_dict["custom_user"] = user_obj.first()
                resume_type_model = resume_model_dict.get(resume_type)
                if resume_type == "resume":
                    resume_obj = Resume.objects.filter(custom_user_id=user_obj)
                    if resume_obj.exists():
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
                result_dict = get_resume_detail_info(custom_user_id)
            else:
                result_dict["err"] = 1
                result_dict["msg"] = "未找到用户信息，新增失败!"
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
