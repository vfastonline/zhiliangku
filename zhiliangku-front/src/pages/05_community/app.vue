<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <community></community>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>

</style>

<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import F from '../../components/01_header_footer/03_footer'
  import community from '../../components/08_community/01_community'
  export default {
    data() {
      return {}
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      community:community
    }
  }
</script>
