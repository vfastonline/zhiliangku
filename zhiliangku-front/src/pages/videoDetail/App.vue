<template>
  <div id="app">
    <project-header :type="'videoHeader'"></project-header>
    <videoView :vid="vid"></videoView>
    <videolist></videolist>
    <videoContent :noteData="allData"></videoContent>
    <project-footer></project-footer>
  </div>
</template>
<script>
import Bus from '../../assets/js/bus'
  import projectHeader from '../../components/home/projectHeader.vue'
  import projectFooter from '../../components/home/projectFooter.vue'
  import videolist from '../../components/videoDetail/videolist.vue'
  export default {
    name: 'app',
    data() {
      return {
        allData: {},
        showList: false,
      }
    },
    methods: {
      jj() {
        console.log(111)
      }
    },
    components: {
      'projectHeader': projectHeader,
      'projectFooter': projectFooter,
      'videolist': videolist
    },
    methods: {
      getData(video_id) {
        this.$get('/tracks/video/detail/info?video_id=' + video_id).then(res => {
          this.allData = res.data.data;
          var tvue = this.$fn.getTargetVue(this.$children, 'videoContent');
          var note = this.$fn.getTargetVue(tvue.$children, 'notes')
          if (note) {
            note.$emit('noteData', res.data.data.notes)
          }
          this.noteData = res.data.data.notes;
          this.$children[1].$emit('vid', res.data.data.vid)
          Bus.$emit('titleBreadCrumb',res.data.data)
          console.log(res)
        })
      }
    },
    created() {
      this.$on('showVideoList', function () {
        this.$children[2].$emit('openDialog')
      })
      var video_id = this.$fn.getSearchKey('video_id');
      if (!video_id) {
        video_id = 1;
        var g = '';
        if (window.location.search.length > 1) {
          g = '&'
        }
        window.location.search += g + 'video_id=' + video_id
      }
      this.getData(video_id);
      // console.log(this)
    }
  }

</script>
<style lang="scss">
  @import "../../style/style";

</style>
<style lang="scss">
  @import "../../style/bass";

</style>
