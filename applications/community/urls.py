#!encoding:utf-8
from django.conf.urls import url
import faq
import faq_answer
import faq_answer_reply

urlpatterns = [
    url('^faq/list/$', faq.FaqList.as_view()),
    url('^faq/list/info$', faq.FaqListInfo.as_view()),
    url('^faq/detail/$', faq.FaqDetai.as_view()),
    url('^faq/detail/info$', faq.FaqDetaiInfo.as_view()),
    url('^get/faqbytitle$', faq.GetFaqByTitle.as_view()),
    url('^add/faq$', faq.AddFaq.as_view()),
    url('^follow/faq$', faq.FollowFaq.as_view()),
    url('^appraisal/faqanswer$', faq_answer.AppraisalFaqAnswer.as_view()),
    url('^accept/faqanswer$', faq_answer.AcceptFaqAnswer.as_view()),
    url('^add/faqanswer$', faq_answer.AddFaqAnswer.as_view()),
    url('^add/faqanswerreply$', faq_answer_reply.AddFaqAnswerReply.as_view()),
]
