<template>
<div class="sfq-container marginbottom24">
  <div class="incenter sfq-content">
    <sectionli v-for="(item,index) in mainData" :key="index" :mainData="item"></sectionli>
  </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.sfq-container{
    padding-top:32px;
    background:#fafafa;
    min-height:500px;
}
.sfq-content{
    width:780px;
}
</style>
<script>
import sectionli from './sectionCommen'
export default {
  name: 'HelloWorld',
  data () {
    return {
      mainData:""
    }
  },
  components:{
    sectionli:sectionli
  },
  created(){
      var video_id=this.$fn.getSearchKey('video_id');
      if(!video_id){
        video_id=1;
        var g='';
        if(window.location.search.length>1){g='&'}
        window.location.search+=g+'video_id='+video_id
      }
      this.$get('/tracks/common_question/list/info?video_id='+this.$fn.getSearchKey('video_id')).then(res=>{
        console.log(res.data.data)
        this.mainData=res.data.data
      })
  }
}
</script>


