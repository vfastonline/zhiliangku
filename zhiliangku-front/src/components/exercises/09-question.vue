<template>
  <div class="mainwidth incenter aq_container">
    <div class="aq-width incenter relative">
      <el-button class="foucusButton">关注这个问题</el-button>
      <el-button class="quizButton">我要提问</el-button>
      <div class="question-title font20pr3a3c50">{{mainData.title}}</div>
      <div>
        <div class="info relative">
          <img class="question-icon imgmiddle" :src="$myConst.httpUrl+mainData.custom_user_avatar" alt="">
          <span class="qestion-owner-name font14pl7c7e8c">{{mainData.custom_user_nickname}}</span>
          <span class="font14pl7c7e8c">{{mainData.create_time}}</span>
          <span class="scan font14pl7c7e8c">{{mainData.browse_amount}}次浏览</span>
        </div>
        <div v-html="mainData.description"></div>
      </div>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .aq-width {
    width: 780px;
  }

  .aq_container {
    background: white;
  }

  .foucusButton {
    position: absolute;
    left: -150px;
  }

  .quizButton {
    position: absolute;
    right: -123px;
  }
  .question-icon{
    border-radius: 50%;
  }
</style>
<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {}
    },
    props: {
      mainData: Object
    },
    methods: {

    },
    created() {

    },
    components: {

    }
  }

</script>
