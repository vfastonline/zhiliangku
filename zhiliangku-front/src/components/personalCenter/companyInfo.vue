<template>
  <div class="cio-company rise pointer">
    <div class="cio-top">
      <div class="cio-left-logo"><img src="../../assets/img/user-icon.jpg"></div>
      <div class="cio-right-content">
        <p class="font14pl5a646e">该公司主要依靠在线广告、游戏、互联网和增值业务创收。
        2014年1月15日，奇虎360宣布进军台湾，授权希悦资讯为台湾地区总代理。
        2015年2月4日，内部人士确认，奇虎360公司斥巨资收购国际顶级域名360.com，
        收购价格为1700万美元，约合人民币1.1亿元……</p>
      </div>
    </div>
    <div class="cio-bottom">
      <div class="cio-company-name font16pl3a3c50" >360奇虎科技有限公司</div>
      <div class="cio-company-people font14pr3a3c50">人员规模：7000人</div>
    </div>
  
    
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.cio-company{
    width:824px;
    height:140px;
    padding-top:22px;
    box-sizing:border-box;
    background:white;
}
.cio-top, .cio-bottom{
   margin:0 20px;
}
.cio-top{
  height:80px;
}
/*左侧公司logo */
.cio-top .cio-left-logo {
    float:left;
}
.cio-top .cio-left-logo img{
    width:155px;
    height:56px;
}
/*右侧公司简介 */
.cio-top .cio-right-content{
  width:581px;
  height:80px;
  float:right;
}

/*公司名字和人数 */
.cio-bottom .cio-company-name{
  float:left;
}
.cio-bottom .cio-company-people{
  float:right;
}
</style>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>


