// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './app'
import '../../assets/js/index'
import '../../assets/style/baseScss.scss'
import './javascripts/01_wx'
import './javascripts/02_rem'
import 'mint-ui/lib/style.min.css'
var $ = window.$
$.xiejiabing = 'man'
Vue.prototype.$is_empty = function (params) {
  var blo = JSON.stringify(params) === '{}'
  return blo
}
Vue.mixin({
  props: {
    image_url: {},
    main_data: {}
  },
  computed: {
    url() {
      return 'url(' + this.$myConst.httpUrl + this.image_url + ')'
    }
  }
})
Vue.config.productionTip = false
/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: {
    App
  },
  template: '<App/>'
})
