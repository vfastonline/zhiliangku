<template>
  <div class="mw hc personnal-center-main clearfix">
    <ul class="fl personal-center-left">

    </ul>
    <div class="personal-center-right">
      <rc0 :mainData="mainData.resume" :applyData="mainData.careerobjectives"></rc0>
      <rc1 :mainData="mainData.resume"></rc1>
      <rc2 :mainData="mainData.careerobjectives"></rc2>
      <rc3 :mainData="mainData.workexperiences"></rc3>
      <rc4 :mainData="mainData.educationexperiences"></rc4>
      <rc5 :mainData="mainData.projectexperiences"></rc5>
    </div>
  </div>
</template>
<script>
  import Bus from '../../assets/js/02_bus'
  import rc0 from './resumeContent0'
  import rc1 from './resumeContent1'
  import rc2 from './resumeContent2'
  import rc3 from './resumeContent3'
  import rc4 from './resumeContent4'
  import rc5 from './resumeContent5'
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
      sendResume() {
        this.$notify({
          type: 'info',
          message: '简历已投递，请留意邮箱消息',
          offset: 100,
          duration: 3000,
          position: 'bottom-right'
        });
      },
      goAnchor(selector, index) {
        this.activeIndex = index;
        var anchor = document.querySelector(selector);
        window.scrollTo(0, anchor.offsetTop + 470)
        //这里可以计算两者的差值并计算传参
      },
      inputfunc(evt) {
        console.log(evt)
      },
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
  .personnal-center-main{
    display: flex;
    justify-content: space-between;
    margin-top:96px
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
  @import "./style/02_personal_center.scss";
  @import "./style/03_resume.scss";

</style>
<style scoped>


</style>
