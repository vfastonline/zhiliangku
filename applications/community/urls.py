#!encoding:utf-8
from django.conf.urls import url

import faq
import faq_answer
import faq_answer_reply

urlpatterns = [
	# 问题
	url('^faq/list/$', faq.FaqList.as_view()),
	url('^faq/list/info$', faq.FaqListInfo.as_view()),
	url('^faq/detail/$', faq.FaqDetai.as_view()),
	url('^faq/detail/info$', faq.FaqDetaiInfo.as_view()),
	url('^get/faqbytitle$', faq.GetFaqByTitle.as_view()),
	url('^follow/faq$', faq.FollowFaq.as_view()),
	url('^unfollow/faq$', faq.UnFollowFaq.as_view()),
	url('^add/faq$', faq.AddFaq.as_view()),
	url('^del/faq$', faq.DelFaq.as_view()),
	url('^edit/faq$', faq.EditFaq.as_view()),

	# 回答
	url('^appraisal/faqanswer$', faq_answer.AppraisalFaqAnswer.as_view()),
	url('^accept/faqanswer$', faq_answer.AcceptFaqAnswer.as_view()),
	url('^add/faqanswer$', faq_answer.AddFaqAnswer.as_view()),
	url('^del/faqanswer$', faq_answer.DelFaqAnswer.as_view()),
	url('^edit/faqanswer$', faq_answer.EditFaqAnswer.as_view()),

	# 回答-回复
	url('^add/faqanswerreply$', faq_answer_reply.AddFaqAnswerReply.as_view()),
	url('^del/faqanswerreply$', faq_answer_reply.DelFaqAnswerReply.as_view()),
	url('^edit/faqanswerreply$', faq_answer_reply.EditFaqAnswerReply.as_view()),
]
