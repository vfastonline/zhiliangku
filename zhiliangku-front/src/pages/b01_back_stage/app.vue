<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <top_content></top_content>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>

</style>

<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import F from '../../components/01_header_footer/03_footer'
  import top_content from '../../components/b01_back_stage/01_index'
  export default {
    data() {
      return {}
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      top_content:top_content,
    }
  }
</script>
