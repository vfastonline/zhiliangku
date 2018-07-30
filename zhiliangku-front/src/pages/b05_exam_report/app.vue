<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>

</style>

<script>
  import MyHeader from '../../components/01_header_footer/b01_header'
  import F from '../../components/01_header_footer/03_footer'

  export default {
    data() {
      return {}
    },
    components: {
      MyHeader: MyHeader,
      F: F
    }
  }
</script>
