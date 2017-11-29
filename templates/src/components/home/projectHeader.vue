<template>
  <div class="project-header">
    <div class="ph-content inmiddle clearfix">
      <img class='ph-logo' src='../../assets/img/icons/Logo.png' alt="">
      <span class="ph-tag">课程</span>
      <span class="ph-tag">直播</span>
      <span class="ph-tag">职业路径</span>
      <span class="ph-tag">社区</span>
      <span class="ph-tag last">线下课程</span>
      <span class="ph-search">
        <input type="text">
        <img class="phs-magnifier" src="../../assets/img/icons/Search-magnifier.svg" alt="">
      </span>
      <el-button type="primary" size="small" round >岗位匹配</el-button>
      <span class="user-info">
      <img class="user-icon" src="../../assets/img/user-icon.jpg" alt="">
      </span>
    </div>
  </div>
</template>
<script>
export default {
  name: "projectHeader",
  data() {
    return {
      msg: "Welcome to Your Vue.js App"
    };
  }
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style  lang='scss'>
.project-header {
  width: 100%;
  height: 70px;
  // background: brown;
  position: relative;
  // background: #FFFFFF;
  .ph-content {
    width: 80%;
    height: 48px;
    line-height: 48px;
    // background: skyblue;
  }
  .ph-logo {
    width: 9.72222%;
    height: auto;
    vertical-align: middle;
    margin-right: 3.8194%;
  }
  .ph-tag {
    opacity: 0.8;
    font-family: PingFangSC-Light "微软雅黑" "宋体";
    font-size: 18px;
    color: #3a3c50;
    padding-left: 2.2%;
    padding-right: 2.2%;
  }
  .ph-search{
    margin-right:5.556%;
  }
  .phs-magnifier{
    vertical-align: middle;
    width:1.7%;
    height:24px;
  }
  .user-info{
    float:right;
  }
  .user-icon{
    height: 48px;
    width:48px;
    vertical-align: middle;
    border-radius: 24px;
  }
}
</style>

