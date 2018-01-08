<template>
  <div id="app">
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
