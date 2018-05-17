<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <MyVideo></MyVideo>
      <VideoRouterBar></VideoRouterBar>
      <button>123123123</button>
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
  import VideoRouterBar from '../../components/07_video_detail/08_video_sub_content'

  export default {
    data() {
      return {}
    },
    methods: {
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      MyVideo:MyVideo,
      VideoRouterBar:VideoRouterBar
    }
  }
</script>
