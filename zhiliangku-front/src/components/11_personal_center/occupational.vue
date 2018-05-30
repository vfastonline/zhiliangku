<template>
  <div class="mainwidth incenter personnal-center-main clearfix">
    <ul class="floatl personal-center-left">
      <li><router-link to='/occupational/matchingRate'><span class="font14pr3a3c50">岗位匹配度</span><span class="pcl-triangle"></span></router-link></li>
      <li><router-link to='/occupational/comprehensiveEvalution'><span class="font14pr3a3c50">综合素质评分</span><span class="pcl-triangle"></span></router-link></li>
      <li><router-link to='/occupational/focusOnMe'><span class="font14pr3a3c50">关注我的企业</span><span class="pcl-triangle"></span></router-link> </li>
    </ul>
    <div class="personal-center-right">
      <router-view ></router-view>
    </div>

  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
  @import "./style/02_personal_center.scss";

</style>
<style scoped>
</style>
<script>
export default {
  data () {
    return {
    }
  }
}
</script>


