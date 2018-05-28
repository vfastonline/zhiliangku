<template>
  <div class=" mw hc">
    <div class="ftc hc" :class="{'success_status':status===1, 'failure_status':status===0}">
      <p class="font1_26_c">恭喜你已顺利通过考核，再接再厉！</p>
    </div>
    <!-- 区别成功失败的页面样式-->
    <div class="ftc" :class="{'success_emoticon':status===1,'failure_emoticon':status===0}">
      <img :src="$myConst.httpUrl+'/media/image/static/assess_result_01_happy.png'" alt="">
    </div>
    <div class="success_bottom ftc">
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

  .failure_status {
    margin-top: 50px;
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
