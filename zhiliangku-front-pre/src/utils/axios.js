import Vue from 'vue'
import Axios from 'axios'
import Obj from '../assets/js/const'
import { get } from 'http';
Axios.defaults.withCredentials = true;
Axios.defaults.baseURL = Obj.httpUrl;
// 此处写拦截函数
function lanjie(res,obj) {
  var showNotify = function (callback) {
    var nds = obj.$notify({
      type: 'error',
      message: res.data.msg,
      offset: 100,
      duration: 3000,
      position: 'bottom-right'
    });
    var notifies = document.getElementsByClassName(nds.$el.className);
    for (var notifiesIndex = 0; notifiesIndex < notifies.length; notifiesIndex++) {
      notifies[notifiesIndex].style.zIndex = 20000;
    }
    if (callback) {
      callback()
    }
  }
  switch (res.data.err) {
    case 1: 
    showNotify()
    break;
    case 2:
      obj.$children[0].$children[0].$children[0].$emit('open','loginActive');
      showNotify()
      break
    case 3:
      showNotify()
      break
    case 4:
      showNotify()
      obj.$children[0].$children[0].$children[0].$emit('noActive', 'loginActive');
      obj.$children[0].$children[0].$children[0].$emit('logupTologin')
      break
    case 5:
      showNotify()
      break
    case 6:
      showNotify()
      obj.$children[0].$children[0].$children[0].$emit('noActive', 'emailVerifyAginActive')
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
  return res;
}
//获取最顶级的vue实例
function getparent(obj){
  if(!obj.$parent){return obj}
  return getparent(obj.$parent)
}
// 分别封装了get，post请求方法
Vue.prototype.$post = function (url, options) {
  return Axios.post(url, options).then(response => {
    // console.log(this)
    // console.log(response)
    var bigVueInc=getparent(this)
    console.log(bigVueInc)
    lanjie(response,bigVueInc)
    return new Promise(function (resolve, reject) {
      resolve(response)
    })
  })
}
Vue.prototype.$get = function (url, options) {
  return Axios.get(url, options).then(response => {
    // console.log(this)
    // console.log(response)
    var bigVueInc=getparent(this)
    // console.log(bigVueInc)
    lanjie(response,bigVueInc)
    return new Promise(function (resolve, reject) {
      resolve(response)
    })
  })
}
