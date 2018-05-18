import Vue from 'vue'
import VueLazyload from 'vue-lazyload'
import {Notification} from 'element-ui'

Vue.use(VueLazyload)
Vue.prototype.$notify=Notification
