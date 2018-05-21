<template>
  <div class="sfq-container mw hc">
    <div class="incenter sfq-content">
      <sectionli v-for="(item,index) in mainData" :key="index" :mainData="item"></sectionli>
    </div>
    <Pager></Pager>
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
  import sectionli from './06_QA_unit'
  import Pager from '../00_common/06_pager'
  export default {
    name: 'FAQ',
    data () {
      return {
        mainData:""
      }
    },
    components:{
      sectionli:sectionli,
      Pager:Pager
    },
    created(){
      //这代码没什么用
      // var video_id=this.$fn.getSearchKey('video_id');
      // if(!video_id){
      //   video_id=1;
      //   var g='';
      //   if(window.location.search.length>1){g='&'}
      //   window.location.search+=g+'video_id='+video_id
      // }
    }
  }
</script>


