<template>
  <div>
    <div class="marginbottom24">
      当前满足<span class="font16pl5A646E">{{mainData.length}}</span>个岗位需求 （岗位匹配度基于你的简历内容、学习行为给出）
    </div>
    <matchRatePart v-for="(item,index) in mainData" :key="index"  :mainData="item" :otherData="otherData[index]" ></matchRatePart>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
<script>
import matchRatePart from './matchRatePart'
export default {
  data () {
    return {
      mainData:{},
      otherData:{}
    }
  },
  created(){
    this.$get('/personal_center/job/post/match?custom_user_id='+localStorage.uid).then(res=>{
      console.log(res)
      // this.$fn.addString(this.$myConst.httpUrl+,res.data.data,'logo')
      this.mainData=res.data.data;
    })
    this.$get('/personal_center/job/post/match/detail?custom_user_id='+localStorage.uid).then(res=>{
      console.log(res);
      this.otherData=res.data.data;
    })
  },
    components:{
    matchRatePart:matchRatePart
  }
}
</script>


