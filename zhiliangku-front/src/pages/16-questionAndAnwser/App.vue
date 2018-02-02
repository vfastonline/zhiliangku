<template>
  <div id="app">
    <project-header></project-header>
    <community></community>
    <project-footer></project-footer>
  </div>
</template>
<script>
import community from '../../components/exercises/03-community'
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
    },
    components:{
      community:community
    }
  }

</script>
<style lang="scss">
  @import "../../style/style";

</style>
<style lang="scss">
  @import "../../style/bass";

</style>
