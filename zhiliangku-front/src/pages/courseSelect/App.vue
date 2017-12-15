<template>
  <div id="app">
    <project-header></project-header>
    <course-select></course-select>
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
