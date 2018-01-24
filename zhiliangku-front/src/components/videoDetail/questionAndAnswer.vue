<template>
  <div class="qa-container">
    <div class="mainwidth incenter">
     <qustionli v-for="(item,index) in mainData" :key="index" :mainData="item"></qustionli>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.qa-container{
  padding-top:32px;
    background:#fafafa;
    min-height:500px;
}
</style>
<script>
import qustionli from './questionCommen'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        mainData:{}
      }
    },
    components:{
      qustionli:qustionli
    },
    created(){
      var video_id=this.$fn.getSearchKey('video_id');
      this.$get('/community/faq/list/info?video_id='+this.$fn.getSearchKey('video_id')).then(res=>{
        console.log(res)
        this.$fn.addString(this.$myConst.httpUrl,res.data.data,'custom_user_avatar')
        this.mainData=res.data.data
      })
    }
  }

</script>
