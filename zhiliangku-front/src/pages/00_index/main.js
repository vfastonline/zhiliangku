// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './app'
import '../../assets/js/index'
import '../../assets/style/baseScss.scss'
// import ElementUI from 'element-ui'
// Vue.use(ElementUI)
Vue.config.productionTip = false
console.log(process.env.NODE_ENV)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})
