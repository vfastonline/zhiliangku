<template>
  <div id="app">
    <projectHeader></projectHeader>
    <loginPage></loginPage>
  </div>
</template>
<script>
  import loginPage from '../../components/login/loginPage'
  import projectHeader from '../../components/home/projectHeader'
  import projectFooter from '../../components/home/projectFooter'
  export default {
    name: 'app',
    data() {
      return {}
    },
    methods: {
      jj() {
        console.log(111)
      }
    },
    created() {
      console.log(this)
    },
    components: {
      projectHeader: projectHeader,
      projectFooter: projectFooter,
      loginPage:loginPage
    }
  }

</script>
<style lang="scss">
  @import "../../style/style";

</style>
<style lang="scss">
  @import "../../style/bass";

</style>
