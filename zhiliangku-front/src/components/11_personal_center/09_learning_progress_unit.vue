<template>
  <div class="unit_container rose">
    <div class="img_container">
      <img class="project_img" :src="main_data.pathwel" alt="">
      <div class="bottom_bg"></div>
    </div>
    <div class="block_info r">
      <div class="project_name font1_34_3">{{main_data.name}}</div>
      <div class="progress font1_18_b4">已完成：{{parseInt(main_data.schedule *100) }} %</div>
      <BlueButton class="continue_button a" @click="go_page" ><span class="continue_learn font1_24_f" >继续学习</span></BlueButton>
    </div>
  </div>
</template>

<script>
  import BlueButton from '../00_common/04_blue_button'
  import func from '../../assets/js/01_other/01_dispatch'
  export default {
    name: "learning_progress_unit",
    components:{
      BlueButton:BlueButton
    },
    props: {
      main_data: {},
      timeKey: []
    },
    methods:{
      go_page(){
        let type=this.main_data.learn_video_type
        let course_id=this.main_data.learn_course_id
        let video_id=this.main_data.learn_video_id
        func.goCourse(type,course_id,video_id)
      }
    }
  }
</script>

<style scoped>
  .continue_button{
    bottom: 0;
    left: 0;
  }
  .continue_learn{
    padding: 5px 17px;
  }
  .block_info{
    margin-left: 60px;
    flex: 0 0 auto;
    max-width: 340px;
  }
  .img_container {
    flex: 0 0 auto;
    width: 300px;
  }
  .project_img{
    height: 172px;
    width: 252px;
    margin: auto;
    display: block;
  }
  .bottom_bg{
    display: block;
    height: 10px;
    background-color: #edeef3;
    border-radius: 0 0 20px 20px;
  }
  .unit_container {
    display: flex;
    justify-content: left;
    width: 800px;
    height: 222px;
    padding: 20px 50px;
    box-sizing: border-box;
    border-radius: 10px;
    background-color: white;
  }
</style>
