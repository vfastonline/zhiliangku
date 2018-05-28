<template>
  <div class=" mw hc">
    <div class="ftc hc success_status">
      <p class="font1_26_c">恭喜你已顺利通过考核，再接再厉！</p>
    </div>
    <!-- 区别成功失败的页面样式-->
    <div class="ftc success_emoticon">
      <img :src="$myConst.httpUrl+'/media/image/static/assess_result_01_happy.png'" alt="">
    </div>
    <div class="ftc">
      <p class="font1_18_6">本次考核结果：</p>
    </div>
  </div>
</template>
<script>
  export default {
    data() {
      return {}
    },
    props: {
      status: ''
    }
  }
</script>
<style>
  .success_status {
    margin-top: 200px;
  }

  .success_status p {
    hieght: 26px;
    line-height: 26px;
  }

  .success_emoticon {
    padding: 50px 0 82px;
  }

  .failure_emoticon {
    padding: 20px 0 30px;
  }

  .success_emoticon p {
    height: 100px;
    width: 100px;
  }
</style>
