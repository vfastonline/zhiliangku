from django.conf.urls import url

import path_list, course_list

urlpatterns = [
    url('^path/list$', path_list.PathList.as_view()),
    url('^course/list$', course_list.CourseList.as_view()),
]
