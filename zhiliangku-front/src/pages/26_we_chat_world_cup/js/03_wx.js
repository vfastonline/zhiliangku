// 改成一个函数
var wx = window.wx
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
      title: '积分竞猜赢10万大礼', // 分享标题
      link: 'https: //open.weixin.qq.com/connect/oauth2/authorize?appid=wx96fdf187f5c8f9f2&redirect_uri=http%3a%2f%2fwww.zhiliangku.com%2fcustomuser%2fweixin%2fwebpage%2flogin&response_type=code&scope=snsapi_userinfo&state=aHR0cDovL3d3dy56aGlsaWFuZ2t1LmNvbS93b3JsZGN1cC90b3BpYw==&#wechat_redirect', // 分享链接，该链接域名必须与当前企业的可信域名一致
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
      desc: '荣新大数据带你看透世界杯', // 分享描述
      link: 'https: //open.weixin.qq.com/connect/oauth2/authorize?appid=wx96fdf187f5c8f9f2&redirect_uri=http%3a%2f%2fwww.zhiliangku.com%2fcustomuser%2fweixin%2fwebpage%2flogin&response_type=code&scope=snsapi_userinfo&state=aHR0cDovL3d3dy56aGlsaWFuZ2t1LmNvbS93b3JsZGN1cC90b3BpYw==&#wechat_redirect', // 分享链接，该链接域名必须与当前企业的可信域名一致
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
