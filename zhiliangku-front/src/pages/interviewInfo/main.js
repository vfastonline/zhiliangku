import Vue from 'vue'
import App from './App'
Vue.config.productionTip = false
//引入脚本
import fn from '../../utils/index'
Vue.prototype.$fn = fn;
import Obj from '../../assets/js/const'
Vue.prototype.$myConst = Obj;
//引入选择的插件
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)
import '../../utils/axios'
Vue.prototype.deepCopy = function (obj) {
  return JSON.parse(JSON.stringify(obj))
}

var indexvue = new Vue({
  el: '#app',
  template: '<App/>',
  components: {
    App
  }
})
