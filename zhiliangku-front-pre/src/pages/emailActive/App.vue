<template>
  <div id="app">
    <projectHeader></projectHeader>
    <emailActive></emailActive>
  </div>
</template>
<script>
  import emailActive  from '../../components/login/03-emailActive'
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
      emailActive:emailActive
    }
  }

</script>
<style lang="scss">
  @import "../../style/style";

</style>
<style lang="scss">
  @import "../../style/bass";

</style>
