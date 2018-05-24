<template>
  <section class="mw hc video_container">
    <div class="video_title ftj">
      <Crumb class="dib crumb" :main_data="main_data.breadcrumbs" :type="'white'"></Crumb>
      <!--<span class="cp dib font1_18_f pointer ">-->
        <!--<svg class="icon" aria-hidden="true">-->
          <!--<use xlink:href="#icon-hanbaobao"></use>-->
        <!--</svg>-->
        <!--<span>列表</span>-->
      <!--</span>-->
      <!--<span class="line2"></span>-->
    </div>
    <div class="video_content r">
      <video-player id="my-video" :options="playerOptions"></video-player>
      <video-list v-show="list_switch" :main_list="main_list"></video-list>
    </div>
  </section>
</template>
<style scoped>
  .crumb{
    line-height: 32px;
    height: 32px;
    background-color: #494d58;
    padding-left:10px;
  }
</style>
<script>
  import Vue from 'vue'
  import VueVideo from 'vue-video-player'
  import 'video.js/dist/video-js.css'
  import Crumb from '../../components/00_common/10_crumb'
  import videoList from './13_video_list'
  Vue.use(VueVideo)
  export default {
    name: "my_video",
    data() {
      return {
        list_switch: true,
        playerOptions: {
          // video js options
          muted: true,
          height: '525px',
          width: '850px',
          language: 'en',
          playbackRates: [1.0, 1.25, 1.5, 1.75, 2.0],
          sources: [{
            type: "video/mp4",
            src: "/media/video/180521/fullsizeoutput_89.mov"
          }],
          // fluid: true,
          poster: ""// 海豹图片地址
        },
        video_id: '',
      }
    },
    components: {
      Crumb: Crumb,
      videoList: videoList
    },
    props: {
      main_data: {},
      main_list: {},
    },
    methods: {
    },
    created() {
    }

  }
</script>
<style lang="scss">
  @import "./style/01_customizing_look.css";
</style>
<style lang="scss">
  .icon_menu {

  }

  .section_list {
    margin: 20px 20px 24px;
  }

  .section_list li {
    margin-bottom: 10px;
    text-indent: 20px;
    line-height: 30px;
  }

  .section_list li:hover {
    background-color: #2b2d30;
    cursor: pointer;
  }

  .list_content {
    padding-top: 10px;
    margin-left: 20px;
    height: 100%;
    overflow: hidden;
    background-color: #3c4451;
  }

  .content_list {
    height: 100%;
    width: 300px;
    background-color: #333742;
    right: 0;
    top: 0px;
  }

  .video_title {
    height: 32px;
    overflow: hidden;
    margin-bottom: 16px;
  }

  .video_container {
    padding: 16px 20px 16px 16px;
    box-sizing: border-box;
    height: 600px;
    background-color: #333742;
  }

  .video_content {
    height: 525px;
  }

  .section_title {
    padding-left: 20px;
    line-height: 30px;
  }

  .active {
    background-color: #2b2d30;
  }
</style>
