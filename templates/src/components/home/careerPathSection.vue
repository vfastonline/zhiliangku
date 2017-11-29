<template>
  <div class="cps-container ">
      <img class="spsc-img floatl" src="../../assets/img/careerPath.png" alt="">
      <div class="cpsc-introduce floatr">
          <div class="cpsci-title font24pr2C343B textellipsis">UI视觉设计师</div>
          <div class="cpsci-content font14pr5a646e ofhid">测试文本</div>
          <div class="cpsci-button"><el-button type="small">查看详情</el-button></div>
      </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.cps-container{
    height: 400px;
    width: 1152px;
    box-sizing: border-box;
    padding: 32px;
}
.spsc-img{
    height: 336px;
    width: 512px;
}
.cpsc-introduce{
    width:544px;
    height: 336px;
}
.cpsci-title{
    margin-bottom:12px;
}
.cpsci-content{
    line-height: 30px;
    letter-spacing: 1px;
    height:257px;
}
.cpsci-button{
    height:36px;
}
</style>

<script>
export default {
  name: 'careerPathSection',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  props:{
      imgsrc:String,
      title:String,
      content:String,
      link:String
  }
}
</script>

