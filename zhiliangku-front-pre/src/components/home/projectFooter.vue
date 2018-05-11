<template>
  <div class="projectFooter ofhid">
      <div class="pf-content inmiddle">
      <div class="fc-tags flexjustify">
          <span class="pfct-tag font18pl2C343B pointer" href="">关于我们</span>
          <span class="pfct-tag font18pl2C343B pointer" href="">联系我们</span>
          <span class="pfct-tag font18pl2C343B pointer" href="">友情链接</span>
          <span class="pfct-tag font18pl2C343B pointer" href="">意见反馈</span>
      </div>
      <address class="fontcenter font14pl2C343B">copyright 2017 北京智量酷教育科技有限公司 京ICP备09076312号</address>
      </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.projectFooter{
    height: 140px;
    width: 100%;
    position: relative;
}
.pf-content{
    width: 604px;
}
.fc-tags{
    margin-top:32px;
}
address{
    margin-top:28px;
    margin-bottom:34px;
}
</style>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      msg: "Welcome to Your Vue.js App"
    };
  }
};
</script>


