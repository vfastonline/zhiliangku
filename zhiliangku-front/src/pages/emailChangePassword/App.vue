<template>
  <div id="app">
    <projectHeader></projectHeader>
    <emailChangePassword></emailChangePassword>
  </div>
</template>
<script>
  import emailChangePassword from '../../components/login/emailChangePassword'
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
      emailChangePassword:emailChangePassword
    }
  }

</script>
<style lang="scss">
  @import "../../style/style";

</style>
<style lang="scss">
  @import "../../style/bass";

</style>
