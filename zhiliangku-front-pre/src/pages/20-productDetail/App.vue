<template>
  <div id="app">
    <project-header></project-header>
    <shoppingHeader :styleData="styleData"></shoppingHeader>
    <productDetail></productDetail>
    <project-footer></project-footer>
  </div>
</template>
<script>
  import projectHeader from '../../components/home/projectHeader'
  import projectFooter from '../../components/home/projectFooter'
  import shoppingHeader from '../../components/09-shopping/02-shoppingHeader.vue'
  import productDetail from '../../components/09-shopping//07-productDetail'
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
      projectFooter: projectFooter,
      shoppingHeader: shoppingHeader,
      productDetail:productDetail
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
