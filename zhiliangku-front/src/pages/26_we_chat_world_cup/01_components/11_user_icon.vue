<template>
  <div>
    <img class="user_icon a"
         v-if="icon_url"
         :src="$myConst.httpUrl+icon_url"
         alt="">

  </div>
</template>

<script>
export default {
  data () {
    return {
      user_info: {},
      icon_url: ''
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
    get_icon () {
      this.$get('/customuser/get/avatar').then(res => {
        this.icon_url = res.data.data
        if (res.data.err == 1) {
          this.go_href()
        }
      })
    },
    go_href () {
      window.location.href = "//open.weixin.qq.com/connect/oauth2/authorize?appid=wx96fdf187f5c8f9f2&redirect_uri=http%3a%2f%2fwww.zhiliangku.com%2fcustomuser%2fweixin%2fwebpage%2flogin&response_type=code&scope=snsapi_userinfo&state=aHR0cDovL3d3dy56aGlsaWFuZ2t1LmNvbS93b3JsZGN1cC90b3BpYw==&#wechat_redirect"
    },
  },
  created () {
    this.get_icon()
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
