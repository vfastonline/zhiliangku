#!encoding:utf-8
from django.conf.urls import url

import collect_course
import common_question
import nodus_views
import student_notes
import course_list
import live
import path_list
import poly_upload_video
import video_list
import projects_list


urlpatterns = [
	url('^technology/list/info$', projects_list.TechnologyListInfo.as_view()),  # 技术分类

	url('^projects/list/info$', projects_list.ProjectListInfo.as_view()),  # 项目信息列表
	url('^projects/list/$', projects_list.ProjectList.as_view(), name='projects'),  # 项目信息列表页面

	url('^projects/detail/$', projects_list.ProjectDetail.as_view()),  # 项目详情--页面
	url('^projects/detail/info$', projects_list.ProjectDetailInfo.as_view()),  # 项目详情--信息

	url('^course/detail/$', course_list.CourseDetail.as_view()),
	url('^course/detail/info$', course_list.CourseDetailInfo.as_view()),

	url('^common_question/list/info$', common_question.CommonQuestionList.as_view()),  # 视频常见问题
	url('^nodus/list/info$', nodus_views.NodusList.as_view()),  # 视频难点解析
	url('^next/video$', video_list.GetNextVideo.as_view()),  # 获取下一节视频信息

	# 视频详情，观看页
	url('^video/detail/$', video_list.VideoDetail.as_view()),
	url('^video/detail/info$', video_list.VideoDetailInfo.as_view()),

	# 学生笔记
	url('^student/notes/list/info$', student_notes.StudentNotesList.as_view()),  # 学生笔记
	url('^student/add/notes/info$', student_notes.AddStudentNotes.as_view()),  # 增加--学生笔记

	# url('^project/list/info$', path_list.ParticipateProject.as_view()),  # 参与学习项目

	# url('^index_path/list$', path_list.IndexPathList.as_view()),
	url('^index_course/list$', course_list.IndexCourseList.as_view()),

	# url('^path/list/$', path_list.PathList.as_view()),
	# url('^path/list/info$', path_list.PathListInfo.as_view()),

	# url('^path/detail/$', path_list.PathDetail.as_view()),
	# url('^path/detail/info$', path_list.PathDetailInfo.as_view()),

	url('^course/list/$', course_list.CourseList.as_view()),
	url('^course/list/info$', course_list.CourseListInfo.as_view()),
	url('^search/course/list/info$', course_list.SearchForCourse.as_view()),

	url('^collect/course$', collect_course.CollectCourse.as_view()),

	url('^video/list/info$', video_list.VideoList.as_view()),



	# 直播详情，观看页
	url('^live/detail/$', live.LiveDetail.as_view()),
	url('^live/detail/info$', live.LiveDetailInfo.as_view()),

	# 获取上传视频参数
	url('^get-polyv$', poly_upload_video.UploadVideoPolyvParam.as_view()),

	# 问题方向
	url('^question/path/info$', course_list.QuestionPathInfo.as_view()),
]
