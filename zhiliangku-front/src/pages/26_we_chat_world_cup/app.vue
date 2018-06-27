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
        this.init_wx()
      })
    },
    init_wx () {
      // 改成一个函数
      var wx = window.wx
      var url = this.url
      var imgurl = this.shear_icon, add_num = this.add_num
      this.$get(url + '/wechat/get/signature?urls=' + encodeURIComponent(window.location.href.split('#')[0]), function (data) {
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
            link: 'https://www.zhiliangku.com/worldcup/topic',
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
            link: 'https://www.zhiliangku.com/worldcup/topic',
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
    },
    add_num () {
      var name = this.$fn.funcUrl('name') || ''
      this.$get(this.url + '/wechat/share?name=' + name)
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
        window.location.href = "//open.weixin.qq.com/connect/oauth2/authorize?appid=wx96fdf187f5c8f9f2&redirect_uri=http%3a%2f%2fwww.zhiliangku.com%2fcustomuser%2fweixin%2fwebpage%2flogin&response_type=code&scope=snsapi_userinfo&state=aHR0cDovL3d3dy56aGlsaWFuZ2t1LmNvbS93b3JsZGN1cC90b3BpYw==&#wechat_redirect"
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
