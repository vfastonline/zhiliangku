<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <loginPage></loginPage>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>

</style>

<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import F from '../../components/01_header_footer/03_footer'
  import loginPage from '../../components/02_login/07_login_page'

  export default {
    data() {
      return {}
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      loginPage:loginPage
    }
  }
</script>
