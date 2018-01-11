<template>
  <div class="match-rate-part-container rise">
    <courseli :mainData="courseData"></courseli>
    <div class="mrpc-additional-list">
      <div class="marginbottom24">
        <span class="font16pl3a3c50 inlineblock mrpc-salary">6K-8K</span>
        <span class="font14pr424242">移动互联网、游戏/上市公司/北京/全职</span>
      </div>
      <ul >
        <li class="marginbottom24 textellipsis">
          <img class="mrpc-conform" src="../../assets/img/icons/个人中心和积分商城图标/勾选框_空选.svg" alt="">
          <span class="textellipsis">1-3年工作经验</span>
        </li>
        <li >
          <img class="mrpc-conform textellipsis" src="../../assets/img/icons/个人中心和积分商城图标/勾选框_选中.svg" alt="">
          <span class="textellipsis">本科及以上</span>
        </li>
      </ul>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
import courseli from './courseLi'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        courseData:{job:true}
      }
    },
    components:{
      courseli:courseli
    }
  }
</script>
<style>
  .match-rate-part-container,
  .match-rate-part-inner {
    padding: 16px 24px;
    background: white;
  }

  .match-rate-part-inner {
    height: 100px;
  }

  .mrpc-company-logo {
    height: 100px;
    width: 100px;
  }

  .mrpc-match-rate {
    margin-right: 32px;
  }
  .mrpc-company-info {
    margin-left: 130px;
  }
  .mrpc-progress .el-progress-bar__inner {
    border-radius: 0px
  }
  .mrpc-progress .el-progress-bar__outer {
    border-radius: 0;
  }
  .mrpc-company-line2 {
    /* line-height: 38px; */
    height: 40px;
  }
  .mrpc-job-name,
  .mrpc-progress {
    width: 340px;
  }
  .mrpc-salary{
    margin-right:24px;
  }
  .mrpc-conform{
    vertical-align:middle;
    margin-right:21px;
  }
</style>

