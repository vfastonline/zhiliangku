<template>
  <div class=" mw hc">
    <div class="ftc hc failure_status">
      <p class="font1_26_c">很遗憾，你没有通过考核，继续加油！</p>
    </div>
    <!-- 区别成功失败的页面样式-->
    <div class="ftc failure_emoticon">
      <img :src="$myConst.httpUrl+'/media/image/static/assess_result_01_sad.png'" alt="">
    </div>
    <div class="success_bottom ftc">
      <p class="font1_18_6">本次考核结果：答对 {{main_data.right||0}} 个，答错 {{main_data.wrong || 0}} 个</p>
    </div>
  </div>
</template>
<script>
  export default {
    data() {
      return {}
    },
    props: {
      main_data: ''
    }
  }
</script>
<style>
  .failure_status {
    margin-top: 50px;
  }

  .success_status p {
    hieght: 26px;
    line-height: 26px;
  }

  .failure_emoticon {
    padding: 20px 0 30px;
  }

  .success_emoticon p {
    height: 100px;
    width: 100px;
  }
</style>
