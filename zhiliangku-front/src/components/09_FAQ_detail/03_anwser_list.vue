<template>
  <div class="mw incenter anwser_list_container relative">
    <div class="anwser_list" >
      <anwser v-for="(item) in mainData.faq_answer_list" :key="item.id" :questionId="mainData.id" :mainData="item"></anwser>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .anwser_list_container {
  //   background-color: white;
  }
  .answernum{
    position: absolute;
    top:-90px;
    left: 0;
  }
  .anwser_list{
    // margin-top: 94px;
    margin-bottom:20px;
  }
</style>
<script>
  import anwser from './04_anwser'
  export default {
    name: 'HelloWorld',
    data() {
      return {}
    },
    props: {
      mainData:Object
    },
    methods: {

    },
    created() {
    },
    components: {
      anwser: anwser
    }
  }
</script>
