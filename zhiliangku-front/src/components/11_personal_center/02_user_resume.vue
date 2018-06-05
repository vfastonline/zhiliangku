<template>
  <div class=" hc personnal-center-main clearfix">
    <div class="personal-center-right">
      <rc0 :mainData="mainData.resume" :applyData="mainData.careerobjectives"></rc0>
      <rc1 :mainData="mainData.resume"></rc1>
      <rc2 :mainData="mainData.careerobjectives"></rc2>
      <rc3 :mainData="mainData.workexperiences"></rc3>
      <rc5 :mainData="mainData.projectexperiences"></rc5>
      <rc4 :mainData="mainData.educationexperiences"></rc4>
    </div>
  </div>
</template>
<script>
  import Bus from '../../assets/js/02_bus'
  import rc0 from './07_resume_content_0_display'
  import rc1 from './07_resume_content_1_display'
  import rc2 from './07_resume_content_2_display'
  import rc3 from './07_resume_content_3_display'
  import rc4 from './07_resume_content_4_diplay'
  import rc5 from './07_resume_content_5_display'
  import timer from './timerbox'
  import experience from './personalExperience'
  import myform from './myform'
  import {Button} from 'element-ui'
  import Vue from 'vue'
  Vue.use(Button)
  export default {
    data() {
      return {
        anchorarr: ['个人信息', '我的优势', '求职意向', '工作经历', '教育经历', '项目经验'],
        mainData: {
          resume: {

          },
          "projectexperiences": [{

          }],
          "educationexperiences": [{

          }],
          "age": 27,
          "workexperiences": [{

          }],
          "careerobjectives": [{

          }],
          "career_objective_id": 1
        },
        activeIndex: 0
      }
    },
    methods: {
      getData() {
        this.$get('/personal_center/resume/detail/info?custom_user_id=' + localStorage.uid).then(res => {
          this.mainData = res.data.data;
          console.log(res)
        })
      }
    },
    created() {
      this.getData();
      Bus.$on('refreshResume', res => {
        this.mainData = res
      })
    },
    components: {
      rc0: rc0,
      rc1: rc1,
      rc2: rc2,
      rc3: rc3,
      rc4: rc4,
      rc5:rc5,
      timer: timer,
      experience: experience,
      myform: myform,
    }
  }
</script>
<style lang='scss'>
  .resume-model{
    margin-bottom: 85px;
  }
  .personnal-center-main{
    display: flex;
    justify-content: space-between;
  }
  .personal-center-left {
    width: 292px;
  }
  .personal-center-right{
    width:900px;
  }
  .personal-center-left li {
    margin-bottom: 64px;
  }

  .personal-center-left .router-link-active {
    color: #23B8FF;
  }

  .personal-center-left .router-link-active .pcl-triangle {
    border-left-color: #23B8FF;
  }

</style>
<style lang="scss">
  /*@import "./style/02_personal_center.scss";*/
  /*@import "./style/03_resume.scss";*/

</style>
<style scoped>


</style>
