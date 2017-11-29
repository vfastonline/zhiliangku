// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false
// 引入样式表
//引入选择的插件
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Echarts from 'echarts'
Vue.use(ElementUI)
Vue.prototype.$echarts=Echarts
//引入自写组件
import ProjectHeader from './components/home/projectHeader.vue'
import PostMatch from './components/home/postMatch.vue'
import Carousel from './components/home/carousel.vue'
import Subtitle from './components/home/subtitle.vue'
import HotCourse from './components/home/hotCourse.vue'
import CareerPathSection from './components/home/careerPathSection.vue'
import InterviewCover from './components/home/interviewCover.vue'
import ProjectFooter from './components/home/projectFooter.vue'
import Cooperator from './components/home/cooperator.vue'
Vue.component('projectHeader',ProjectHeader)
Vue.component('postMatch',PostMatch)
Vue.component('carousel',Carousel)
Vue.component('subtitle',Subtitle)
Vue.component('hotCourse',HotCourse)
Vue.component('carrerps',CareerPathSection)
Vue.component('interviewCover',InterviewCover)
Vue.component('projectFooter',ProjectFooter)
Vue.component('cooperator',Cooperator)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
