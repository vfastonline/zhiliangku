<template>
  <div class="mw hc">
    <video-player id="my-video" :options="playerOptions"></video-player>
  </div>
</template>

<script>
  import Vue from 'vue'
  import VueVideo from 'vue-video-player'
  import 'video.js/dist/video-js.css'

  Vue.use(VueVideo)
  export default {
    name: "my_video",
    data() {
      return {
        playerOptions: {
          // video js options
          muted: true,
          language: 'en',
          playbackRates: [1.0, 1.25, 1.5, 1.75, 2.0],
          sources: [{
            type: "video/mp4",
            src: "https://cdn.theguardian.tv/webM/2015/07/20/150716YesMen_synd_768k_vp8.webm"
          }],
          fluid: true,
          poster: ""// 海豹图片地址
        }
      }
    }
  }
</script>

<style scoped>

</style>
