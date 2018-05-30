<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <personalInfo></personalInfo>
      <mainRouter :routerInfo="routerData"></mainRouter>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>

</style>

<script>
  import Bus from '../../assets/js/02_bus'
  import MyHeader from '../../components/01_header_footer/01_header'
  import F from '../../components/01_header_footer/03_footer'
  import mainRouter from '../../components/personalCenter/mainRouter.vue'
  import personalInfo from '../../components/personalCenter/personalInfo.vue'

  export default {
    name: 'personal_center',
    data() {
      return {
        routerData: [{
          to: {path: '/occupational'},
          name: '职业信息'
        },
          {
            to: {path: '/myCourse'},
            name: '我的课程'
          },
          {
            to: {path: '/myResume'},
            name: '我的简历'
          },
          {
            to: {path: '/mySettings'},
            name: '个人设置'
          },
          {
            to: {path: '/myVIP'},
            name: '我的VIP'
          }

        ]
      }
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      mainRouter: mainRouter,
      personalInfo: personalInfo
    }
  }
</script>
