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

// 引入样式表
import '../../style/base/modifiedel.css'
//这个组件目前还未用到
// import Moment from 'moment'

Vue.use(ElementUI)
Vue.prototype.$echarts=Echarts;


import Axios from 'axios'
Axios.defaults.baseURL = Obj.httpUrl;

// Axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
Vue.prototype.$ajax=Axios;
//引入自写小组件
//home
import ProjectHeader from '../../components/home/projectHeader.vue'
import PostMatch from '../../components/home/postMatch.vue'
import ProjectFooter from '../../components/home/projectFooter.vue'
// courseInfo
import BeforeAdd from '../../components/courseInfo/BeforeAdd.vue'
//login
import LoginCommenLis from '../../components/login/commenLi.vue'
import Login from '../../components/login/login.vue'
import Logup from '../../components/login/logup.vue'
import VerificationCode from '../../components/login/verificationCode.vue'
import GetPassword from '../../components/login/getPassword.vue'
import LogupSuccess from '../../components/login/logupSuccess.vue'
//引入混合组件
// home
// courseInfo



//声明自写小组件
//首页部分
//home
Vue.component('projectHeader',ProjectHeader)
Vue.component('postMatch',PostMatch)
Vue.component('projectFooter',ProjectFooter)
//courseInfo
Vue.component('beforeAdd',BeforeAdd)
//login
Vue.component('loginCommenLis',LoginCommenLis)
Vue.component('login',Login)
Vue.component('logup',Logup)
Vue.component('verificationCode',VerificationCode)
Vue.component('getPassword',GetPassword)
Vue.component('logupSuccess',LogupSuccess)
//声明自写混合组件
//home
//courseInfo
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
