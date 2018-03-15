<template>
  <div id="app">
    <project-header></project-header>
      <AQinfo></AQinfo>
    <project-footer></project-footer>
  </div>
</template>
<script>
  import AQinfo from '../../components/exercises/08-AQinfo.vue'
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
      // console.log(this)
    },
    components: {
      AQinfo: AQinfo
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
