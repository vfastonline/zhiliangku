<template>
  <div>
    <div class="marginbottom24">
      当前满足<span class="font16pl5A646E">3</span>个岗位需求 （岗位匹配度基于你的简历内容、学习行为给出）
    </div>
    <matchRatePart></matchRatePart>
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
    }
  },
    components:{
    matchRatePart:matchRatePart
  }
}
</script>


