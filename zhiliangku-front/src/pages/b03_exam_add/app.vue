<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <sample_info></sample_info>
      <editor_block></editor_block>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>

</style>

<script>
  import MyHeader from '../../components/01_header_footer/b01_header'
  import F from '../../components/01_header_footer/03_footer'
  import sample_info from '../../components/b03_exam_add/01_exam_sample_info'
  import editor_block from '../../components/b03_exam_add/03_editor_block'
  export default {
    data() {
      return {}
    },
    components: {
      MyHeader: MyHeader,
      sample_info: sample_info,
      editor_block:editor_block,
      F: F,
    }
  }
</script>
