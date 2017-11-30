from django.conf.urls import url

import course_list
import path_list

urlpatterns = [
    url('^path/list$', path_list.PathList.as_view()),
    url('^course/list$', course_list.CourseList.as_view()),
]
