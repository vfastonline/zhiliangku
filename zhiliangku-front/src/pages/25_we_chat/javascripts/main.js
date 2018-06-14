//修改的不是很如意啊
//希望对模块化有更多的了解。
module.exports = {
  init: function () {
    let $ = window.$
    let bgMusic = $('audio').get(0);
    let $btnMusic = $('.btn-music');
    // background music control
    $btnMusic.click(function () {
      if (bgMusic.paused) {
        bgMusic.play();
        $(this).removeClass('paused');
      } else {
        bgMusic.pause();
        $(this).addClass('paused');
      }
    })
    //音乐的播放时机和触发
    let play_muisc = function () {
      if (!$btnMusic.hasClass('paused') && bgMusic.paused) {
        bgMusic.play();
      }
    }
    document.addEventListener('touchstart', play_muisc)
    setTimeout(play_muisc, 500)
    $('.loading-overlay').slideUp();
  },
  swiper: function () {
    let $ = window.$
    let Swiper = window.Swiper
    let bgMusic = $('audio').get(0);
    let $btnMusic = $('.btn-music');
    let $upArrow = $('.up-arrow');
    let animationControl = require('./animation-control.js')
    var swiper = new Swiper('.swiper-container', {
      mousewheelControl: true,
      effect: 'coverflow', // slide, fade, coverflow or flip
      speed: 400,
      direction: 'vertical',
      fade: {
        crossFade: false
      },
      coverflow: {
        rotate: 100,
        stretch: 0,
        depth: 300,
        modifier: 1,
        slideShadows: false // do disable shadows for better performance
      },
      flip: {
        limitRotation: true,
        slideShadows: false // do disable shadows for better performance
      },
      onInit: function (swiper) {
        animationControl.initAnimationItems(); // get items ready for animations
        animationControl.playAnimation(swiper); // play animations of the first slide
      },
      onTransitionStart: function (swiper) { // on the last slide, hide .btn-swipe
        if (swiper.activeIndex === swiper.slides.length - 1) {
          $upArrow.hide();
        } else {
          $upArrow.show();
        }
      },
      onTransitionEnd: function (swiper) { // play animations of the current slide
        animationControl.playAnimation(swiper);
      },
      onTouchStart: function () { // mobile devices don't allow audios to play automatically, it has to be triggered by a user event(click / touch).
        if (!$btnMusic.hasClass('paused') && bgMusic.paused) {
          bgMusic.play();
        }
      }
    })
    return swiper
  }
}
