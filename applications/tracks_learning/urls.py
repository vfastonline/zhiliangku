from django.conf.urls import url

import course_list
import path_list
import video_list
import views

urlpatterns = [
    url('^index_path/list$', path_list.IndexPathList.as_view()),
    url('^index_course/list$', course_list.IndexCourseList.as_view()),

    url('^path/list/$', path_list.PathList.as_view()),
    url('^path/list/info$', path_list.PathListInfo.as_view()),

    url('^path/detail/$', path_list.PathDetail.as_view()),
    url('^path/detail/info$', path_list.PathDetailInfo.as_view()),

    url('^course/list/$', course_list.CourseList.as_view()),
    url('^course/list/info$', course_list.CourseListInfo.as_view()),

    url('^course/detail/$', course_list.CourseDetail.as_view()),
    url('^course/detail/info$', course_list.CourseDetailInfo.as_view()),

    url('^video/list/info$', video_list.VideoList.as_view()),
]
