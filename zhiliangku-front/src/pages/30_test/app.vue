<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <F></F>
    </div>
  </div>
</template>
<style scoped lang='scss'>
</style>
<script>
import MyHeader from '../../components/01_header_footer/01_header'
import F from '../../components/01_header_footer/03_footer'

export default {
  data () {
    return {}
  },
  components: {
    MyHeader: MyHeader,
    F: F
  },
  mounted () {
  }
}

</script>
