<template>
  <div class="course_section_container">
    <div class="course_section ftj">
      <span class="fl">
          <img v-if="main_data.unlock" class="vm first_icon " src="./img/player.png" alt="">
          <img v-if="!main_data.unlock" class="vm first_icon " src="./img/lock.png" alt="">
      </span>
      <span class="dib ftj section_name fr">
          <span class="dib font1_22_3 lesson_name fl">{{main_data.title}}</span>
          <span class="dib font1_16_9 lesson_info fr">
            <span class="dib timer">总时长：{{main_data.duration}}</span>
            <span class="dib progress">{{main_data.is_complete?"完成":"未完成"}}</span></span>
      </span>
    </div>
    <ul>
      <li class="section_li" @click="item.unlock&&go_video_detail(item)" v-for="(item, index) in main_data.videos" :key="index">
        <span class="fl">
          <img v-if="item.unlock" class="vm first_icon " src="./img/player.png" alt="">
          <img v-if="!item.unlock" class="vm first_icon " src="./img/lock.png" alt="">
        </span>
        <span class="dib ftj lesson_child fr">
          <span class="dib font1_18_3 lesson_name fl">{{item.name}}</span>
          <span class="dib font1_16_9 lesson_info fr">
            <span class="dib timer" :total_time="item.duration">时长：{{item.duration}}</span>
            <span class="dib progress">{{item.is_complete?"完成":"未完成"}}</span>
          </span>
      </span>
      </li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: "course_section",
    data(){
      return {
        total_time: ''
      }
    },
    props: {
      main_data: {
        required: true
      },
      videos: []
    },
    methods: {
      go_video_detail(item){
        let course_id = this.$fn.funcUrl("course_id")
        window.open("/tracks/video/detail?course_id=" +course_id + "&video_id="+item.id)
      }
    },
    created() {
    },
    mounted() {
    }

  }
</script>

<style scoped>
  .course_section_container {
    margin-left: 110px;
    width: 990px;
    margin-bottom:20px;
  }
  .course_section {
    font-weight:700;
  }

  .first_icon {

  }

  .course_section {
    width: 990px;
    margin-bottom: 20px;
    height: 40px;
    line-height: 40px;
  }

  .section_name {
    /*margin-bottom: 20px;*/
    height: 100%;
    width: 950px;
    background-color:#eee;
  }

  .lesson_info {
    margin-right: 53px;
  }

  .lesson_name {
    margin-left: 10px;
  }

  .lesson_child {
    width: 890px;
  }

  .section_li {
    width: 940px;
    margin-left: 50px;
    line-height: 30px;
    height: 30px;
    cursor: pointer;
  }

  .section_li:hover .lesson_child {
    background-color: #eeeeee;
  }

  .first_icon {

  }

  .timer {
    margin-right: 20px;
  }
</style>
