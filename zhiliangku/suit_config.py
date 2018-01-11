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

        # 用户管理
        {'app': 'custom_user',
         'models': ('CustomUser', 'CustomUserAuths', 'CustomUserPath', "CustomUserCourse", "VerifyCode")},

        # 个人中心
        {'app': 'personal_center',
         'models': ('Resume', 'CareerObjective', 'WorkExperience', "ProjectExperience", "EducationExperience")},

        # 职业路径
        {'app': 'tracks_learning', 'models': ('Path', 'PathStage', 'CourseCategory')},

        # 课程
        {'label': '课程', 'app': 'tracks_learning',
         'models': ('Course', 'Section', "Video", "CommonQuestion", 'CoursePath', "Technology", "Faq", "FaqAnswer")},

        # 观看进度
        {'app': 'record', 'models': ('WatchRecord',)},

        # 直播
        {'app': 'live_streaming'},

        # 习题
        {'app': 'exercise'},

        # 轮播图
        {'app': 'slideshow'},

        # 企业面试题
        {'app': 'interview_question',
         'models': ('EnterpriseInfo', 'ExaminationQuestion', 'ExaminationAnswer',
                    "AnswerRecord", "CompletedInterviewQuestion")},

        # 公司招聘职位
        {'app': 'company_jobs'},

        # 社区问答
        {'app': 'community', 'models': ('Faq', 'FaqAnswer', "FaqAnswerReply")},
    ),

    # misc
    # 'LIST_PER_PAGE': 15
}
