![](https://www.zhiliangku.com/static/img/Logo.a827faf.png)
# 智量酷
## Zhiliangku - A Smart classroom 
[官方主页](https://www.zhiliangku.com "智量酷")

#### Directory description
* applications：包含项目所有应用
    * assessment：考核
    * community：社区问答
    * company_jobs：公司招聘职位
    * custom_user：用户管理
    * exercise：习题
    * face：面部识别
    * integral：积分商城
    * interview_question：企业面试题
    * live_streaming：直播
    * personal_center：个人中心
    * record：视频观看记录
    * slideshow：轮播图
    * tracks_learning：职业路径
* conf：配置文件
* doc：相关文档
* lib：公用工具
* media：模块产生图片
* templates：模板
* top：第三方库，阿里巴巴短信
* zhiliangku：总路由，包含settings
* zhiliangku-front：前端编译后文件

### Introduce
* assessment：考核
    > 平台针对学员学习情况进行标准化考核，
    考核结果决定是否进入下一阶段学习，
    讲师在页面提供习题（选择、判断、实操），
    学员通过平台运用Docker生成的shell输入框进行答题，
    由后台统一判题并给出答案。
* community：社区问答
    > 平台提供一个可以让所有用户角色沟通的社区，
    功能类似论坛，
    功能包括：留言、评论、赞、踩、通过回答最佳答案赚取积分。
* company_jobs：公司招聘职位
    > 平台针对企业，发布最近要招聘的职位信息。
* custom_user：用户管理
    > 管理不同角色用户信息，包括：学生、讲师、HR
* exercise：习题
    > 针对指定课程视频，由讲师设计的课后练习题，
    以巩固知识，
    同时记录学员答题记录，
    方便班主任及时并直观的分析学员学习情况。
* face：面部识别
    > 平台通过摄像头捕捉学员观看视频课程时的面部表情，
    辅助分析学员对课程的情绪，帮助讲师更好的优化课程视频。
* integral：积分商城
    > 发布不同积分对应奖品，
    学员可通过回答其他人在社区中的提问，
    赚取响应积分，并可以换取实物。
* interview_question：企业面试题
    > 平台针对不同企业，为学员提供往年企业面试真题，
    并提供答题环节，并记录答题信息。
* live_streaming：直播
    > 平台对接保利威视提供的视频点播和直播服务，
    管理员可通过智量酷后台上传视频课程托管，
    还可在后台创建直播频道，提供在线直播课程。
* personal_center：个人中心
    > 包括：我的简历，积分商城，我的路线，关注我的企业；
    查看自己学习总时长。
* record：视频观看记录
    > 通过播放器控件，记录用户各自看过课程视频的进度，
    方便汇总学员学习进度，并能按播放历史续播。
* slideshow：轮播图
    > 提供主页和其他宣传类页面轮播图管理。
* tracks_learning：职业路径
    > 平台提供丰富的学习路径，路径根据职业类型划分。

#### Requirements
* Python==3.6
* Django==2.1
* PyMySQL
* mysqlclient
* requests==2.19.1
* django-colorfield==0.1.15
* Django-Select2==6.1.2
* django-suit==0.2.26
* pycrypto==2.6.1
* django-cors-headers==2.4.0
* django-multiselectfield==0.1.8
* django-breadcrumbs==1.1.3
* redis==2.10.6
* djangorestframework==3.8.2
* markdown==2.6.11
* django-filter==2.0.0
* ujson==1.35
* pillow==5.2.0

#### Installation
```
git clone https://github.com/vfastonline/zhiliangku.git
cd zhiliangku 
pip install -r requirements.txt
cp -r doc/image media
```

#### Scheduled task
```
定时销毁超时的考核容器
0 */1 * * * /usr/local/bin/python /usr/local/zhiliangku/manage.py destroydocker

定时（10：30am）汇总世界杯比赛结果
30 10 * * * /usr/local/bin/python /usr/local/zhiliangku/manage.py SummaryCompetition

# 每小时汇总每个学员当天任务学习进度
0 */1 * * * /usr/local/bin/python /usr/local/zhiliangku/manage.py SummaryUserLearnTaskSchedule

# 每天23:50汇总当天总学习任务进度
50 23 * * * /usr/local/bin/python /usr/local/zhiliangku/manage.py SummaryLearnTaskSchedule
```

#### Architecture
* git, vue

