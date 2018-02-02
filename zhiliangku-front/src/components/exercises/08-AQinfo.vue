<template>
  <div class=" incenter">
    <div class="question-container">
      <question></question>
    </div>
    <anwserlist></anwserlist>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .question-container {
    background-color: white;
    padding-top: 44px;
    padding-bottom: 24px;
  }

</style>
<script>
  import question from './09-question'
  import anwserlist from './11-anwserList'
  export default {
    name: 'HelloWorld',
    data() {
      return {}
    },
    props: {

    },
    methods: {},
    created() {
      this.$get('/community/faq/detail/info?id=' + this.$fn.funcUrl('id')).then(res => {
        console.log(res)
      })
    },
    components: {
      question: question,
      anwserlist: anwserlist
    }
  }

</script>
