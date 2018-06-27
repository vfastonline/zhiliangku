<template>
  <div class="main_block">
    <div class="swiper-container">
      <div class="swiper-wrapper">
        <slide_01 :user_mark="user_mark"
                  @show_rules="show_rules"
                  class="swiper-slide"></slide_01>
        <slide_03 v-show="show_03"
                  class="swiper-slide"></slide_03>
        <slide_02 @show_info="show_info_page"
                  :user_mark="user_mark"
                  class="swiper-slide"></slide_02>
        <slide_04 v-show="show_04"
                  v-for="item in bgc"
                  :key="item"
                  :main_data="item"
                  class="swiper-slide show_slide_bet_info"></slide_04>
        <!-- <result></result> -->
      </div>
    </div>
  </div>
</template>
<style>
</style>
<style scoped lang='scss'>
.main_block {
  height: 100%;
}
</style>
<script>

import slide_01 from './01_components/01_slid'
import slide_02 from './01_components/03_slid'
import slide_03 from './01_components/07_slid'
import slide_04 from './01_components/10_slid_04'
import result from './01_components/09_result_0'
import Bus from '../../assets/js/02_bus'
import { Base64 } from 'js-base64'
export default {
  data () {
    return {
      my_swiper: "",
      shear_icon: '',
      url: "http://www.zhiliangku.com",
      user_mark: '',
      show_03: false,
      show_04: false,
      bgc: []
    }
  },
  methods: {
    newSwiper () {
      let Swiper = window.Swiper
      var that = this
      this.my_swiper = new Swiper('.swiper-container', {
        direction: 'vertical',
        preloadImages: true,
        observer: true,
        observeParents: true,
        on: {
          SlideChangeEnd: function (params) {
            that.my_swiper.update();
            that.mySwiper.reLoop();
          }
        }
      })
    },
    get_bgc () {
      this.$get('/worldcup/get/analysis/info').then(res => {
        this.bgc = res.data.data
        this.$nextTick().then(res => {
          this.newSwiper()
        })
      })
    },
    show_info_page () {
      this.show_04 = true
      this.$nextTick().then(res => {
        this.newSwiper()
        let num = 2
        if (this.show_03) { num = 3 }
        this.my_swiper.slideTo(num, 300)
      })
    },
    show_rules () {
      this.show_03 = true
      this.$nextTick().then(res => {
        this.newSwiper()
        this.my_swiper.slideTo(1, 300)
      })
    },
    get_user_mark () {
      this.$get('/worldcup/get/user/integral').then(res => {
        this.user_mark = { value: res.data.data }
      })
    },
    get_icon () {
      this.$get('/wechat/background/music').then(res => {
        this.shear_icon = res.data.data.images
      })
    },
    add_num () {
      var name = this.$fn.funcUrl('name') || ''
      this.$get(this.url + '/wechat/share?name=' + name)
      alert(1)
      Bus.$emit('shear_success')
    },
    get_user_info () {
      this.user_info = this.search_turn_obj(Base64.decode(this.$fn.funcUrl('user_info')))
      for (let k in this.user_info) {
        localStorage[k] = this.user_info[k]
      }
    },
    search_turn_obj (se) {
      if (typeof se !== "undefined") {
        se = se.substr(1);
        var arr = se.split("&"),
          obj = {},
          newarr = [];
        arr.forEach((i) => {
          newarr = i.split("=");
          if (typeof obj[newarr[0]] === "undefined") {
            obj[newarr[0]] = newarr[1];
          }
        });
        return obj;
      }
    },
    have_cookie () {
      if (!document.cookie) {
        window.location.href = "//open.weixin.qq.com/connect/oauth2/authorize?appid=wx96fdf187f5c8f9f2&redirect_uri=http%3a%2f%2fwww.zhiliangku.com%2fcustomuser%2fweixin%2fwebpage%2flogin&response_type=code&scope=snsapi_userinfo&state=aHR0cDovL3d3dy56aGlsaWFuZ2t1LmNvbS93b3JsZGN1cC90b3BpYw==&#wechat_redirect"
      }
    }
  },
  created () {
    this.get_user_mark()
    this.get_user_info()
    this.get_bgc()
    Bus.$on('clear_stake', this.get_user_mark())
    this.have_cookie()
  },
  mounted () {
    this.get_icon()
  },
  components: {
    slide_01: slide_01,
    slide_02: slide_02,
    slide_03: slide_03,
    slide_04: slide_04,
    result: result
    // 	https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx96fdf187f5c8f9f2&redirect_uri=http%3a%2f%2fwww.zhiliangku.com%2fcustomuser%2fweixin%2fwebpage%2flogin&response_type=code&scope=snsapi_userinfo&state=aHR0cDovL3d3dy56aGlsaWFuZ2t1LmNvbS93b3JsZGN1cC90b3BpYw==&#wechat_redirect
    //  uid=112&nickname=猛熊爱吃蜜&role=学生&avatar=/media/custom_user_avatar/112/20180625164857_weixin.jpg&position=
  }
}
</script>
