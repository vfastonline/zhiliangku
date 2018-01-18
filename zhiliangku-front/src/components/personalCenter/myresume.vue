<template>
  <div class="mainwidth incenter personnal-center-main clearfix">
    <ul class="floatl personal-center-left">
      <li v-for="(item,index) in anchorarr" :key="index">
        <a href="javascript:void(0)" @click="goAnchor('#anchor'+index)">
          <span class="font14pr3a3c50">{{item}}</span>
          <span class="pcl-triangle"></span>
        </a>
      </li>
    </ul>
    <div class="personal-center-right">
      <rc0 :mainData="mainData.resume" :applyData="mainData.careerobjectives"></rc0>
      <rc1 :mainData="mainData.resume"></rc1>
      <rc2 :mainData="mainData.careerobjectives" ></rc2>
      <rc3 :mainData="mainData.workexperiences"></rc3>
      <rc4 :mainData="mainData.educationexperiences"></rc4>
      <rc5 :mainData="mainData.projectexperiences"></rc5>
    </div>
  </div>
</template>
<script>
  import Bus from '../../assets/js/bus'
  import rc0 from './resumeContent0'
  import rc1 from './resumeContent1'
  import rc2 from './resumeContent2'
  import rc3 from './resumeContent3'
  import rc4 from './resumeContent4'
  import rc5 from './resumeContent5'
  import timer from './timerbox'
  import experience from './personalExperience'
  import myform from './myform'
  export default {
    data() {
      return {
        anchorarr: ['个人信息', '我的优势', '求职意向', '工作经历',  '教育经历','项目经验'],
        mainData: {
          resume: {
            "status": "在职",
            "name": "许慧良",
            "advantage": "认真踏实",
            "expect_salary_high": 2,
            "sex": "男",
            "custom_user_id": 31,
            "avatar": "sss",
            "expect_salary_low": 1,
            "id": 1,
            "position": "Python开发工程师",
            "education": "大专",
            "company": "智量酷",
            "years_of_service": "4"
          },
          "projectexperiences": [{
            "name": "质量路1",
            "url": "www.zhiliangku.com",
            "start_time": "2017-11-2",
            "custom_user_id": 31,
            "role": "后台工程",
            "end_time": "至今",
            "id": 1,
            "description": "为学生网上学习使用。"
          }],
          "educationexperiences": [{
            "discipline": "摄影",
            "school": "中国环境管理干部学院",
            "start_time": "2013",
            "experience": "没敢什么事。",
            "custom_user_id": 31,
            "end_time": "至今",
            "education": "大专",
            "id": 1
          }],
          "age": 27,
          "workexperiences": [{
            "company": "智量酷",
            "id": 1,
            "content": "主要对智量酷网站做开发。",
            "custom_user_id": 31,
            "end_time": "至今",
            "position": "Python开发工程师",
            "start_time": "2017-11-2"
          }],
          "careerobjectives": [{
            "city": "深圳",
            "expect_salary_low": 1,
            "expect_salary_high": 2,
            "industry": "教育",
            "custom_user_id": 31,
            "position": "前端开发",
            "id": 1
          }],
          "career_objective_id": 1
        }
      }
    },
    methods: {
      goAnchor(selector) {
        var anchor = document.querySelector(selector);
        window.scrollTo(0, anchor.offsetTop+470)
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
      rc5,
      rc5,
      timer: timer,
      experience: experience,
      myform: myform,
    }
  }

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang='scss'>
  .personal-c\enter-left {
    width: 210px;
  }

  .personal-center-left li {
    text-align: right;
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
  @import "../../style/scss/components/personalCenter.scss";
  @import "../../style/scss/components/resume.scss";

</style>
<style scoped>


</style>
