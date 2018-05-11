<template>
  <div class="cio-company rise pointer marginbottom24">
    <div class="cio-top">
      <div class="cio-left-logo fontcenter"><img v-lazy="mainData.logo"></div>
      <div class="cio-right-content ofhid ">
        <p class="font16pl5a646e">{{mainData.info}}</p>
      </div>
    </div>
    <div class="cio-bottom">
      <div class="cio-company-name fontcenter font16pl3a3c50" >{{mainData.company}}</div>
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
  margin-bottom:8px;
}
/*左侧公司logo */
.cio-top .cio-left-logo {
    float:left;
}
.cio-left-logo{
  width: 155px;
}
.cio-top .cio-left-logo img{
    max-width:155px;
    max-height:80px;
    vertical-align: bottom;
    margin: auto
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
.cio-company-name{
  width: 155px;
}
.cio-bottom .cio-company-people{
  float:right;
}
</style>
<script>
import VueLazyLoad from 'vue-lazyload'
Vue.use(VueLazyLoad,{
})
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


