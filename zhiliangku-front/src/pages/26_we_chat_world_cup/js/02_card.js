//修改的不是很如意啊 希望对模块化有更多的了解。
module.exports = {
  swiper: function () {
    let Swiper = window.Swiper
    var swiper = new Swiper('.swiper-container', {
      direction: 'vertical',
      passiveListeners: false

    })
    return swiper
  }
}
