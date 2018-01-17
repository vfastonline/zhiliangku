<template>
  <div class="cio-company rise pointer marginbottom24">
    <div class="cio-top">
      <div class="cio-left-logo"><img src="../../assets/img/user-icon.jpg"></div>
      <div class="cio-right-content">
        <p class="font14pl5a646e">{{mainData.info}}</p>
      </div>
    </div>
    <div class="cio-bottom">
      <div class="cio-company-name font16pl3a3c50" >{{mainData.company}}</div>
      <div class="cio-company-people font14pr3a3c50">人员规模：{{mainData.scale}}人</div>
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
  },
  props:{
    mainData:Object
  }
}
</script>


