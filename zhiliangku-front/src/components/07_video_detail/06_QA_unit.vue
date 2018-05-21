<template>
  <div class="sc-container rise mw hc">
    <div class=" sc-question-container">
      <div class="fl  font1_20_b4 sc-tag">Q:</div>
      <div class="sc-question-title font14pl3a3c50" v-html="mainData.question"></div>
    </div>
    <div class="sc-question-content font14pl3a3c50" v-html="mainData.answer"></div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
  .sc-container {
    padding: 31px 40px 24px 40px;
    background: white;
    margin-bottom: 24px;
  }

  .sc-tag {
    opacity: 0.5;
  }

  .sc-question-container {
    line-height: 32px;
  }

  .sc-question-title {
    margin-left: 33px;
    pre {
      white-space: pre-wrap;
      word-wrap: break-word;
    }
  }

  .sc-question-content {
    margin-left: 32px;
    opacity: 0.6;
    pre {
      white-space: pre-wrap;
      word-wrap: break-word;
    }
  }
</style>
<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    },
    props: {
      mainData: Object
    },
    created() {
    }
  }

</script>
