import MyConst from './01_const'
import './02_bus'
import './03_http'
import fn from './04_ulit'
import Vue from 'vue'
import './05_project_base'

Vue.prototype.$fn = fn
Vue.prototype.$myConst = MyConst
