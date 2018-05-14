<template>
  <header class="mw project_header hc">
    <div class="fl">
      <img class="logo dib vm" src="./img/智量酷-logo-slogan.png" alt="">
      <span class="dib nav_tag"><a href="/tracks/projects/list/index.html"> <span class="font1_22_3"> 项目</span> </a></span>
      <!--<span class="dib nav_tag"><a href="#"> <span class="font1_22_3"> 考核</span> </a></span>-->
      <span class="dib nav_tag"><a href="#"> <span class="font1_22_3"> 就业</span> </a></span>
      <span class="dib"><a href="#"> <span class="font1_22_3"> 社区</span> </a></span>
    </div>
    <!--<div class="fr">-->
    <!--<span class="font1_20_3">登录</span>-->
    <!--<span class="font1_20_3"> / </span>-->
    <!--<span class="font1_20_3">注册</span>-->
    <!--</div>-->
    <div class="fr aaa">
      <span class="dib r notice_icon_container">
       <img class="vm notice_icon" src="./img/notice_icon.png" alt="">
        <i class="red_point a"></i>
      </span>
      <img class="user_icon vm" src="./img/user_icon.png" alt="">
    </div>
  </header>
</template>

<script>
  export default {
    data() {
      return {}
    },
    methods: {},
    components: {}
  }
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
