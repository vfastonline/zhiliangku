// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
// import router from './router'

Vue.config.productionTip = false
//引入脚本
import fn from '../../utils/index'
Vue.prototype.$fn = fn;
import Obj from '../../assets/js/const'
Vue.prototype.$myConst = Obj;
//引入选择的插件
import ElementUI from 'element-ui'
// import { Button,Carousel,Scrollbar,CarouselItem } from 'element-ui'
//目前来看实现element-ui的部分调用比较难//但是依然是一个很好的解决方案
// Vue.component('elButton',Button)
// Vue.component('elCarousel',Carousel)
// Vue.component('elScrollbar',Scrollbar)
// Vue.use(CarouselItem)
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)
var sd = {};
// 引入样式表
import '../../style/base/modifiedel.css'
// import Moment from 'moment'
import '../../utils/axios'

import VueLazyLoad from 'vue-lazyload'
console.log(Obj)
Vue.use(VueLazyLoad,{
    loading:Obj.httpUrl+'/media/course/20180116/20180116151859_987.jpg'
})


//引入自写小组件
//home
import ProjectHeader from '../../components/home/projectHeader.vue'
import myCarousel from '../../components/home/carousel.vue'
import Subtitle from '../../components/home/subtitle.vue'
import HotCourse from '../../components/home/hotCourse.vue'
import CareerPathSection from '../../components/home/careerPathSection.vue'
import InterviewCover from '../../components/home/interviewCover.vue'
import ProjectFooter from '../../components/home/projectFooter.vue'
import Cooperator from '../../components/home/cooperator.vue'
import LiveVideoStreaming from '../../components/home/liveVideoStreaming.vue'
// courseInfo
import Container from '../../components/courseInfo/container.vue'

//login
import Login from '../../components/login/login.vue'

//引入混合组件

// home
import LiveVideoStreamingMain from '../../components/home/liveVideoStreamingMain.vue'
import HotCourseMain from '../../components/home/hotCourseMain.vue'
import CareerPathMain from '../../components/home/careerPathMain.vue'
import ProjectHome from '../../components/home/home.vue'
// import default from 'axios';


//声明自写小组件
//首页部分
//home
Vue.component('projectHeader', ProjectHeader)
Vue.component('carousel', myCarousel)
Vue.component('subtitle', Subtitle)
Vue.component('hotCourse', HotCourse)
Vue.component('carrerps', CareerPathSection)
Vue.component('interviewCover', InterviewCover)
Vue.component('projectFooter', ProjectFooter)
Vue.component('cooperator', Cooperator)
Vue.component('lvs', LiveVideoStreaming)
Vue.component('projectHome', ProjectHome)
Vue.component('container', Container)

//login
Vue.component('login',Login)
//声明自写混合组件
//home
Vue.component('lvsm', LiveVideoStreamingMain)
Vue.component('hcm', HotCourseMain)
Vue.component('cpm', CareerPathMain)
//courseInfo
// 过滤器
Vue.filter("turnToThu", function (value) {
  return parseInt(value / 1000) + 'k'
})

//自写函数
Vue.prototype.$vueself = function () {
  return this;
}
Vue.prototype.deepCopy = function (obj) {
  return JSON.parse(JSON.stringify(obj))
}
/* eslint-disable no-new */
var indexvue = new Vue({
  el: '#app',
  // router,
  template: '<App/>',
  components: {
    App
  }
})
//此处作用是为了在拦截器中能够快速的访问到vue实例
// indexvue.$ajax.vue=indexvue
sd.vue = indexvue;
