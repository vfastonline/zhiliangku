<template>
  <div id="app">
    <project-header></project-header>
    <!-- <post-match></post-match> -->
    <!-- <carousel></carousel> -->
    <!--<subtitle :enTitle="a" :title="b" :slogon="c"></subtitle>-->
    <!-- <carrerps></carrerps> -->
    <!--<interview-cover></interview-cover>-->
    <!-- <interview-main></interview-main> -->
    <!--<cooperator ></cooperator>-->
    <!--<project-footer></project-footer>-->
    <!--<test></test>-->
    <!--<lvs></lvs>-->
    <!-- homeend -->
    <!-- <course-info></course-info> -->
    <!-- <project-pager></project-pager> -->
    <!-- <hcm></hcm> -->
    <!-- <router-view name='a' />   -->
    <!-- <router-view name='b' />   -->

    <!-- <before-add></before-add> -->
    <!-- <path-info></path-info> -->
    <!-- <course-select></course-select> -->



    <career-path-list></career-path-list>
    <!-- <project-header></project-header> -->
    <!-- <login></login> -->
    
    <project-footer></project-footer>
  </div>
</template>
<script>
  export default {
    name: 'app',
    data() {
      return {
        a: 'Live Course',
        b: '课程直播',
        c: '好好学习，天天向上',
        centerDialogVisible: false
      }
    },
    methods: {
      jj() {
        console.log(111)
      }
    }
  }

</script>
<style lang="scss">
  @import "./style/style";

</style>
<style lang="scss">
  @import "./style/bass";

</style>
