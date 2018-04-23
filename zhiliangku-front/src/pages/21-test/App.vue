<template>
  <div id="app">
    <project-header></project-header>
    <test></test>  
    
  </div>
</template>
<script>
  import projectHeader from '../../components/home/projectHeader'
  import test from '../../components/10-test/test'
  export default {
    name: 'app',
    data() {
      return {
        
      }
    },
    methods: {
      jj() {
        console.log(111)
      }
    },
    created() {
      // console.log(this)
    },
    components: {
      projectHeader: projectHeader,
      test:test
    }
  }

</script>
<style lang="scss">
  @import "../../style/style";

</style>
<style lang="scss">
  @import "../../style/bass";
  @import "../../style/scss/components/06-AQinfo.scss";

</style>
