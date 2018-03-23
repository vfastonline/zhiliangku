<template>
  <div>
    <projectHeader :type="'videoHeader'"></projectHeader>
    <exercisesProgress></exercisesProgress>
    <videolist></videolist>
    <choiceQuestion></choiceQuestion>
    <projectFooter></projectFooter>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
<script>
  import exercisesProgress from '../../components/exercises/progress'
  import projectHeader from '../../components/home/projectHeader.vue'
  import projectFooter from '../../components/home/projectFooter.vue'
  import choiceQuestion from '../../components/exercises/choiceQuestion.vue'
  import videolist from '../../components/videoDetail/videolist.vue'
  import Bus from '../../assets/js/bus'
  export default {
  name: 'HelloWorld',
  data () {
    return {
    }
  },
  components:{
    exercisesProgress:exercisesProgress,
    projectHeader:projectHeader,
    projectFooter:projectFooter,
    choiceQuestion:choiceQuestion,
    videolist:videolist
  },
  created(){
     this.$on('showVideoList', function () {
        this.$children[2].$emit('openDialog')
      })
      this.$get('/tracks/video/detail/info?video_id=' + this.$fn.funcUrl('video_id')).then(res => {
        Bus.$emit('titleBreadCrumb',res.data.data)
      })
  }
}
</script>
<style lang="scss">
  @import "../../style/style";

</style>
<style lang="scss">
  @import "../../style/bass";
</style>


