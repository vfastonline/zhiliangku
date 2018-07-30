// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './app'
import Vuex from 'vuex'
import '../../assets/js/index'
import '../../assets/style/baseScss.scss'
Vue.config.productionTip = false
let store = new Vuex.Store({
  state:{},
})
/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  components: { App },
  template: '<App/>'
})
