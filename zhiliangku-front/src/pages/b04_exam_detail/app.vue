<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <select_time></select_time>
      <my_table></my_table>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>

</style>

<script>
  import MyHeader from '../../components/01_header_footer/b01_header'
  import select_time from '../../components/b04_exam_detail/01_select_time'
  import F from '../../components/01_header_footer/03_footer'
  import my_table from '../../components/b04_exam_detail/02_table'

  export default {
    data() {
      return {}
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      select_time:select_time,
      my_table:my_table
    }
  }
</script>
