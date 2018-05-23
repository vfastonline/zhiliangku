<template>
  <div class="sfq-container mw hc">
    <div class=" sfq-content">
      <sectionli v-for="(item,index) in mainData" :key="index" :mainData="item"></sectionli>
    </div>
    <Pager @pagerGetData="mainPagerData" :url="url" :addition-data="params"></Pager>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .sfq-container{
    padding-top:32px;
    /*background:#fafafa;*/
    min-height:70vh;
    margin-bottom: 30px;
  }
  .sfq-content{
    width:780px;
    min-height: 65vh;
  }
</style>
<script>
  import sectionli from './06_FQA_unit'
  import Pager from '../00_common/06_pager'
  export default {
    name: 'FAQ',
    data () {
      return {
        mainData:"",
        url: '/tracks/common_question/list/info',
        params: {}
      }
    },
    components:{
      sectionli:sectionli,
      Pager:Pager
    },
    methods: {
      // get_faq_data() {
      //   this.video_id = this.$fn.funcUrl("video_id")
      //   this.$get('tracks/common_question/list/info?video_id='+this.video_id).then(res => {
      //     console.log(res.data.data);
      //
      //   })
      // },
      mainPagerData(res) {
        // console.log(res.data)
        this.mainData = res.data.data
      }
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

      // this.get_faq_data()
      let video_id = this.$fn.funcUrl('video_id')
      this.params={
        'video_id':video_id,
      }
    }
  }
</script>


