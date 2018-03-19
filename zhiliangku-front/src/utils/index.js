module.exports = (function () {
  var fn = {};
  //切换显隐开关的函数，支持传入数组、index，对象、key，show。该函数还有优化空间。
  // fn.changeShow = function (arr) {
  //   console.log(arr)
  //   var show = arr[1],
  //     index = arr[2];
  //   console.log(this)
  //   if (typeof index != 'undefined') {
  //     if (this.show instanceof Array) {
  //       this.show.splice(index, 1, !this.show[index])
  //       return show
  //     }
  //     if (show instanceof Object) {
  //       this.show.index = !this.show.index;
  //       return show
  //     }
  //   }
  //   this.show = !this.show;
  //   return show
  // }
  fn.go = function (str) {
    window.location.href = 'http://' + window.location.host + str;
  }
  fn.changeShow = function (obj, key) {
    obj[key] = !obj[key]
  }
  fn.addObjString = function (str, obj, key) {
    obj[key] = str + obj[key]
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
              fn.addObjString(str, arr[i], key[j])
              // arr[i][key[j]] = str + arr[i][key[j]]
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
    arr[key] = str + arr[key]
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
    return obj
  }
  fn.exchangeObjectKey = function (obj, oldkey, newkey, d) {
    if (!(oldkey instanceof Array)) {
      oldkey = [oldkey],
        newkey = [newkey]
    }
    for (var i = 0; i < oldkey.length; i++) {
      fn.exchangeKey(obj, oldkey[i], newkey[i], d)
    }
    return obj;
  }
  fn.exchangeArrayObjectKey = function (arr, oldkey, newkey, d) {
    for (var i = 0; i < arr.length; i++) {
      fn.exchangeObjectKey(arr[i], oldkey, newkey, d)
    }
    return arr
  }
  fn.getSearch = function () {
    var str;
    if (window.location.search) {
      str = window.location.search.substr(1);
    }
    if (str) {
      return str
    }
  }
  fn.getSearchKey = function (key) {
      var searchStr = fn.getSearch();
      if (!searchStr) {
        return
      }
      var kvrr = searchStr.split('&');
      for (var i = 0; i < kvrr.length; i++) {
        if (kvrr[i]) {
          var keyvaluearr = kvrr[i].split('=');
          if (keyvaluearr[0] == key) {
            return keyvaluearr[1]
          }
        }
      }
    },
    fn.getCookie = function (key) {
      var arr = document.cookie.split(';');
      for (var i = 0; i < arr.length; i++) {
        var brr = arr[i].split('=');
        if (brr[0] == key || brr[0] == ' ' + key) {
          console.log(key)
          return brr[1]
        }
      }
    }
  fn.getCookies = function (keyarr) {
    var tarr = [];
    keyarr.each(function (i) {
      tarr.push(fn.getCookie(i))
    })
  }
  fn.getTargetVue = function (vuearr, key) {
    for (var i = 0; i < vuearr.length; i++) {
      if (vuearr[i].name == key) {
        return vuearr[i]
      }
    }
  }
  fn.objToSearch = function (obj) {
    var str = '';
    for (var k in obj) {
      str = str + k + '=' + obj[k] + '&';
    }
    return str;
  }
  fn.searchToObj = function (url) {
    var reg_url = /^[^\?]+\?([\w\W]+)$/,
      reg_para = /([^&=]+)=([\w\W]*?)(&|$|#)/g,
      arr_url = reg_url.exec(url),
      ret = {};
    if (arr_url && arr_url[1]) {
      var str_para = arr_url[1],
        result;
      while ((result = reg_para.exec(str_para)) != null) {
        ret[result[1]] = result[2];
      }
    }
    return ret;
  }
  fn.funcUrlDel = function (name) {
    var loca = window.location;
    var baseUrl = loca.origin + loca.pathname + "?";
    var query = loca.search.substr(1);
    if (query.indexOf(name) > -1) {
      var obj = {}
      var arr = query.split("&");
      for (var i = 0; i < arr.length; i++) {
        arr[i] = arr[i].split("=");
        obj[arr[i][0]] = arr[i][1];
      };
      delete obj[name];
      var url = baseUrl + window.JSON.stringify(obj).replace(/[\"\{\}]/g, "").replace(/\:/g, "=").replace(/\,/g, "&");
      return url
    };
  }

  fn.funcUrlDelArr = function (nameArr) {
    var loca = window.location;
    var baseUrl = loca.origin + loca.pathname + "?";
    var query = loca.search.substr(1);
    var obj = {};
    var arr = query.split("&");
    for (var i = 0; i < arr.length; i++) {
      arr[i] = arr[i].split("=");
      obj[arr[i][0]] = arr[i][1];
    };
    for (var j = 0; j < nameArr.length; j++) {
      if (query.indexOf(nameArr[j]) > -1) {
        delete obj[nameArr[j]];
      }
    };
    var url = baseUrl + window.JSON.stringify(obj).replace(/[\"\{\}]/g, "").replace(/\:/g, "=").replace(/\,/g, "&");
    return url
  }

  fn.showNotice = function (t, str, type) {
    t.$notify({
      type: type || 'info',
      message: str,
      offset: 100,
      duration: 3000,
      position: 'bottom-right'
    })
  }
  fn.funcUrl = function (name, value, type) {
    var loca = window.location;
    var baseUrl = type == undefined ? loca.origin + loca.pathname + "?" : "";
    var query = loca.search.substr(1);
    // 如果没有传参,就返回 search 值 不包含问号
    if (name == undefined) {
      return query
    }
    // 如果没有传值,就返回要查询的参数的值
    if (value == undefined) {
      var val = query.match(new RegExp("(^|&)" + name + "=([^&]*)(&|$)"));
      return val != null ? decodeURI(val[2]) : null;
    };
    var url;
    if (query == "") {
      // 如果没有 search 值,则返回追加了参数的 url
      // url = baseUrl + name + "=" + value;
      //现在改为，如果没有search值则加入
      url = name + "=" + value;
      window.location.search = '?' + url;
    } else {
      // 如果没有 search 值,则在其中修改对应的值,并且去重,最后返回 url
      var obj = {};
      var arr = query.split("&");
      for (var i = 0; i < arr.length; i++) {
        arr[i] = arr[i].split("=");
        obj[arr[i][0]] = arr[i][1];
      };
      obj[name] = value;
      // url = baseUrl + window.JSON.stringify(obj).replace(/[\"\{\}]/g, "").replace(/\:/g, "=").replace(/\,/g, "&");
      window.location.search = '?' + window.JSON.stringify(obj).replace(/[\"\{\}]/g, "").replace(/\:/g, "=").replace(/\,/g, "&");
    };
    // return url;
  }
  return fn
})();
