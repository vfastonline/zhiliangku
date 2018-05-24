<template>
  <section class="mw hc video_container">
    <div class="video_title ftj">
      <span class="dib font1_18_f">
        <span class="dib ">{{main_data.project}} &gt;</span>
        <span class="dib ">{{main_data.course}} &gt;</span>
        <span class="dib ">{{main_data.section_title}} &gt;</span>
        <span class="dib ">{{main_data.name}} </span>
      </span>
      <!--<span @click="list_switch=!list_switch" class="cp dib font1_18_f pointer ">-->
      <span class="cp dib font1_18_f pointer ">
        <svg class="icon" aria-hidden="true">
          <use xlink:href="#icon-hanbaobao"></use>
        </svg>
        <span>列表</span>
      </span>
      <span class="line2"></span>
    </div>
    <div class="video_content r">
      <video-player id="my-video" :options="playerOptions"></video-player>
      <div v-show="list_switch" class="a content_list ">
        <div ref="section_scroll" class="list_content">
          <div v-for="(item,index) in main_list.sections" :key="index">
            <div class="section_title font1_18_f vm">
              <img class="vm" v-if="item.unlock" src="./img/unlock.png" alt="">
              <img class="vm" v-if="!item.unlock" src="./img/onplay.png" alt="">
              <span class="vm">{{item.title}}</span>
            </div>
            <ul class="section_list">
              <li class="font1_14_f vm" :class="{active: (element.id==video_id) }" @click = "element.unlock && go_video_detail(element)"
                  v-for="(element,index) in item.videos" :key="index">
                <img class="vm" v-if="(element.unlock)&&(element.id==video_id)" src="./img/onplay.png" alt="">
                <img class="vm" v-else-if="!element.unlock" src="./img/Shape.png" alt="">
                <img class="vm" v-else-if="element.unlock" src="./img/unlock.png" alt="">
                <span class="vm">{{element.name}}</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
  import Vue from 'vue'
  import VueVideo from 'vue-video-player'
  import 'video.js/dist/video-js.css'
  import Scrollbar from 'smooth-scrollbar'

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
        isActive: true,
      }
    },
    props: {
      main_data: {},
      main_list: {}
    },
    methods: {
      jj() {
        this.scroll.refresh();
      },
      getPlayId() {
        this.course_id = this.$fn.funcUrl("course_id")
        this.video_id = this.$fn.funcUrl("video_id")
        //假视屏地址
        this.src = "/media/video/180521/fullsizeoutput_89.mov"
      },
      go_video_detail(item) {
        location.href="/tracks/video/detail/?course_id=" + this.course_id +"&video_id="+ item.id
      }
    },
    created() {
      this.getPlayId()
    },
    mounted() {
      //  注意此处要请求数据之后进行操作
      this.scroll = Scrollbar.init(this.$refs.section_scroll)
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
