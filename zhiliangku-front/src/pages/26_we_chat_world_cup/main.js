// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './app'
import '../../assets/js/index'
import '../../assets/style/baseScss.scss'
import './scss/_base.scss'
import './js/01_rem'
import './js/03_wx'
import 'mint-ui/lib/style.min.css'
import mui from 'mint-ui'
import inhence_num from './01_components/12_inhence_num'
Vue.use(mui)
Vue.config.productionTip = false
Vue.component('num', inhence_num)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: {
    App
  },
  template: '<App/>'
})
