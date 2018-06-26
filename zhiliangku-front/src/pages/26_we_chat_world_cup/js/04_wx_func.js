var wx = window.wx
export default {
  ShareTimeline: function (url, shear_url, imgurl) {
    wx.onMenuShareTimeline({
      title: '积分竞猜赢10万大礼', // 分享标题
      link: url + shear_url, // 分享链接，该链接域名必须与当前企业的可信域名一致
      imgUrl: url + imgurl, // 分享图标
      success: function () {},
      cancel: function () {
        // 用户取消分享后执行的回调函数
      }
    })
  },
  ShareAppMessage: function (url, shear_url, imgurl) {
    wx.onMenuShareAppMessage({
      title: '积分竞猜赢10万大礼', // 分享标题
      desc: '荣新大数据带你看透世界杯', // 分享描述
      link: url + shear_url, // 分享链接，该链接域名必须与当前企业的可信域名一致
      imgUrl: url + imgurl, // 分享图标
      type: 'link', // 分享类型,music、video或link，不填默认为link
      dataUrl: '', // 如果type是music或video，则要提供数据链接，默认为空
      success: function () {},
      cancel: function () {
        // 用户取消分享后执行的回调函数
      }
    })
  }
}
