from django.conf.urls import url

import course_list
import path_list
import video_list

urlpatterns = [
    url('^path/list$', path_list.PathList.as_view()),
    url('^path/detail$', path_list.PathDetail.as_view()),
    url('^course/list$', course_list.CourseList.as_view()),
    url('^course/detail$', course_list.CourseDetail.as_view()),
    url('^video/list$', video_list.VideoList.as_view()),
]
