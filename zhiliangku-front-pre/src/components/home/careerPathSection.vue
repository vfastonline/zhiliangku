<template>
  <div class="cps-container rise">
      <img class="spsc-img" :class="['floatl','floatr'][mainData.index]" :src="mainData['path_img']" alt="">
      <div class="cpsc-introduce" :class="['floatr','floatl'][mainData.index]" >
          <div class="cpsci-title font24pr2C343B textellipsis">{{mainData.name}}</div>
          <div class="cpsci-content font14pr5a646e ofhid">{{mainData.desc}}</div>
          <div class="cpsci-button">
              <el-button class="font14pr23b8ff fontcenter" 
              @click="goPathInfo()"
              :style="myButtonStyle" type="small">查看详情
              </el-button>
            </div>
      </div>
  </div>
</template>
<script>
export default {
  name: 'careerPathSection',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      myButtonStyle:{'letter-spacing': '1px','height':'36px',
      'width':'124px','border':'2px  solid #23B8FF','border-radius':'18px'}
    }
  },
  props:{
      mainData:Object
  },
  methods:{
      goPathInfo(){
          window.location.href='/tracks/path/detail/?path_id='+this.mainData.id;
      }
  },
  created(){
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.cps-container{
    height: 400px;
    width: 1152px;
    box-sizing: border-box;
    padding: 32px;
    background:#ffffff;
    z-index: 1;
}
.cps-container:hover{
z-index:2;
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



