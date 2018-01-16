<template>
  <div class="resume-improve">
    <p class="ri-title font20pr3a3c50">面试结果投递</p>
    <p class="ri-content">
      你还没有一份完善的简历， 为了保证最佳的投递效果，请先完善你的简历信息后再进行面试结果投递。 本次面试结果已存档到智量酷的云服务器。 你可以随时在“企业面试题”--“我已经完成的面试题”中查看这份面试结果。
    </p>
    <button>去完善简历</button>
    <button>取消</button>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .resume-improve {
    width: 649px;
    height: 291px;
    background: #FFFFFF;
    box-sizing: border-box;
    background: #FFFFFF;
    box-shadow: 0 0 10px 5px rgba(99, 117, 138, 0.10);
    padding-top: 16px;
    padding-left: 38px;
  }

  .resume-improve .ri-title {
    height: 28px;
    line-height: 28px;
  }

  .font20pr3a3c50 {
    font-family: 'PingFangSC-Light';
    font-size: 20px;
    color: #3A3C50;
  }

  .ri-content {
    width: 540px;
    height: 120px;
    letter-spacing: 1px;
    line-height: 30px;
    margin-top: 16px;
    margin-left: 69px;
  }

  .font14pr5a646e {
    font-family: PingFangSC-Regular;
    font-size: 14px;
    color: #5A646E;
  }

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
