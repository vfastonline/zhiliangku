<template>
  <div class="project-header " :style="outerStyle">
    <login></login>
    <div class="ph-container  inmiddle clearfix ">
      <!-- <div v-if="!(['videoHeader','liveHeader'].indexOf(type)+1)" @click="inputActive" @keyup.enter="search" class="ph-search inmiddle fontcenter">
        <input @blur="inputNoActive" type="text" id="search-input" v-model="searchValue" class="search-input" :class="inputClass"
          ref="searchInput" placeholder="课程搜索">
        <img class="phs-magnifier  pointer " :class="iconClass" src="../../assets/img/icons/Search-magnifier.svg" alt="">
      </div> -->
        <!-- <div class="inmiddle  input-mask">
          <div class="input-mask-inner ">
            <img class="phs-magnifier search-active pointer " src="../../assets/img/icons/Search-magnifier.svg" alt="">
            <span class="font18pl7c7e8c">课程搜索</span>
          </div>
        </div> -->
      
      <div class="main">
        <div class="inner">
          <div v-if="['videoHeader','liveHeader'].indexOf(type)+1" class="ph-content white">
            <span class="font16prffffff bigCatergory">{{videoTitle.section_desc}}</span>
            >
            <span>{{videoTitle.name}}</span>
          </div>
          <div v-if="!type" class="nav_tags ">
            <span class="ph-tag pointer">
              <a href="/tracks/course/list/"> 课程</a>
            </span>
            <span class="ph-tag pointer">
              <a href="/tracks/path/list/">
                <el-badge value="free!"  class="project-header-free">
                  <span> 高薪就业班 </span>
                </el-badge>
              </a>
            </span>
            <span class="ph-tag pointer"><a href="/community/faq/list/"> 社区</a></span>
            <span class="ph-tag last pointer">线下课程</span>
          </div>
        </div>
      </div>
      <div class="left">
        <img v-if="!type" class='ph-logo pointer' @click="goindex()" src='../../assets/img/icons/Logo.png' alt="">
        <img v-if="['videoHeader','liveHeader'].indexOf(type)+1" @click="showVideoList()" 
        class='ph-expend-button pointer' src='../../assets/img/icons/视频播放+习题图标/视频播放_汉堡按钮.svg'
          alt="">
      </div>
      <div class="rightbar">
        <!--<el-button @click="changShow()" class="ph-button" type="primary" :style="buttonStyle" round>岗位匹配</el-button>-->
        <span
        v-on:mouseenter="changeUsershow1()" v-on:mouseleave="changeUsershow2()"
         class="user-info  font18pl3a3c50" :class="{'white':['videoHeader','liveHeader'].indexOf(type)+1}" >
          <img v-if="is_login" @click="changeUsershow()" class="user-icon pointer" :src="userinfo.avatar" alt="">
          <span v-if="!is_login" class="pointer" @click="myDispatch('open','loginActive')">登录 |</span>
          <span v-if="!is_login" class="pointer" @click="myDispatch('open','logupActive')">注册</span>
        </span>
        <transition   name='fade'>
          <!--<postbMatch v-if="show" class="floatr"></postbMatch>-->
          <userMune class="" v-on:mouseenter="changeUsershow1()" v-on:mouseleave="changeUsershow2()" v-if="showuser"></userMune>
        </transition>
      </div>
    </div>
  </div>
</template>
<style>
  #search-input {
    height: 46px;
    width: 360px;
    box-sizing: border-box;
    border-radius: 200px;
    background-color: #CFD8DC;
    border: none;
    outline: none;
    padding-left: 23px;
    padding-right: 23px;
    text-align: center;
    color: #7C7E8C;
    font-size: 18px;
    font-family: 'PingFangSC-Light', '微软雅黑';
  }

  #search-input:focus {
    height: 46px;
    width: 360px;
    box-sizing: border-box;
    border-radius: 200px;
    /* background-color:rgba(0, 0, 0, 0); */
    color: black;
    border: none;
  }

  .input-mask {
    height: 46px;
    line-height: 42px;
  }

  .input-mask-inner {
    width: 118px;
    margin-left: 110px;
    overflow: hidden;
    /* transition: all ease 0.2s; */
  }

  .input-mask-inner-active {
    margin-left: 2px;
    width: 24px;
  }

</style>

<script>
  import Bus from '../../assets/js/bus'
  import Login from '../../components/login/login.vue'
  // import postMatch from '../../components/home/postMatch'
  import userMune from './userIconMune.vue'
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
      'login': Login,
      // 'postMatch': postMatch,
      'userMune': userMune
    },
    props: {
      type: String,
    },
    watch: {
      is_login: function (a, b) {
        // console.log(a)
        // console.log(b)
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
          window.location.href = '/tracks/course/list/?searchWord=' + encodeURI(this.searchValue) ;
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
        if(!this.is_login){return}
        if(this.setTimer){
        clearTimeout(this.setTimer)
        }
        this.showuser = true;
      },
      changeUsershow2() {
       this.setTimer= setTimeout(()=>{
          this.showuser = false;
        },2000)
      },
      showVideoList() {
        // console.log(this)
        this.$parent.$emit('showVideoList')
      },
      goindex() {
        window.location.href = '/'
      },
      myDispatch(eventName, key) {
        var arr = this.$children;
        for (let i = 0; i < arr.length; i++) {
          arr[i].$emit(eventName, key)
        }
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
      if (['videoHeader','liveHeader'].indexOf(this.type)+1) {
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
      if(this.$fn.funcUrl('searchWord')){
       this.searchValue= this.$fn.funcUrl('searchWord')
       this.inputActive()
       this.$refs.searchInput.blur()
      }
    }
  };

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang='scss'>
  .left {
    // background: red;
    width: 132px;
    float: left;
    margin-left: -100%;
    height: 100%;
    /*position: relative;*/
    /*left:-100px;*/
  }

  .white {
    color: white;
  }

  .fade-enter-active,
  .fade-leave-active {
    transition: all 0.25s ease;
  }

  .fade-enter,
  .fade-leave-active {
    opacity: 0;
  }

  .main {
    // background: blue;
    width: 100%;
    float: left;
    height: 100%;
  }

  .rightbar {
    // background: red;
    width: 235px;
    padding-right:50px;
    float: left;
    margin-left: -285px;
    height: 100%;
    /*position:relative;*/
    /*right:-200px;*/
  } //新增inner元素
  .inner {
    margin-left: 132px;
    margin-right: 285px;
  }

  .ph-content {
    margin-left: -42px;
  }
  .nav_tags{
    margin-left: 150px;
  }
  .project-header-free {
    sup {
      top: 20px !important;
    }
  }

  .project-header {
    // z-index: 100;
    width: 100%;
    height: 70px; // background: brown;
    position: relative; // background: #FFFFFF;
    // border-bottom: 1px solid #cccccc;
    box-shadow: 0 3px 2px rgba(0, 0, 0, 0.1);
    .ph-container {
      line-height: 70px;
    }
    .bigCatergory{
      opacity: 0.75;
    }
    .ph-content {
      height: 70px;
      line-height: 70px; // background: skyblue;
    }
    .ph-logo {
      margin-left: 50px;
      width: 132px;
      height: 48px;
      vertical-align: middle;
    }
    .ph-expend-button {
      position: relative;
      left: 40px;
      vertical-align: middle;
    }
    .ph-tag {
      opacity: 0.8;
      font-family: 'PingFangSC-Light', "Microsoft YaHei", "宋体";
      font-size: 18px;
      color: #3a3c50;
      margin-right: 35px;
      vertical-align: text-bottom;
    }
    .project-tip {
      transition: all 0.5s ease;
      background: #66bb6a;
      padding: 0 4px;
      border-radius: 100px;
    }
    .ph-search {
      width: 380px;
      vertical-align: text-bottom;
    }
    .phs-magnifier {
      vertical-align: middle;
      width: 24px;
      height: 24px;
      position: absolute;
      left: 118px;
      top: 23px; // transition: all ease 0.2s;
    }
    .search-active {
      left: 20px;
    }
    .ph-button {
      vertical-align: middle;
    }
    .user-info {
      float: right;
    }
    .user-icon {
      height: 48px;
      width: 48px;
      vertical-align: middle;
      border-radius: 24px;
    }
    .ph-tag .el-badge {
      vertical-align: unset;
    }
    .project-header {

      .el-dialog__wrapper {
        position: fixed;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        overflow: auto;
        margin: 0;
        background: rgba(0, 0, 0, .5);
        overflow: hidden;
      }
      .el-dialog {
        position: relative;
        margin: 0 auto 50px;
        background: rgba(0, 0, 0, .5);
        border-radius: 2px;
        -webkit-box-shadow: 0 1px 3px rgba(0, 0, 0, .3);
        box-shadow: 0 1px 3px rgba(0, 0, 0, .3);
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
        width: 412px;
        padding: 16px;
      }
      .el-dialog__body {
        background: #ffffff;
        padding: 24px 40px;
        color: #5a5e66;
        line-height: 24px;
        font-size: 14px
      }
      .el-dialog__header {
        padding: 0;
      }
      .el-input__inner {
        border-radius: 0px;
      }
    }
  }

</style>
