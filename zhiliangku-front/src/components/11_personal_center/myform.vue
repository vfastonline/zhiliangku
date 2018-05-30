<template>
  <div class="myform">
    <div class="myform-title font20pl3a3c50">编辑求职意向</div>
    <div class="myform-body">
      <div class="item  the-input">
        <span class="tags">期望职位</span>
        <el-input></el-input>
      </div>
      <div class="item  the-input">
        <span class="tags">期望职位</span>
        <el-input  type="textarea"></el-input>
        <div></div>
      </div>
      <div class="item  the-input">
        <span class="tags">期望职位</span>
        <el-select></el-select>
      </div>
      <div class="item  the-input">
        <span class="tags">期望职位</span>
        <el-date-picker  type="month" placeholder="选择月">
        </el-date-picker>
      </div>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    }
  }

</script>
<style lang="scss">
  @import "./style/01_resume_form.scss";
</style>
