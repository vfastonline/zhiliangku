<template>
  <div id="app">
    <projectHeader></projectHeader>
    <pathInfo></pathInfo>
    <projectFooter></projectFooter> 
  </div>
</template>
<script>
import projectHeader from '../../components/home/projectHeader.vue'
  export default {
    name: 'app',
    data() {
      return {
      }
    },
    methods: {
    },
    components:{
      projectHeader:projectHeader
    },
    created(){
    }
  }

</script>
<style lang="scss">
  @import "../../style/style";

</style>
<style lang="scss">
  @import "../../style/bass";

</style>
