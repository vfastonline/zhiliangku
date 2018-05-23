<template>
  <header class="mw project_header hc">
    <div class="fl">
      <a href="/"><img class="logo dib vm" src="./img/智量酷-logo-slogan.png" alt=""></a>
      <span class="dib nav_tag"><a href="/tracks/projects/list/"><span
        class="font1_22_3"> 项目</span> </a></span>
      <!--<span class="dib nav_tag"><a href="#"> <span class="font1_22_3"> 考核</span> </a></span>-->
      <span class="dib nav_tag"><a href="#"> <span class="font1_22_3"> 就业</span> </a></span>
      <span class="dib"><a href="/community/faq/list/"> <span class="font1_22_3"> 社区</span> </a></span>
    </div>
    <div v-if="!is_login" class="fr">
      <span @click="myDispatch('specify_display',{show_key:'log_in',title_key:'登录'})" class="font1_20_3 cp">登录</span>
      <span class="font1_20_3"> / </span>
      <span @click="myDispatch('specify_display',{show_key:'log_up',title_key:'用户注册'})" class="font1_20_3 cp">注册</span>
    </div>
    <div v-else class="fr aaa">
      <span class="dib r notice_icon_container">
       <img class="vm notice_icon" src="./img/notice_icon.png" alt="">
        <i class="red_point a"></i>
      </span>
      <img class="user_icon vm" :src="userinfo.avatar" alt="">
    </div>
    <LoginNew @success="is_login=true"></LoginNew>
  </header>
</template>

<script>
  import Bus from '../../assets/js/02_bus'
  import LoginNew from '../02_login/02_login_module'
  import userMune from './04_user_menu'
  let Base64 = require('js-base64').Base64;
  export default {
    name: "projectHeader",
    data() {
      return {
        loginshow: false,
        logupshow: false,
        show: false,
        showuser: false,
        msg: "Welcome to Your Vue.js App",
        buttonStyle: {
          width: "121px",
          height: "42px",
          background: "23B8FF",
          "font-family": "PingFangSC-Light",
          "font-size": "18px",
          'border': '1px solid white'
        },
        videoButtonStyle: {
          width: "121px",
          height: "42px",
          background: 'none',
          "font-family": "PingFangSC-Light",
          "font-size": "18px"
        },
        mainstyle: {},
        showLogin: false,
        outerStyle: {},
        is_login: false,
        userinfo: {
          avatar: ''
        },
        videoTitle: {},
        inputClass: [],
        iconClass: [],
        searchValue: ''
      };
    },
    components: {
      // 'postMatch': postMatch,
      'userMune': userMune,
      'LoginNew':LoginNew
    },
    props: {
      type: String,
    },
    watch: {
      is_login: function (a, b) {

      }
    },
    methods: {
      inputActive() {
        this.inputClass = ['input-mask-inner-active'];
        this.iconClass = ['search-active'];
        var inputDom = this.$refs.searchInput;
        // inputDom.placeholder = '';
        inputDom.style.paddingLeft = '43px';
        inputDom.style.textAlign = 'left';
        inputDom.style.color = 'black';
        inputDom.focus();
      },
      inputNoActive() {
        var inputDom = this.$refs.searchInput;
        if (!this.searchValue.trim()) {
          this.inputClass = [];
          this.iconClass = [];
          // inputDom.value = '';
          inputDom.placeholder = '搜索课程';
          inputDom.style.paddingLeft = '23px'
          inputDom.style.textAlign = 'center';
        }
      },
      search() {
        window.location.href = '/tracks/course/list/?searchWord=' + encodeURI(this.searchValue);
      },
      jj() {
        this.is_login = !this.is_login;
      },
      changShow() {
        this.show = !this.show;
      },
      changeUsershow() {
        this.showuser = !this.showuser;
      },
      changeUsershow1() {
        if (!this.is_login) {
          return
        }
        if (this.setTimer) {
          clearTimeout(this.setTimer)
        }
        this.showuser = true;
      },
      changeUsershow2() {
        this.setTimer = setTimeout(() => {
          this.showuser = false;
        }, 2000)
      },
      showVideoList() {
        // console.log(this)
        this.$parent.$emit('showVideoList')
      },
      goindex() {
        window.location.href = '/'
      },
      myDispatch(eventName, key) {
        Bus.$emit(eventName,key)
      },
      getUserInfo() {
        this.userinfo.avatar = this.$myConst.httpUrl + localStorage.avatar;
      },
      loginfun() {
        this.getUserInfo();
        // 决定用户信息模块的显示与隐藏
        this.is_login = true;
        // 请问这里如何做呢？
        // 现在是不管用户在什么模块登录都会刷新。
        // 不等于首页的页面均需要重载
        if (location.pathname != '/') {
          //这里的逻辑应该是删除掉user_info的字段
          // debugger
          if (this.$fn.funcUrl('next') || this.$fn.funcUrl('user_info')) {
            window.location.href = this.$fn.funcUrlDelArr(['user_info', 'next'])
          }
        }
        // console.log(this.userinfo)
      },
      logoutFunc() {
        this.is_login = false;
        localStorage.clear();
        this.show = false;
        this.showuser = false;
        if (location.pathname == '/') {
          return
        }
        window.location.href = window.location.href;
        window.location.href = "/"
      }
    },
    created() {
      // window.location.search='?'+Base64.encode('uid=46&nickname=猛熊爱吃蜜&role=0&avatar=/media/custom_user_avatar/46/20171225094221_weixin.jpg&position=');
      // window.location.search='?user_info=P3VpZD00NiZuaWNrbmFtZT3njJvnhorniLHlkIPonJwmcm9sZT3lrabnlJ8mYXZhdGFyPS9tZWRpYS9jdXN0b21fdXNlcl9hdmF0YXIvNDYvMjAxNzEyMjUwOTQyMjFfd2VpeGluLmpwZyZwb3NpdGlvbj0='
      //获取包含用户信息的base64加密字符串
      var userstr = this.$fn.getSearchKey('user_info');
      // 解密
      var tstr = Base64.decode(userstr);
      // 分割
      var arr = tstr.split('&');
      var brr = {};
      for (var i = 0; i < arr.length; i++) {
        brr[arr[i].split('=')[0]] = arr[i].split('=')[1];
      }
      if (brr['uid']) {
        for (var k in brr) {
          localStorage[k] = brr[k]
        }
        this.loginfun();
        // console.log(this.is_login)
      }
      // console.log(document.cookie)
      if (['videoHeader', 'liveHeader'].indexOf(this.type) + 1) {
        this.buttonStyle = this.videoButtonStyle;
        this.outerStyle = {
          background: '#333742'
        };
      }
      this.$on('login', this.loginfun)
      this.$on('logout', this.logoutFunc)
      //如果先进行这一步判断，然后再进行取user_info的字段就可以完成后退功能
      if (this.$fn.getCookie('token')) {
        this.getUserInfo()
        // console.log(this.userinfo)
        this.is_login = true;
      } else {
        this.is_login = false;
        localStorage.clear();
      }
      Bus.$on('titleBreadCrumb', res => {
        this.videoTitle = res;
      })
      Bus.$on('logout', this.logoutFunc)
      Bus.$on('refreshAvatar', this.getUserInfo)

    },
    mounted() {
      this.$on('loginClose', function (child) {
        this.showLogin = false;
      })
      if (this.$fn.funcUrl('searchWord')) {
        this.searchValue = this.$fn.funcUrl('searchWord')
        this.inputActive()
        this.$refs.searchInput.blur()
      }
    }
  };
</script>

<style scoped lang='scss'>
  $margin: 46px;
  .project_header {
    height: 90px;
    line-height: 90px;
  }

  .logo {
    margin-right: $margin;
  }

  .nav_tag {
    margin-right: $margin;
  }

  .user_icon {
    border-radius: 50%;
    margin-left: 24px;
    height: 80px;
    width: 80px;
  }

  .red_point {
    right: -3px;
    top: -3px;
    background-color: red;
    height: 10px;
    width: 10px;
    border-radius: 10px;
  }

  .notice_icon_container {
    line-height: normal;
  }
</style>
