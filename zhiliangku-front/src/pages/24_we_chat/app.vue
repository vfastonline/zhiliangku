<template>
  <div class="project_container">
    <div class="loading-overlay">
    <img src="./img/loading.svg">
    </div>

    <div class="swiper-container">
      <div class="swiper-wrapper">
        <div class="swiper-slide slide-1">
        </div>
        <div class="swiper-slide slide-2">
        </div>
        <div class="swiper-slide slide-3">
        </div>
        <div class="swiper-slide slide-4">
        </div>
        <div class="swiper-slide slide-5">
        </div>
        <div class="swiper-slide slide-6">
        </div>
        <div class="swiper-slide slide-7">
          <div class="notice">送你个么么哒~~q^_^p~~</div>
          <div class="the_button">
            <span>为他打call</span>
            <span class="count db a">
                <span class="animated" :class="{'shake':show_num}">{{num}}</span>
              <transition
                enter-active-class="animated fadeInUp">
                <span v-if="show" class="added a">+1</span>
              </transition>
            </span>
          </div>
        </div>
      </div>
    </div>

    <button class="up-arrow">
      <i class="icon-angle-double-up"></i>
    </button>

    <button class="btn-music">
      <i class="icon-note"></i>
    </button>

    <audio loop>
      <source src="./audios/background.mp3" type="audio/mpeg">
    </audio>
  </div>
</template>
<style>
  .slide-1 {
    background-color: #5cc2f1;
    background-image: url('./img/1.jpg');
    background-size: 100% 100%;
  }
  .slide-2 {
    background-color: #5cc2f1;
    background-image: url('./img/2.jpg');
    background-size: 100% 100%;


  }
  .slide-3 {
    background-color: #9993c1;
    background-image: url('./img/3.jpg');
    background-size: 100% 100%;


  }
  .slide-4 {
    background-color: #9993c1;
    background-image: url('./img/4.jpg');
    background-size: 100% 100%;


  }
  .slide-5 {
    background-color: #9993c1;
    background-image: url('./img/5.jpg');
    background-size: 100% 100%;


  }
  .slide-6 {
    background-color: #9993c1;
    background-image: url('./img/6.jpg');
    background-size: 100% 100%;


  }
  .slide-7 {
    background-color: #9993c1;
    background-image: url('./img/7.jpg');
    background-size: 100% 100%;
  }
</style>
<script>

  export default {
    data() {
      return {
        show: false,
        num: 100,
        show_num: false
      }
    },
    components: {},
    created(){
      this.$get('/wechat/thumbsuptotal').then(res=>{
        this.num=res.data.total
      })
    },
    mounted() {
      var $ = window.jQuery
      var changshow = () => {
        this.show = !this.show
        setTimeout(() => {
          this.num++
          this.show = false
          this.show_num = true
        }, 800)
      }
      $(document).ready(function () {
        var a = true
        var button = document.querySelector('.the_button')
        var notice = document.querySelector('.notice')
        button.addEventListener('touchstart', function (e) {
          if (!a) return
          $(e.target).addClass('the_button_active')
        })
        button.addEventListener('touchend', (function (e) {
          if (!a) return
          $(notice).addClass('notice_actve')
          $.get('http://www.zhiliangku.com/wechat/thumbsup', function (e) {
            if (e.err) return
            $(button).removeClass('the_button_active')
            changshow()
            setInterval(function () {
              $(notice).removeClass('notice_actve')
            }, 1300)
            a = false
          })
        }));
      })
    }
  }
</script>
<style lang='scss'>
  @import "./scss/main";
  .count {
    left: 100%;
    top: 0;
    line-height: 0.28rem;
    font-size: 0.28rem;
    padding: 0.1rem;
    white-space: nowrap;
    border-radius: 10rem;
    border: 0.02rem solid red;
    box-sizing: border-box;
    background-color: white;
    color: red;
    margin-left: 0.1rem;
  }

  .added {
    right: 0;
    bottom: 100%;
    margin-bottom: 0.1rem;
    margin-right: 0.1rem;
  }

  .project_container {
    height: 100%;
    width: 100%;
  }

  .slide-1 {
    background-color: #e88a63;
    background-image: url('./img/1.jpg');
  }

  .slide-2 {
    background-color: #5cc2f1;
    background-image: url('./img/2.jpg');

  }

  .slide-3 {
    background-color: #9993c1;
    background-image: url('./img/3.jpg');

  }

  .slide-4 {
    background-color: #9993c1;
    background-image: url('./img/4.jpg');

  }

  .slide-5 {
    background-color: #9993c1;
    background-image: url('./img/5.jpg');

  }

  .slide-6 {
    background-color: #9993c1;
    background-image: url('./img/6.jpg');

  }

  .slide-7 {
    background-color: #9993c1;
    background-image: url('./img/7.jpg');
  }

  .the_button {
    line-height: 0.28rem;
    font-size: 0.28rem;
    color: #ffffff;
    padding: 0.10rem 0.15rem;
    background-color: #9091d3;
    box-shadow: 0px 5px 8px #000;
    border-radius: 0.5rem;
    position: absolute;
    top: 22%;
    left: 50%;
    transform: translate(-50%, 0);
    transition: all 0.05s;
  }

  .the_button_active {
    box-shadow: 0 0 0 #000;
  }

  .notice {
    transition: all ease 0.3s;
    position: absolute;
    width: 100%;
    line-height: 0.4rem;
    background-color: rgba($color: #000, $alpha: .3);
    color: #ffffff;
    font-size: 0.28rem;
    text-align: center;
    top: -0.5rem;
    opacity: .1;
  }

  .notice_actve {
    font-size: 0.28rem;
    top: 0rem;
    opacity: 1;
  }
</style>

