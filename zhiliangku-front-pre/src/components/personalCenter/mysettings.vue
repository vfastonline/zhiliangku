<template>
  <div class="mainwidth incenter personnal-center-main clearfix">
    <ul class="floatl personal-center-left">
      <li><router-link to='/mySettings/baseInfo'><span class="font14pr3a3c50">基本信息</span><span class="pcl-triangle"></span></router-link></li>
      <li><router-link to='/mySettings/bindAccount'><span class="font14pr3a3c50">账号绑定</span><span class="pcl-triangle"></span></router-link></li>
      <li><router-link to='/mySettings/password'><span class="font14pr3a3c50">密码设置</span><span class="pcl-triangle"></span></router-link> </li>
      <li><router-link to='/mySettings/address'><span class="font14pr3a3c50">收货地址</span><span class="pcl-triangle"></span></router-link> </li>
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


