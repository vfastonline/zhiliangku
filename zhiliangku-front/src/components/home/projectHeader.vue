<template>
  <div class="project-header " :style="outerStyle">
    <login></login>
    <div class="ph-container mainwidth inmiddle clearfix">
      <div class="main">
        <div class="inner">
          <div v-if="type=='videoHeader'" class="ph-content white">
            <span>Linix系统管理</span>><span>修改进程优先级</span>
          </div>
          <div v-if="!type" class="ph-content">
            <span class="ph-tag pointer">
              <a href="/tracks/course/list/"> 课程</a>
            </span>
            <span class="ph-tag pointer">
              <a href="/tracks/video/detail/"> 直播</a>
            </span>
            <span class="ph-tag pointer">
              <a href="/tracks/path/list/">职业路径</a>
            </span>
            <span class="ph-tag pointer">社区</span>
            <span class="ph-tag last pointer">线下课程</span>
            <span class="ph-search">
              <!-- <input type="text"> -->
              <img class="phs-magnifier pointer" src="../../assets/img/icons/Search-magnifier.svg" alt="">
            </span>
          </div>
        </div>
      </div>
      <div class="left">
        <img v-if="!type" class='ph-logo pointer' @click="goindex()" src='../../assets/img/icons/Logo.png' alt="">
        <img v-if="type=='videoHeader'" class='ph-expend-button pointer' src='../../assets/img/icons/视频播放+习题图标/视频播放_汉堡按钮.svg' alt="">
      </div>
      <div class="rightbar">
        <el-button @click="changShow()" class="ph-button" type="primary" :style="buttonStyle" round>岗位匹配</el-button>
        <span class="user-info font18pl3a3c50">
          <img v-if="login" @click="changeUsershow()" class="user-icon pointer" :src="userinfo.avatar" alt="">
          <span v-if="!login" class="pointer" @click="myDispatch('open','loginActive')">登陆 |</span>
          <span v-if="!login" class="pointer" @click="myDispatch('open','logupActive')">注册</span>
        </span>
        <transition name='fade'>
          <postMatch v-if="show" class="floatr"></postMatch>
          <userMune v-if="showuser"></userMune>
        </transition>
      </div>
    </div>
  </div>
</template>
<script>
  import Login from '../../components/login/login.vue'
  import postMatch from '../../components/home/postMatch'
  import userMune from './userIconMune.vue'
  export default {
    name: "projectHeader",
    data() {
      return {
        loginshow: false,
        logupshow: false,
        show: false,
        showuser:false,
        msg: "Welcome to Your Vue.js App",
        buttonStyle: {
          width: "121px",
          height: "42px",
          background: "23B8FF",
          "font-family": "PingFangSC-Light",
          "font-size": "18px",
          'border':'1px solid white'
        },
        videoButtonStyle: {
          width: "121px",
          height: "42px",
          background: 'none',
          "font-family": "PingFangSC-Light",
          "font-size": "18px"
        },
        mainstyle:{},
        showLogin: false,
        outerStyle:{},
        login:'',
        userinfo:{avatar:''},
      };
    },
    components: {
      'login': Login,
      'postMatch': postMatch,
      'userMune':userMune
    },
    props:{
      type:String,
    },
    methods: {
      changShow() {
        this.show = !this.show;
      },
      changeUsershow(){
        this.showuser=!this.showuser;
      },
      goindex() {
        window.location.href = '/'
      },
      myDispatch(eventName, key) {
        var arr = this.$children;
        console.log(111)
        for (let i = 0; i < arr.length; i++) {
          arr[i].$emit(eventName, key)
        }
      },
      getUserInfo(){
        this.userinfo.avatar=this.$myConst.httpUrl+localStorage.avatar;
      },
    },
    created() {
      console.log(this.type)
      if(this.type=='videoHeader'){
        this.buttonStyle=this.videoButtonStyle;
        this.outerStyle={background:'#333742'};
      }
      this.$on('login',function(){
        this.getUserInfo();
        this.login=true;
        if(location.pathname=='/'){return}       
        location.reload();
        console.log(this.userinfo)
      })
      this.$on('logout',function(){
        this.login=false;
        localStorage.clear();
        this.show=false;
        this.showuser=false;
        if(location.pathname=='/'){return}        
        window.location.href="/"
      })
      if(this.$fn.getCookie('token')){
        this.getUserInfo()
        console.log(this.userinfo)
        this.login=true;
      }
      else{
        this.login=false;
      }
    },
    mounted() {
      this.$on('loginClose', function (child) {
        this.showLogin = false;
      })
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
  .white{
    color:white;
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
    width: 285px;
    float: left;
    margin-left: -285px;
    height: 100%;
    /*position:relative;*/
    /*right:-200px;*/
  }

  //新增inner元素
  .inner {
    margin-left: 132px;
    margin-right: 285px;
  }

  .ph-content {
    padding-left: 50px;
  }

  .project-header {
    z-index: 10000;
    width: 100%;
    height: 70px; // background: brown;
    position: relative; // background: #FFFFFF;
    // border-bottom: 1px solid #cccccc;
    box-shadow: 0 3px 2px rgba(0, 0, 0, 0.1);
    .ph-container{
      line-height: 70px;
    }
    .ph-content {
      height: 70px;
      line-height: 70px; // background: skyblue;
    }
    .ph-logo {
      width: 132px;
      height: 48px;
      vertical-align: middle;
    }
    .ph-expend-button{
      vertical-align: middle;
    }
    .ph-tag {
      opacity: 0.8;
      font-family: PingFangSC-Light "微软雅黑" "宋体";
      font-size: 18px;
      color: #3a3c50;
      margin-right: 35px;
      vertical-align: text-bottom;
    }
    .ph-search {
      margin-right: 5.556%;
      vertical-align: text-bottom;
    }
    .phs-magnifier {
      vertical-align: middle;
      width: 24px;
      height: 24px;
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
  }

</style>
