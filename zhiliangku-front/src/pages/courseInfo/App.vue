<template>
  <div id="app">
    <project-header></project-header>
    <before-add></before-add>
    <project-footer></project-footer>
  </div>
</template>
<script>
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
    created(){
      console.log(this)
    }
  }

</script>
<style lang="scss">
  @import "../../style/style";

</style>
<style lang="scss">
  @import "../../style/bass";

</style>
