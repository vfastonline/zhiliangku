<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <MessageCenter></MessageCenter>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>

</style>

<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import F from '../../components/01_header_footer/03_footer'
  import  MessageCenter from '../../components/14_notification/01_message_center'
  export default {
    data() {
      return {}
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      MessageCenter:MessageCenter
    }
  }
</script>
