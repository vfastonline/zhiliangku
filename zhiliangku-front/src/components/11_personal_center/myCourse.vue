<template>
  <div class="mw hc personnal-center-main clearfix">
    <ul class="fl personal-center-left">
      <li><router-link to='/myCourse/recentlyLearing'><span class="font14pr3a3c50">最近学习</span><span class="pcl-triangle"></span></router-link></li>
      <li><router-link to='/myCourse/myCollection'><span class="font14pr3a3c50">我的收藏</span><span class="pcl-triangle"></span></router-link></li>
      <li><router-link to='/myCourse/myPath'><span class="font14pr3a3c50">我的路径</span><span class="pcl-triangle"></span></router-link> </li>
      <li><router-link to='/myCourse/recommondCourse'><span class="font14pr3a3c50">推荐课程</span><span class="pcl-triangle"></span></router-link> </li>
    </ul>
    <div class="personal-center-right">
      <router-view ></router-view>
    </div>
  </div>
</template>
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


