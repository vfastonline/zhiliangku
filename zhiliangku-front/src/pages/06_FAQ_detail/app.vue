<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <faq_detail></faq_detail>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>

</style>

<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import F from '../../components/01_header_footer/03_footer'
  import faq_detail from '../../components/09_FAQ_detail/01_FAQ_detail'
  export default {
    data() {
      return {}
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      faq_detail:faq_detail
    }
  }
</script>
