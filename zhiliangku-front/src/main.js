// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false
//引入脚本
import fn from './utils/index'
Vue.prototype.$fn=fn;
import Obj from './assets/js/const'
Vue.prototype.$myConst=Obj;
//引入选择的插件
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Echarts from 'echarts'

// 引入样式表
import './style/base/modifiedel.css'
//这个组件目前还未用到
import ScrollBar from 'vue2-scrollbar'
import 'vue2-scrollbar/dist/style/vue2-scrollbar.css'
// 为用到组件结束，需要删除
import Moment from 'moment'

Vue.use(ElementUI)
Vue.prototype.$echarts=Echarts;


import Axios from 'axios'
Axios.defaults.baseURL = Obj.httpUrl;

// Axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
Vue.prototype.$ajax=Axios;
//引入自写小组件
//home
import ProjectHeader from './components/home/projectHeader.vue'
import PostMatch from './components/home/postMatch.vue'
import Carousel from './components/home/carousel.vue'
import Subtitle from './components/home/subtitle.vue'
import HotCourse from './components/home/hotCourse.vue'
import CareerPathSection from './components/home/careerPathSection.vue'
import InterviewCover from './components/home/interviewCover.vue'
import ProjectFooter from './components/home/projectFooter.vue'
import Cooperator from './components/home/cooperator.vue'
import LiveVideoStreaming from './components/home/liveVideoStreaming.vue'
// courseInfo
import CourseSelect from './components/courseInfo/courseSelect.vue'
import ProjectPager from './components/courseInfo/pager.vue'
import BeforeAdd from './components/courseInfo/BeforeAdd.vue'
import PathInfoLeft from './components/courseInfo/pathInfoLeft.vue'
import PathInfoRight from './components/courseInfo/pathInfoRight.vue'
import CareerPathCarousel from './components/courseInfo/careerPathCarousel.vue'
import Container from './components/courseInfo/container.vue'
//login
import LoginCommenLis from './components/login/commenLi.vue'
import Login from './components/login/login.vue'
//引入混合组件
// home
import LiveVideoStreamingMain from './components/home/liveVideoStreamingMain.vue'
import HotCourseMain from './components/home/hotCourseMain.vue'
import CareerPathMain from './components/home/careerPathMain.vue'
import InterviewMain from './components/home/interviewMain.vue'
import ProjectHome from './components/home/home.vue'
// courseInfo
import PathInfo from './components/courseInfo/pathInfo.vue'
import CareerPathList from './components/courseInfo/careerPathList.vue'



//声明自写小组件
//首页部分
//home
Vue.component('projectHeader',ProjectHeader)
Vue.component('postMatch',PostMatch)
Vue.component('carousel',Carousel)
Vue.component('subtitle',Subtitle)
Vue.component('hotCourse',HotCourse)
Vue.component('carrerps',CareerPathSection)
Vue.component('interviewCover',InterviewCover)
Vue.component('projectFooter',ProjectFooter)
Vue.component('cooperator',Cooperator)
Vue.component('lvs',LiveVideoStreaming)
Vue.component('projectHome',ProjectHome)
//courseInfo
Vue.component('courseSelect',CourseSelect)
Vue.component('projectPager',ProjectPager)
Vue.component('beforeAdd',BeforeAdd)
Vue.component('pathInfoLeft',PathInfoLeft)
Vue.component('pathInfoRight',PathInfoRight)
Vue.component('careerPathCarousel',CareerPathCarousel)
Vue.component('container',Container)
//login
Vue.component('loginCommenLis',LoginCommenLis)
Vue.component('login',Login)
//声明自写混合组件
//home
Vue.component('lvsm',LiveVideoStreamingMain)
Vue.component('hcm',HotCourseMain)
Vue.component('cpm',CareerPathMain)
Vue.component('interviewMain',InterviewMain)
Vue.component('pathInfo',PathInfo)
//courseInfo
Vue.component('careerPathList',CareerPathList)
// 过滤器
Vue.filter("turnToThu",function(value){
  return parseInt(value/1000)+'k'
})

//自写函数
Vue.prototype.$vueself=function(){
  return this;
}
Vue.prototype.deepCopy=function(obj){
  return JSON.parse(JSON.stringify(obj))
}
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
