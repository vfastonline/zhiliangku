<template>
  <div class="aq-width incenter anwser_list_container relative">
    <div class="answernum">{{mainData.faq_answer_list.length}}个回答</div>
    <div class="anwser_list" >
    <anwser v-for="(item,index) in mainData.faq_answer_list" :key="index" :mainData="item"></anwser>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .anwser_list_container {
     
  }
  .answernum{
    position: absolute;
    top:-30px;
    left: 0;
  }
  .anwser_list{
    margin-top: 94px;
  }
</style>
<script>
  import anwser from './10-anwser'
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
