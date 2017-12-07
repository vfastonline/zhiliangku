module.exports = (function () {
  var fn = {};
  //切换显隐开关的函数，支持传入数组、index，对象、key，show。该函数还有优化空间。
  fn.changeShow = function (arr) {
    console.log(arr)
    var show = arr[1],
      index = arr[2];
    console.log(this)
    if (typeof index != 'undefined') {
      if (this.show instanceof Array) {
        this.show.splice(index, 1, !this.show[index])
        return show
      }
      if (show instanceof Object) {
        this.show.index = !this.show.index;
        return show
      }
    }
    this.show = !this.show;
    return show
  }
  //将字符串拼接，并且将原来变量进行了改变。
  // 该方法支持全是没有修饰的arr，以及arr盛着的对象的多个未修饰的key
  fn.addString = function (str, arr, key) {
    if (arr instanceof Array) {
      for (var i = 0; i < arr.length; i++) {
        if (!key) {
          arr.splice(i, 1, str + arr[i])
        } else {
          if (key instanceof Array) {
            for (var j = 0; j < key.length; j++) {
              arr[i][key[j]] = str + arr[i][key[j]]
            }
          }
          if (typeof key == 'string') arr[i][key] = str + arr[i][key]
        }
      }
      return arr
    }
    if (typeof arr == 'string') {
      return str + arr;
    }
  }
  fn.initMainData = function (obj, arr, brr) {
    for (var i = 1; i < arr.length; i++) {
      if (obj.arr === undefined || obj.arr === null) {
        obj.arr[i] = brr[i]
      }
    }
    return obj
  }
  fn.initStyle = function (obj, key, keys) {
    if (!obj[key]) return;
    if (obj[key] instanceof Object) {
      for (var i = 0; i < keys.length; i++) {
        if (obj[key][keys[i]]) {
          obj[keys[i]] = obj[key][keys[i]]
        }
      }
    }
  }
  fn.exchangeKey = function (obj, oldkey, newkey, d) {
    obj[newkey] = obj[oldkey]
    if (d) {
      delete obj[oldkey];
    }
  }
  fn.exchangeObjectKey = function (obj, oldkey, newkey, d) {
    if (!(oldkey instanceof Array)) {
      oldkey = [oldkey],
        newkey = [newkey]
    }
    for (var i = 0; i < oldkey.length; i++) {
      fn.exchangeKey(obj, oldkey[i], newkey[i], d)
    }

  }
  fn.exchangeArrayObjectKey = function (arr, oldkey, newkey, d) {
    for (var i = 0; i < arr.length; i++) {
      fn.exchangeObjectKey(arr[i], oldkey, newkey, d)
    }
  }


  return fn
})();
