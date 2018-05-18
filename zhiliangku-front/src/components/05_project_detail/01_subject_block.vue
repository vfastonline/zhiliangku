<template>
  <section class="subject_block rose">
    <p class="subject_name  ftc font1_20_f">{{main_data.name}}</p>
    <p class="subject_introduce font1_16_6">{{main_data.desc}}</p>
    <ul class="subject_info">
      <li class="subject_info_li_1">{{main_data.summary.desc}}</li>
      <li class="font1_18_9 subject_info_li_1"><span>时长：</span><span class="dib subject_time_value">{{main_data.summary.total_time}}</span>
        <span>完成</span><span>{{main_data.summary.video_process}}</span>
      </li>
      <li class="subject_info_li_2">
        <span class="dib">
          <img :src="main_data.avatar" class="user_icon vm" alt="">
          <span class="dib vbo font1_18_6">{{main_data.lecturer}}</span></span>
        <a :href="link">
          <span>
            <a :href="link">
              <BlueButton v-if="(main_data.summary.schedule!=1)&&(main_data.summary.unlock)" class="func_button">继续学习</BlueButton>
            </a>
            <img v-if="!main_data.summary.unlock" src="./img/Shape.png" alt="">
            <img v-if="(main_data.summary.schedule===1)&&(main_data.summary.unlock)" src="./img/finish_icon.png" alt="">
          </span>
        </a>
        <span class="line2"></span></li>
    </ul>
  </section>
</template>
<style>
  .subject_introduce {
    padding: 20px 20px 0px 20px;
    margin-bottom: 10px;
    max-height: 72px;
    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    text-overflow: ellipsis;
  }

  .func_button {
    vertical-align: bottom;
  }
</style>
<script>
  import BlueButton from '../../components/00_common/04_blue_button'

  export default {
    name: "subject_block",
    data() {
      return {
        summary: {},
        link: ''
      }
    },
    props: {
      main_data: {}
    },
    components: {
      BlueButton: BlueButton
    },
    methods: {
      goLink(){
        this.link = "/tracks/course/detail/index.html?course_id="+this.main_data.id
      }
    },
    created() {
      var key = this.main_data.summary.schedule
      if (!key) {
        this.main_data.summary.schedule = 0
      }
      console.log(key)
      this.goLink()
    }
  }
</script>

<style scoped lang="scss">
  .subject_block {
    width: 380px;
    -webkit-border-radius: 10px;
    -moz-border-radius: 10px;
    border-radius: 10px;
    overflow: hidden;
  }

  .subject_name {
    height: 60px;
    line-height: 60px;
    background-color: rgba(122, 155, 89, 0.3);
  }

  .subject_info {
    height: 110px;
    padding: 10px 20px 10px 20px;
  }

  .subject_time_value {
    margin-righr: 32px;
  }

  .user_icon {
    height: 60px;
    width: 60px;
    border-radius: 60px;
    margin-right: 10px;
  }

  .subject_info_li_1 {
    margin-bottom: 14px;
  }

  .subject_info_li_2 {
    text-align: justify;
  }

  .line2 {
    display: inline-block;
    width: 100%;
  }
</style>
