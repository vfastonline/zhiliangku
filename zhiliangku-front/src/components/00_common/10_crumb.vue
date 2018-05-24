<template>
  <div class=" mw hc font1_20_6" :class="{grey:type==='grey',white:type==='white'}" v-html="main_data"></div>
</template>
<script>
  export default {
    data(){
      return {

      }
    },
    props: {
      main_data:'',
      type:{
        default:'grey'
      }
    },
    methods: {

    },
    created() {
    }
  }
</script>
<style>
  .grey a{
    color:#666;
    font-weight: bold;
  }
  .white a{
    color: #ffffff;
    font-weight: bold;
  }
</style>

