import MyConst from './01_const'
import './02_bus'
import './03_http'
import fn from './04_ulit'
import Vue from 'vue'

Vue.prototype.$fn = fn
Vue.prototype.$myConst = MyConst
