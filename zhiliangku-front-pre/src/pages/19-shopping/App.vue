<template>
  <div id="app">
    <project-header></project-header>
    <shoppingHeader :styleData="styleData"></shoppingHeader>
    <mainRouter :routerInfo="routerData"></mainRouter>
    <project-footer></project-footer>
  </div>
</template>
<script>
  import projectHeader from '../../components/home/projectHeader'
  import projectFooter from '../../components/home/projectFooter'
  import mainRouter from '../../components/personalCenter/mainRouter.vue'
  import shoppingHeader from '../../components/09-shopping/02-shoppingHeader.vue'
  export default {
    name: 'app',
    data() {
      return {
        styleData: {
          heigh: '250px'
        },
        routerData: [{
            to: {
              path: 'allProduct',
              
            },
            name: '全部商品'
          },
          {
            to: {
              path: 'virtualProduct',
            },
            name: '虚拟商品'
          },
          {
            to: {
              path: 'entityProduct',
            },
            name: '实体商品'
          },
          {
            to: {
              path: 'convertionRecordList',
            },
            name: '兑换记录'
          }
        ]
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
      mainRouter: mainRouter,
      projectHeader: projectHeader,
      projectFooter: projectFooter,
      shoppingHeader: shoppingHeader
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
