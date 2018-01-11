<template>
  <div id="app">
    <projectHeader></projectHeader>
    <personalInfo></personalInfo>
    <mainRouter></mainRouter>
    <projectFooter></projectFooter>
  </div>
</template>
<style>
  .persona-center-navbar {
    height: 70px;
    line-height: 70px;
  }

  .persona-center-navbar .router-link-active {
    color: #23B8FF;
  }

</style>
<script>
  import Bus from '../../assets/js/bus'

  import projectHeader from '../../components/home/projectHeader.vue'
  import projectFooter from '../../components/home/projectFooter.vue'
  import mainRouter from '../../components/personalCenter/mainRouter.vue'
  import personalInfo from '../../components/personalCenter/personalInfo.vue'
  export default {
    data() {
      return {}
    },
    methods: {
      jj() {
        console.log(111)
      }
    },
    components: {
      projectHeader: projectHeader,
      projectFooter: projectFooter,
      mainRouter: mainRouter,
      personalInfo: personalInfo
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
