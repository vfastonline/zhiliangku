  //这段代码主要是配置微信一些功能
  var $ = window.$
  var wx = window.wx
  var url = 'http://www.zhiliangku.com'
  var imgurl = ''
  $.get(url + '/wechat/background/music', function (params) {
    imgurl = JSON.parse(params).data.images
  })
  var get_name = function (name, value, type) {
    var loca = window.location
    var baseUrl = type === undefined ? loca.origin + loca.pathname + '?' : ''
    var query = loca.search.substr(1)
    // 如果没有传参,就返回 search 值 不包含问号
    if (name === undefined) {
      return query
    }
    // 如果没有传值,就返回要查询的参数的值
    if (value === undefined) {
      var val = query.match(new RegExp('(^|&)' + name + '=([^&]*)(&|$)'))
      return val != null ? decodeURI(val[2]) : null
    }
    var url
    if (query === '') {
      // 如果没有 search 值,则返回追加了参数的 url
      url = baseUrl + name + "=" + value;
      // 现在改为，如果没有search值则加入
      url = name + '=' + value
      window.location.search = '?' + url
    } else {
      // 如果没有 search 值,则在其中修改对应的值,并且去重,最后返回 url
      var obj = {}
      var arr = query.split('&')
      for (var i = 0; i < arr.length; i++) {
        arr[i] = arr[i].split('=')
        obj[arr[i][0]] = arr[i][1]
      }
      obj[name] = value
      url = baseUrl + window.JSON.stringify(obj).replace(/[\"\{\}]/g, "").replace(/\:/g, "=").replace(/\,/g, "&");
      window.location.search =
        '?' +
        window.JSON.stringify(obj)
        .replace(/[\"\{\}]/g, '')
        .replace(/\:/g, '=')
        .replace(/\,/g, '&')
    }
    return url;
  }

  var add_num = function () {
    var name = get_name('name') || ''
    $.get(url + '/wechat/share?name=' + name)
  }
  $.get(url + '/wechat/get/signature?urls=' + encodeURIComponent(window.location.href.split('#')[0]), function (data) {
    var content = JSON.parse(data).data
    var config = {
      debug: false, // 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。
      appId: content.appId, // 必填，企业号的唯一标识，此处填写企业号corpid
      timestamp: content.timestamp, // 必填，生成签名的时间戳
      nonceStr: content.nonceStr, // 必填，生成签名的随机串
      signature: content.signature, // 必填，签名，见附录1
      jsApiList: ['onMenuShareAppMessage', 'onMenuShareTimeline'] // 必填，需要使用的JS接口列表，所有JS接口列表见附录2
    }
    // console.table(config)
    wx.config(config);
    wx.ready(function (res) {
      // alert('ready')
      wx.checkJsApi({
        jsApiList: ['getNetworkType', 'previewImage', 'onMenuShareTimeline', 'onMenuShareAppMessage'],
        success: function (res) {
          // alert(JSON.stringify(res));
        }
      });
      wx.onMenuShareTimeline({
        title: '请为我的努力加分打call', // 分享标题
        link: url + '/wechat/promotion', // 分享链接，该链接域名必须与当前企业的可信域名一致
        imgUrl: url + imgurl, // 分享图标
        success: function () {
          add_num()
        },
        cancel: function () {
          // 用户取消分享后执行的回调函数
        }
      });
      wx.onMenuShareAppMessage({
        title: '请为我的努力加分打call', // 分享标题
        desc: '精彩的未来，我将用勤学不辍的现在去迎接，同学！一起加油！', // 分享描述
        link: url + '/wechat/promotion', // 分享链接，该链接域名必须与当前企业的可信域名一致
        imgUrl: url + imgurl, // 分享图标
        type: 'link', // 分享类型,music、video或link，不填默认为link
        dataUrl: '', // 如果type是music或video，则要提供数据链接，默认为空
        success: function () {
          add_num()
        },
        cancel: function () {
          // 用户取消分享后执行的回调函数
        }
      });
    })
    wx.error(function (res) {
      // alert('错误')
    })
  })
