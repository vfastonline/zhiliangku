#!encoding:utf-8
from __future__ import unicode_literals

from applications.custom_user.models import *
from lib.util import NULL_BLANK_TRUE


class Resume(models.Model):
	"""个人简历基础信息"""
	custom_user = models.OneToOneField(CustomUser, verbose_name="用户信息", related_name="Resumes", unique=True)
	avatar = models.ImageField('简历头像', upload_to='resume', default='custom_user_avatar/defaultUserIcon.png', blank=True)
	name = models.CharField("姓名", max_length=255, default="", **NULL_BLANK_TRUE)
	sex = models.CharField("性别", max_length=2, default="", **NULL_BLANK_TRUE)
	birthday = models.CharField("生日", max_length=30, default="", **NULL_BLANK_TRUE)
	years_of_service = models.CharField("工作年限", max_length=255, default="", **NULL_BLANK_TRUE)
	education = models.CharField("最高学历", max_length=255, default="", **NULL_BLANK_TRUE)
	status = models.CharField("在职状态", max_length=255, default="", **NULL_BLANK_TRUE)
	company = models.CharField("现任公司", max_length=255, default="", **NULL_BLANK_TRUE)
	position = models.CharField("现任职务", max_length=255, default="", **NULL_BLANK_TRUE)
	advantage = models.TextField("我的优势", default="", **NULL_BLANK_TRUE)
	career_objective = models.ForeignKey("CareerObjective", verbose_name="首要意向", related_name="Resumes",
										 **NULL_BLANK_TRUE)

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
	position = models.CharField("职位", max_length=255, default="", **NULL_BLANK_TRUE)
	way = models.CharField("工作方式", max_length=255, default="", **NULL_BLANK_TRUE)
	city = models.CharField("城市", max_length=255, default="", **NULL_BLANK_TRUE)
	expect_salary = models.CharField("薪资", max_length=255, default="", **NULL_BLANK_TRUE)
	industry = models.CharField("行业", max_length=255, default="", **NULL_BLANK_TRUE)

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
	company = models.CharField("公司名称", max_length=255, default="", **NULL_BLANK_TRUE)
	position = models.CharField("职位名称", max_length=255, default="", **NULL_BLANK_TRUE)
	start_time = models.CharField("在职起始时间", max_length=255, default="", **NULL_BLANK_TRUE)
	end_time = models.CharField("在职终止时间", max_length=255, default="", **NULL_BLANK_TRUE)
	content = models.TextField("工作内容", default="", **NULL_BLANK_TRUE)

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
	name = models.CharField("项目名称", max_length=255, default="", **NULL_BLANK_TRUE)
	role = models.CharField("角色", max_length=255, default="", **NULL_BLANK_TRUE)
	url = models.CharField("项目链接", max_length=255, default="", **NULL_BLANK_TRUE)
	start_time = models.CharField("项目起始时间", max_length=255, default="", **NULL_BLANK_TRUE)
	end_time = models.CharField("项目终止时间", max_length=255, default="", **NULL_BLANK_TRUE)
	description = models.TextField("项目描述", default="", **NULL_BLANK_TRUE)
	performance = models.TextField("项目业绩", default="", **NULL_BLANK_TRUE)

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
	school = models.CharField("学校名称", max_length=255, default="", **NULL_BLANK_TRUE)
	discipline = models.CharField("所学专业", max_length=255, default="", **NULL_BLANK_TRUE)
	education = models.CharField("学历", max_length=255, default="", **NULL_BLANK_TRUE)
	start_time = models.CharField("起始时间", max_length=255, default="", **NULL_BLANK_TRUE)
	end_time = models.CharField("终止时间", max_length=255, default="", **NULL_BLANK_TRUE)
	experience = models.TextField("在校经历", default="", **NULL_BLANK_TRUE)

	def __str__(self):
		return self.school

	class Meta:
		db_table = 'EducationExperience'
		verbose_name = "教育经历"
		verbose_name_plural = "教育经历"
		ordering = ['-id']
		index_together = ["custom_user"]
