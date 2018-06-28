<template>
  <div>
    <img class="user_icon a"
         v-if="user_info.avatar"
         :src="$myConst.httpUrl+user_info.avatar"
         alt="">
    <span class="score dib ">
      <span class="dib vm">积分：
        <num :main_data="user_mark"></num>
      </span>
    </span>
  </div>
</template>

<script>
import { Base64 } from 'js-base64'

export default {
  data () {
    return {
      user_info: {}
    }
  },
  watch: {
    user_info: {
      handler (n) {
        // debugger
      },
      deep: true
    }
  },
  props: {},
  methods: {
    get_user_info () {
      if (!window.location.search || this.$fn.funcUrl('user_info')) {
        this.go_href()
      }
      this.user_info = this.search_turn_obj(Base64.decode(this.$fn.funcUrl('user_info')))
    },
    go_href () {
      window.location.href = "//open.weixin.qq.com/connect/oauth2/authorize?appid=wx96fdf187f5c8f9f2&redirect_uri=http%3a%2f%2fwww.zhiliangku.com%2fcustomuser%2fweixin%2fwebpage%2flogin&response_type=code&scope=snsapi_userinfo&state=aHR0cDovL3d3dy56aGlsaWFuZ2t1LmNvbS93b3JsZGN1cC90b3BpYw==&#wechat_redirect"
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
  },
  created () {
    this.get_user_info()
  },
  components: {

  }
}
</script>

<style scoped lang="scss">
.user_icon {
  height: 0.8rem;
  width: 0.8rem;
  border-radius: 50%;
  top: 50%;
  left: 0;
  transform: translate(0, -50%);
}
.score {
  height: 0.62rem;
  line-height: 0.62rem;
  padding: 0 0.06rem;
  border-radius: 1rem;
  color: white;
  font-size: 0.22rem;
  padding-left: 1rem;
  padding-right: 0.1rem;
  background: url('../img/10_blue_button.png');
  background-size: 100% 100%;
}
</style>
