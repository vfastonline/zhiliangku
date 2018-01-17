// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
// import router from './router'

Vue.config.productionTip = false
//引入脚本
import fn from '../../utils/index'
Vue.prototype.$fn=fn;
import Obj from '../../assets/js/const'
Vue.prototype.$myConst=Obj;
//引入选择的插件
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Echarts from 'echarts'
Vue.use(ElementUI)
// 引入样式表
import '../../style/base/modifiedel.css'

// 为用到组件结束，需要删除
// import Moment from 'moment'


Vue.prototype.$echarts=Echarts;


import '../../utils/axios'
//引入自写小组件
//home
import ProjectHeader from '../../components/home/projectHeader.vue'
import PostMatch from '../../components/home/postMatch.vue'
import Carousel from '../../components/home/carousel.vue'
import InterviewCover from '../../components/home/interviewCover.vue'
import ProjectFooter from '../../components/home/projectFooter.vue'
import CareerPathCarousel from '../../components/courseInfo/careerPathCarousel.vue'
import Container from '../../components/courseInfo/container.vue'
//login
import Login from '../../components/login/login.vue'

//引入混合组件
// home
import CareerPathList from '../../components/courseInfo/careerPathList.vue'



//声明自写小组件
//首页部分
//home
Vue.component('projectHeader',ProjectHeader)
Vue.component('postMatch',PostMatch)
Vue.component('interviewCover',InterviewCover)
Vue.component('projectFooter',ProjectFooter)
//courseInfo
Vue.component('careerPathCarousel',CareerPathCarousel)
Vue.component('container',Container)
//login

Vue.component('login',Login)

//声明自写混合组件
//home
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
  // router,
  template: '<App/>',
  components: { App }
})
