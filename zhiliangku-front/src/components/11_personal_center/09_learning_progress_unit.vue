<template>
  <div class="lear_unit_container rise">
    <div class="unit_top">
      <div class="font1_30_3 item_title">项目名称：{{main_data.name}}</div>
      <div class="font1_24_9" :title="main_data.learning">任务解锁：{{main_data.learning}}</div>
    </div>
    <div class="section_container">
      <div class="img_container">
        <img class="project_img" :src="main_data.pathwel" alt="">
        <div class="bottom_bg"></div>
      </div>
      <div class="block_info">
        <BlueButton class="continue_button blue_button " @click="go_page"><span class="continue_learn_blue font1_24_f">继续学习</span>
        </BlueButton>
        <!--<GreyButton class="continue_button  grey_button" @click="go_unlock"><span-->
          <!--class="continue_learn_grey font1_24_f">继续学习</span>-->
        <!--</GreyButton>-->
      </div>
    </div>
    <el-progress  :text-inside="true" :stroke-width="27"  color="#00bcd5" :percentage="main_data.schedule|fixed"></el-progress>
  </div>
</template>

<script>
  import BlueButton from '../00_common/04_blue_button'
  import GreyButton from '../00_common/02_grey_button'
  import func from '../../assets/js/01_other/01_dispatch'
  import {Progress} from 'element-ui'
  import Vue from 'vue'

  Vue.use(Progress)
  export default {
    name: "learning_progress_unit",
    components: {
      BlueButton: BlueButton,
      GreyButton: GreyButton
    },
    props: {
      main_data: {},
      timeKey: []
    },
    filters:{
      fixed(value){
        return (value*100).toFixed(2)
      }
    },
    methods: {
      go_page() {
        let type = this.main_data.learn_video_type
        let course_id = this.main_data.learn_course_id
        let video_id = this.main_data.learn_video_id
        func.goCourse(type, course_id, video_id)
      },
      go_unlock() {
        this.$notify({
          type: 'warning',
          message: '课程尚未解锁',
          offset: 100,
          duration: 3000,
          position: 'bottom-right'
        })
      }
    }
  }
</script>

<style lang="scss">
  .lear_unit_container {
    .el-progress-bar__outer {
      background-color: #b2ebf2;
    }
  }
</style>
<style scoped>
  .lear_unit_container{
    border-radius: 10px;
    padding-top: 22px;
    background-color: white;
  }
  .unit_top{
    margin-bottom: 25px;
    padding-left: 30px;
  }
  .item_title {
    font-weight: 400;
  }

  .continue_button {
    bottom: 0;
    left: 0;
  }

  .blue_button {
    height: 60px;
  }

  .grey_button {
    height: 60px;
  }

  .continue_learn_blue {
    padding: 10px 40px;
  }

  .continue_learn_grey {
    padding: 10px 0;
  }

  .block_info {
    flex: 0 0 auto;
    margin-bottom: 30px;
  }

  .img_container {
    flex: 0 0 auto;
    width: 300px;
  }

  .project_img {
    height: 172px;
    width: 252px;
    margin: auto;
    display: block;
  }

  .bottom_bg {
    display: block;
    height: 10px;
    background-color: #edeef3;
    border-radius: 0 0 20px 20px;
  }

  .section_container {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    width: 800px;
    height: 222px;
    padding: 20px 30px;
    box-sizing: border-box;
  }
</style>
