import Vue from 'vue'
Vue.prototype.getSelf = function () {
  return this
}
Vue.prototype.deepCopy = function (obj) {
  return JSON.parse(JSON.stringify(obj))
}
Vue.prototype.initForm = function (vue, obj, keys1, keys2) {
  for (var i = 0; i < keys1.length; i++) {
    vue[keys2[i]] = obj[keys1[i]];
  }
}
Vue.prototype.changebr = function (value) {
  if (typeof(value) == 'undefined') {
    return ''
  }
  return value.replace(/\n|\r\n/g, "<br>")
}
Vue.prototype.changen = function (value) {
  if (typeof(value) == 'undefined') {
    return ''
  }
  return value.replace(/<br>/g, '\n')
}
