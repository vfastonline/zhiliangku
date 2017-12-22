from django.conf.urls import url
import faq

urlpatterns = [
    url('^faq/list/info$', faq.FaqList.as_view()),
    url('^add/faq$', faq.AddFaq.as_view()),
    url('^add/answerfaq$', faq.AddAnswerFaq.as_view()),
]
