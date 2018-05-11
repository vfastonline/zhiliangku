<template>
  <div id="app">
    <projectHeader></projectHeader>
    <interviewPeogress  ></interviewPeogress>
    <interviewExercies></interviewExercies>
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
  import interviewExercies from '../../components/interview/interviewExercises'
  import interviewPeogress from '../../components/interview/interviewProgress'
  import projectHeader from '../../components/home/projectHeader.vue'
  import projectFooter from '../../components/home/projectFooter.vue'
  import Bus from '../../assets/js/bus'
  export default {
    data() {
      return {
        mainData:{}
      }
    },
    methods: {
      jj() {
        console.log(111)
      }
    },
    created() {

    },
    methods: {},
    components: {
      projectHeader: projectHeader,
      projectFooter: projectFooter,
      interviewPeogress: interviewPeogress,
      interviewExercies,
      interviewExercies
    },


  }

</script>
<style lang="scss">
  @import "../../style/style";

</style>
<style lang="scss">
  @import "../../style/bass";

</style>
