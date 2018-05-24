<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <MyVideo :main_data="video_detail_datas" :main_list="video_detail_lists"></MyVideo>
      <VideoRouterBar :main_data="video_detail_datas.data"></VideoRouterBar>
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
  import VideoRouterBar from '../../components/07_video_detail/08_router_button'
  import Bus from '../../assets/js/02_bus'

  export default {
    data() {
      return {
        video_detail_datas: '',
        video_detail_lists: '',
        breadcrumbs: ''
      }
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      MyVideo:MyVideo,
      VideoRouterBar:VideoRouterBar
    },
    methods: {
      initData() {
        let video_id = this.$fn.funcUrl("video_id")
        let course_id = this.$fn.funcUrl("course_id")
        let custom_user_id = localStorage.getItem("uid")
        this.$get("/tracks/video/detail/info?video_id=" + video_id).then(res => {
          this.video_detail_datas = res.data
          console.log(this.video_detail_datas)
          Bus.$emit('noteData',res.data.data.notes)
        })
        this.$get("/tracks/course/detail/info?custom_user_id="+custom_user_id+"&course_id="+course_id).then(res => {
          this.video_detail_lists = res.data.data
        })
      }
    },
    created() {
      this.initData()
    }
  }
</script>
