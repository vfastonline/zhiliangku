<template>
  <div class="mainwidth incenter personnal-center-main clearfix">
    <ul class="floatl personal-center-left">
      <li><router-link to='/myCourse/recentlyLearing'><span class="font14pr3a3c50">最近学习</span><span class="pcl-triangle"></span></router-link></li>
      <li><router-link to='/myCourse/myCollection'><span class="font14pr3a3c50">我的收藏</span><span class="pcl-triangle"></span></router-link></li>
      <li><router-link to='/myCourse/myPath'><span class="font14pr3a3c50">我的路径</span><span class="pcl-triangle"></span></router-link> </li>
    </ul>
    <div class="personal-center-right">
      <router-view ></router-view>
    </div>
    
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
  @import "../../style/scss/components/personalCenter.scss";

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


