<template>
  <div id="app">
    <project-header :type="'videoHeader'"></project-header>
    <!-- <videoView></videoView> -->
    <videoContent></videoContent>
    <project-footer></project-footer>
  </div>
</template>
<script>
  import projectHeader from '../../components/home/projectHeader.vue'
  import projectFooter from '../../components/home/projectFooter.vue'

  export default {
    name: 'app',
    data() {
      return {}
    },
    methods: {
      jj() {
        console.log(111)
      }
    },
    components: {
      'projectHeader': projectHeader,
      'projectFooter': projectFooter,
    },
    created() {
      this.$get('tracks/video/detail/info?video_id=1').then(res=>{
        console.log(res)
      })
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
