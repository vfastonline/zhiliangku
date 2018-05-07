<template>
  <header class="mw project_header hc">
    <div class="fl">
    <img class="logo dib vm" src="./imgs/智量酷-logo-slogan.png" alt="">
    <span class="dib nav_tag"><a  href="#"> <span> 项目</span> </a></span>
    <span class="dib nav_tag"><a  href="#"> <span> 考核</span> </a></span>
    <span class="dib nav_tag"><a  href="#"> <span> 就业</span> </a></span>
    <span class="dib"><a  href="#"> <span> 社区</span> </a></span>
    </div>
    <div class="fr">
      <span>登录</span>
      <span> / </span>
      <span>注册</span>
    </div>
  </header>
</template>

<script>
export default {
  data () {
    return {
    }
  },
  methods: {
  },
  components: {
  }
}
</script>

<style scoped lang='scss'>
@import '../../assets/style/baseScss';
$mright:46px;
.project_header{
  height: 140px;
  line-height: 140px;
}
.logo{
  margin-right: $mright;
}
.nav_tag{
  margin-right: $mright;
}
</style>
