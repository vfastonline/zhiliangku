<template>
  <div id="app">
    <projectHeader></projectHeader>
    <div class="mainwidth incenter ir-container">
      <interviewleft :mainData="mainData"></interviewleft>
      <div class="ir-right">
        <interviewright :mainData="mainData"></interviewright>
      </div>
    </div>
    <projectFooter></projectFooter>
  </div>
</template>
<style>
  .ir-container {
    margin-top: 54px;
  }

  .ir-right {
    margin-left: 400px;
  }

</style>
<script>
  import interviewright from '../../components/interview/interviewResultRight'
  import interviewleft from '../../components/interview/interviewResultLeft'
  import projectHeader from '../../components/home/projectHeader.vue'
  import projectFooter from '../../components/home/projectFooter.vue'
  import Bus from '../../assets/js/bus'
  export default {
    data() {
      return {
        mainData: {}
      }
    },
    methods: {
      jj() {
        console.log(111)
      }
    },
    components: {
      projectHeader: projectHeader,
      projectFooter: projectFooter,
      interviewleft: interviewleft,
      interviewright: interviewright
    },
    methods: {},
    created() {
      
    }
  }

</script>
<style lang="scss">
  @import "../../style/style";

</style>
<style lang="scss">
  @import "../../style/bass";

</style>
