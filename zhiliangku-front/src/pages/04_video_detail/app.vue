<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <MyVideo></MyVideo>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>

</style>

<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import F from '../../components/01_header_footer/03_footer'
  import MyVideo from '../../components/07_video_detail/01_video'

  export default {
    data() {
      return {}
    },
    methods: {
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      MyVideo:MyVideo
    }
  }
</script>
