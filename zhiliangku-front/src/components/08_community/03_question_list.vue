<template>
  <div class="mainwidth incenter">
    <question @haveClick="godetail(item)"  v-for="(item,index) in mainData" :key="index" :mainData="item"></question>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
<script>
  import question from '../07_video_detail/04_question_answer_unit'
  export default {
    name: 'question_list',
    data () {
      return {
      }
    },
    props:{
      mainData:Array
    },
    methods:{
      godetail(item){
        window.location.href='/community/faq/detail/?id='+item.id
      }
    },
    created(){
    },
    components:{
      question:question
    }
  }
</script>


