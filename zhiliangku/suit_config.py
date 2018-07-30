# encoding: utf8
DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'
SUIT_CONFIG = {
	# header
	'ADMIN_NAME': '智量酷',
	'HEADER_DATE_FORMAT': 'Y-m-d',
	'HEADER_TIME_FORMAT': 'H:i:s',

	# forms
	# 'SHOW_REQUIRED_ASTERISK': True,  # Default True，自动将星号符号*添加到每个必填字段标签的末尾
	# 'CONFIRM_UNSAVED_CHANGES': True, # Default True，当您尝试离开页面时，将显示警报，而不是先保存更改的表格

	# menu
	# 'SEARCH_URL': '/admin/auth/user/',
	# 'MENU_ICONS': {
	#    'sites': 'icon-leaf',
	#    'auth': 'icon-lock',
	# },
	# 'MENU_OPEN_FIRST_CHILD': True, # Default True
	# 'MENU_EXCLUDE': ('auth.group',),
	'MENU': (
		'sites',
		{'app': 'auth', 'icon': 'icon-lock', 'models': ('user', 'group')},

		# {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
		# {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},

		# 首页相关--轮播图
		{'app': 'slideshow', 'icon': 'icon-repeat', "models": ("Carousel", "WebsiteIntroduce", "RecruitmentPlan")},

		# 用户管理
		{'app': 'custom_user', 'icon': 'icon-user',
		 'models': (
		 'tracks_learning.CustomUserClass', 'CustomUser', 'CustomUserAuths', 'CustomUserProject', "CustomUserCourse", "VerifyCode")},

		# 个人中心
		{'app': 'personal_center', 'icon': 'icon-star',
		 'models': ('Resume', 'CareerObjective', 'WorkExperience', "ProjectExperience", "EducationExperience")},

		# 课程
		{'label': '项目-课程', 'app': 'tracks_learning', 'icon': 'icon-bookmark',
		 'models': (
			 "Technology",
			 'Project',
			 'Course',
			 'Section',
			 "Video",
			 "CommonQuestion",
			 "Nodus",
			 "UnlockVideo",
			 # 'CoursePath',
			 # "Faq",
			 # "FaqAnswer",
			 "StudentNotes",
			 "record.WatchRecord"
		 )},

		# Docker字典
		{'label': 'Docker字典', 'app': 'assessment', 'icon': 'icon-comment', 'models': ('DockerType', 'DockerPort')},

		# 练习题
		{'app': 'exercise', 'icon': 'icon-th', },

		# 社区问答
		{'app': 'community', 'icon': 'icon-comment',
		 'models': ('Faq', 'FaqAnswer', "FaqAnswerReply", "FaqAnswerFeedback")},

		# 勋章
		{'label': '勋章', 'app': 'medal', 'icon': 'icon-list-alt', 'models': ('Medal', 'CustomUserMedal')},
		{'label': '消息中心', 'app': 'notification', 'icon': 'icon-list-alt'},

		# 微信推广
		{'label': '微信推广', 'app': 'wechat_promotion', 'icon': 'icon-list-alt',
		 'models': ('WechatBrowse', 'WechatBackground', 'WechatRemark', "WechatMusic")},

		# 世界杯-答题-猜球
		{'label': '世界杯', 'app': 'world_cup', 'icon': 'icon-list-alt',
		 'models': ("Tournament", "Analysis", "Topic", "Country", "BetRecord", "BetRecordCount",)},

		# 后台-首页
		{'label': '教师端-首页', 'app': 'home', 'icon': 'icon-list-alt', 'models': ('LearnTask', "LearnTaskSummary")},

		# 后台-考核统计
		{'label': '教师端-考核统计', 'app': 'exam_statistics', 'icon': 'icon-list-alt'},
		# # 观看进度
		# {'app': 'record', 'icon': 'icon-list-alt', 'models': ('WatchRecord',)},

		# # 直播
		# {'label': '保利威视-直播间', 'app': 'live_streaming', 'icon': 'icon-film', },

		# # 公司招聘职位
		# {'app': 'company_jobs', 'icon': 'icon-briefcase', },

		# # 积分商城
		# {'label': '积分商城', 'app': 'integral', 'icon': 'icon-shopping-cart',
		#  'models': ('Goods', 'ExchangeRecords')},

	),

	# misc
	# 'LIST_PER_PAGE': 15
}
