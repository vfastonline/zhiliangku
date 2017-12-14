<template>
  <div class="mainwidth incenter pathInfo">
    <path-info-left :mainData="allData"></path-info-left>
    <path-info-right :mainData="allData"></path-info-right>
  </div>
</template>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      allData:{}
    }
  },
  created(){
    this.$ajax.get('tracks/path/detail/info?path_id=1').then(res=>{
       this.$fn.addObjString(this.$myConst.httpUrl,res.data.data,['path_img'])
       this.allData=res.data.data;
      console.log(res)
    })
  }
}
</script>
<style scoped>
.pathInfo{
    padding-top:60px;
}
</style>



