<template>
<div class="carousel zindex1">
  <el-carousel :interval="5000" >
    <el-carousel-item v-for="item in urls" :key="item.id">
      <!-- <img class="carouselimg" :src="item.pathwel" alt=""> -->
      <div v-lazy:background-image="item.pathwel" :style="{height:'100%',width:'100%'
      ,'background-repeat':'no-repeat','background-size':'cover','background-position':'center'}"></div>
    </el-carousel-item>
  </el-carousel>
</div>
</template>
<script>
export default {
  data(){
    return {
      urls:[],
      address:'/slides/list?category=1'
    }
  },
  created(){
    if(this.requestUrl){
     this.address= this.requestUrl;
    }
    this.$get(this.address).then(
      res=>{
        this.urls=this.$fn.addString(this.$myConst.httpUrl,res.data.data,'pathwel')
      }
    )
  },
  components:{
  },
  props:{
    requestUrl:String
  }
}
</script>

<style>
.carouselimg{
  width:100%;
  height: 100%;
}
</style>