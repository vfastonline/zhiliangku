<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <set_addition></set_addition>
      <content_layout></content_layout>
      <pager></pager>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>
  @import "../../assets/style/baseConstScss";
#main{
  background-color: $bgc;
  padding-bottom: 20px;
}
</style>

<script>
  import MyHeader from '../../components/01_header_footer/b01_header'
  import F from '../../components/01_header_footer/03_footer'
  import set_addition from '../../components/b02_exam_statistic/01_set_addition'
  import content_layout from '../../components/b02_exam_statistic/02_content_layout'
  import pager from '../../components/00_common/06_pager'
  export default {
    data() {
      return {}
    },
    components: {
      MyHeader: MyHeader,
      set_addition:set_addition,
      content_layout:content_layout,
      pager:pager,
      F: F
    }
  }
</script>
