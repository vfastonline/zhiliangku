import Vue from 'vue'
import Axios from 'axios'
import Obj from './01_const.js'
import Bus from './02_bus'


Axios.defaults.withCredentials = true
Axios.defaults.baseURL = Obj.httpUrl
// 此处写拦截函数
var intercept = function (res, obj) {
  var showNotify = function (callback) {
    debugger
    var nds = obj.$notify({
      type: 'error',
      message: res.data.msg,
      offset: 100,
      duration: 3000,
      position: 'bottom-right'
    })
    var notifies = document.getElementsByClassName(nds.$el.className)
    for (
      var notifiesIndex = 0; notifiesIndex < notifies.length; notifiesIndex++
    ) {
      notifies[notifiesIndex].style.zIndex = 20000
    }
    if (callback) {
      callback()
    }
  }
  switch (res.data.err) {
    case 1:
      showNotify()
      break
    case 2:
      showNotify()
      Bus.$emit('specify_display',{show_key:'log_up',title_key:'登录'})
      break
    case 3:
      showNotify()
      break
    case 4:
      showNotify()
      Bus.$emit('specify_display',{show_key:'log_in',title_key:'登录'})
      break
    case 5:
      showNotify()
      break
    case 6:
      showNotify()
      break
    case 7:
      showNotify()
      break
    case 8:
      showNotify()
      break
    default:
      break
  }
  return res
}
// 获取最顶级的vue实例
// 分别封装了get，post请求方法
Vue.prototype.$post = function (url, options) {
  return Axios.post(url, options).then(response => {
    intercept(response, this)
    return new Promise(function (resolve, reject) {
      resolve(response)
    })
  })
}
Vue.prototype.$get = function (url, options) {
  return Axios.get(url, options).then(response => {
    intercept(response, this)
    return new Promise(function (resolve, reject) {
      resolve(response)
    })
  })
}
