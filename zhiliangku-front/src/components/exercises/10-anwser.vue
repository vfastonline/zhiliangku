<template>
  <div class="anwser-container incenter">
    <div class="relative">
      <img class="question-user-icon imgmiddle" src="../../assets/img/user-icon.jpg" alt="">
      <span class="font14pl7c7e8c">bob</span>
      <span class="font14pl7c7e8c scan">2018-19-29</span>
    </div>
    <div>
      这是问题内容
    </div>
    <div class="relative">
      <div>
        <img src="../../assets/img/icons/QQ.svg" alt="">
        <span class="question-yes font16fbc02d">3</span>
        <img src="../../assets/img/icons/QQ.svg" alt="">
        <span class="question-yes ">3</span>
      </div>
      <div>
        回复
        <img src="../../assets/img/icons/QQ.svg" alt="">
      </div>
    </div>
    <div class="msg-moudel">
      <div class="relative">
        <img class="question-user-icon imgmiddle" src="../../assets/img/user-icon.jpg" alt="">
        <span class="font14pl7c7e8c">bob</span>
        <span class="font14pl7c7e8c scan">2018-19-29 12:45</span>
      </div>
      <div class="msg-container">
      </div>
    </div>
    <div></div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .anwser-container {
    padding: 32px;
  }

  .question-user-icon {
    width: 48px;
    height: 48px;
    margin-right: 32px;
  }

  .question-yes {
    margin-right: 54px;
  }
  .msg-container{
      padding-left:80px;
  }
  .msg-moudel{
      
  }
</style>
<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {}
    },
    props: {

    },
    methods: {

    },
    created() {

    },
    components: {

    }
  }

</script>
