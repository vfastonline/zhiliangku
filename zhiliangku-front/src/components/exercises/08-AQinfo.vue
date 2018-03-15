<template>
  <div class=" incenter">
    <div class="question-container">
      <question :mainData="mainData"></question>
    </div>
    <anwserlist :mainData="mainData"></anwserlist>
    <richtext class="richtext incenter" ></richtext>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .question-container {
    background-color: white;
    padding-top: 44px;
    padding-bottom: 24px;
  }
  .richtext{
    width: 780px;
  }
</style>
<script>
  import question from './09-question'
  import anwserlist from './11-anwserList'
  import richtext from './15-richtexteditor.vue'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        mainData:{}
      }
    },
    props: {

    },
    methods: {},
    created() {
      this.$get('/community/faq/detail/info?faq_id=' + this.$fn.funcUrl('id')).then(res => {
        console.log(res)
        this.mainData=res.data.data;

      })
    },
    components: {
      question: question,
      anwserlist: anwserlist,
      richtext:richtext
    }
  }

</script>
