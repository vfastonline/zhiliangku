<template>
  <div class="project_container">
    <div class="loading-overlay">
      <img src="./img/loading.svg">
    </div>
    <slide_00 v-if="(!show)&&have_img"
              :image_url="background_images[0]">
    </slide_00>
    <div v-if="show&&have_img"
         class="swiper-container">
      <div class="swiper-wrapper">
        <slide_01 :image_url="background_images[0]"
                  :main_data="main_data"></slide_01>
        <slide_02 :image_url="background_images[1]"
                  :main_data="main_data"></slide_02>
        <slide_03 :image_url="background_images[2]"
                  :main_data="main_data"></slide_03>
        <slide_04 :image_url="background_images[3]"
                  :main_data="main_data"></slide_04>
        <slide_05 :image_url="background_images[4]"
                  :main_data="main_data"></slide_05>
      </div>
    </div>

    <button @touchstart="go_next"
            v-if="show"
            class="up-arrow">
      <i class="icon-angle-double-up r"></i>
      <div class="bottom_text ftc a">
        等待你为我打call
      </div>
    </button>

    <button class="btn-music">
      <i class="icon-note"></i>
    </button>

    <audio loop>
      <source src="./audios/background.mp3"
              type="audio/mpeg">
    </audio>
  </div>
</template>
<style lang="scss" scoped>
.bottom_text {
  font: 300 0.24rem/0.24rem 'MicroSoft YaHei';
  color: #ffffff;
  width: 2.1rem;
  margin-left: 50%;
  transform: translate(-50%);
}
</style>

<script>
import slide_00 from './components/00_slide'
import slide_01 from './components/01_slide'
import slide_02 from './components/02_slide'
import slide_03 from './components/03_slide'
import slide_04 from './components/04_slide'
import slide_05 from './components/05_slide'
import init from './javascripts/main'
export default {
  data () {
    return {
      show: false,
      have_img: false,
      background_images: [],
      main_data: {},
      music_src: ''
    }
  },
  watch: {
    show: function (new_value, old_value) {
      var that = this
      // debugger
      this.$nextTick().then(res => {
        setTimeout(() => {
          that.my_swiper = init.swiper()
          // debugger
        }, 100);
      })
    }
  },
  methods: {
    go_next () {
      this.my_swiper.slideNext()
    },
    get_background_img () {
      this.$get('/wechat/backgrounds').then(res => {
        if (!this.$is_empty(res.data.data)) {
          this.background_images = res.data.data
          this.have_img = true
        }
      })
    },
    get_student_info (name) {
      var that = this
      setTimeout(() => {
        window.axios.all([
          window.axios.get('/wechat/promotion/info?name=' + name),
          window.axios.get('/wechat/backgrounds')
        ]).then(window.axios.spread(function (user_info, imgs) {
          // 上面两个请求都完成后，才执行这个回调方法
          that.background_images = imgs.data.data
          that.have_img = true
          if (!that.$is_empty(user_info.data.data)) {
            that.show = true
            that.main_data = user_info.data.data
          }
        }));
      }, 1);

    },
    verify () {
      let name = this.$fn.funcUrl('name')
      if (name) {
        this.get_student_info(name)
      } else {
        this.get_background_img()
        this.show = false
      }
    },
    get_music () {
      this.$get('/wechat/background/music').then(res => {
        this.music_src = res.data.data.address
      })
    }
  },
  created () {
    window.page = this
    this.get_music()
    this.verify()
  },
  mounted () {
    init.init()
  },
  components: {
    slide_00: slide_00,
    slide_01: slide_01,
    slide_02: slide_02,
    slide_03: slide_03,
    slide_04: slide_04,
    slide_05: slide_05,
  },
}

</script>
<style lang='scss'>
@import './scss/main';
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

.slide-0 {
  background-color: #e88a63;
}

.slide-1 {
  background-color: #e88a63;
}

.slide-2 {
  background-color: #5cc2f1;
}

.slide-3 {
  background-color: #9993c1;
}

.slide-4 {
  background-color: #e88a63;
}

.slide-5 {
  background-color: #5cc2f1;
}

.the_button {
  line-height: 0.28rem;
  font-size: 0.28rem;
  color: #ffffff;
  padding: 0.1rem 0.15rem;
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
  background-color: rgba($color: #000, $alpha: 0.3);
  color: #ffffff;
  font-size: 0.28rem;
  text-align: center;
  top: -0.5rem;
  opacity: 0.1;
}

.notice_actve {
  font-size: 0.28rem;
  top: 0rem;
  opacity: 1;
}
</style>
