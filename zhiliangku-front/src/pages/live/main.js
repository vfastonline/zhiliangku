import Vue from 'vue'
import App from './App'
import router from '../../router/videorouter'
// import router from './router'
Vue.config.productionTip = false
//引入脚本
import fn from '../../utils/index'
Vue.prototype.$fn = fn;
import Obj from '../../assets/js/const'
Vue.prototype.$myConst = Obj;
//引入选择的插件
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Echarts from 'echarts'
Vue.use(ElementUI)
Vue.prototype.$echarts = Echarts;
// 引入样式表
import '../../style/base/modifiedel.css'
import '../../utils/axios'

// 引入组件
import  videoView from '../../components/videoDetail/video'
Vue.component('videoView',videoView)
import videoContent from '../../components/videoDetail/videoContent.vue'
Vue.component('videoContent',videoContent)

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
  router,
  template: '<App/>',
  components: {
    App
  }
})
