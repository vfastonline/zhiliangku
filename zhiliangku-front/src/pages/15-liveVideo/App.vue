<template>
  <div id="app">
    <project-header :type="'videoHeader'"></project-header>
    <videoView ></videoView>
    <videolist></videolist>
  </div>
</template>
<script>
  import Bus from '../../assets/js/bus'
  import projectHeader from '../../components/home/projectHeader.vue'
  import videolist from '../../components/videoDetail/videolist.vue'
  import  videoView from '../../components/videoDetail/10-liveVideo.vue'
  export default {
    name: 'app',
    data() {
      return {
        allData: {},
        showList: false,

      }
    },
    watch:{
      
    },
    methods: {
      jj() {
        console.log(111)
      }
    },
    components: {
      'projectHeader': projectHeader,
      'videolist': videolist,
      videoView:videoView
    },
    methods: {
      getData(video_id) {
        this.$get('/tracks/video/detail/info?video_id=' + video_id).then(res => {
          this.acction(res)
          console.log(res)
          this.sendMsg(res)
          Bus.$emit('titleBreadCrumb',res.data.data)
        })
      },
      acction(res){
          this.allData = res.data.data;
      },
      sendMsg(res){
          this.$children[1].$emit('liveid', res.data.data.live_channelId)
      }
    },
    created() {
      this.$on('showVideoList', function () {
        this.$children[2].$emit('openDialog')
      })
      var video_id = this.$fn.getSearchKey('video_id');
      this.getData(video_id);
    }
  }

</script>
<style lang="scss">
  @import "../../style/style";

</style>
<style lang="scss">
  @import "../../style/bass";

</style>
