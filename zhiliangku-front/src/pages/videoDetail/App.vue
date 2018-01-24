<template>
  <div id="app">
    <project-header :type="'videoHeader'"></project-header>
    <videoView :vid="vid"></videoView>
    <videolist></videolist>
    <videoContent v-if="showCP" :noteData="allData"></videoContent>
    <project-footer v-if="showCP"></project-footer>
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
        showCP:true
      }
    },
    watch:{
      showCP:function(){
        console.log('change  i am hear')
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
          this.acction(res)
          console.log(res)
          // 
          this.sendMsg(res)
          Bus.$emit('titleBreadCrumb',res.data.data)
          
        })
      },
      acction(res){
        if(!this.showCP){return}
          this.allData = res.data.data;
          Bus.$emit('noteData', res.data.data.notes)
          this.noteData = res.data.data.notes;
      },
      changeshow(){
        console.log(this.$fn.funcUrl('type'))
        if(this.$fn.funcUrl('type')==3){
          console.log(this.$fn.funcUrl)
        this.showCP=false
      }
      },
      sendMsg(res){
        if(this.showCP){this.$children[1].$emit('vid', res.data.data.vid)}
        else{
          this.$children[1].$emit('liveid', res.data.data.live_channelId)
        }
      }
    },
    created() {
      this.changeshow();
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
