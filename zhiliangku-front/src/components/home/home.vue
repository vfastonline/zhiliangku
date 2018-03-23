<template>
  <div>
    <!-- <carousel></carousel> -->
    <!-- <plant></plant> -->
    <homeimg></homeimg>
    <lvsm></lvsm>
    <div class="white">
    <CourseSelect :hometitle="true"></CourseSelect>
    </div>
    <!-- <homeSelectCourse></homeSelectCourse> -->
    <!-- <hcm :mainData="courseData.latestCourse"></hcm> -->
    <!-- <hcm :mainData="courseData.popularCourse" ></hcm> -->
    <!-- <hcm :mainData="courseData.recommendCourse" ></hcm> -->
    <!-- <cpm></cpm> -->
    <interviewMainVue></interviewMainVue>
    <cooperator></cooperator>
  </div>
</template>
<style>
.white{
  background-color: white;
}

</style>
<script>
import CourseSelect from '../courseInfo/courseSelect'
import homeSelectCourse from './18-homeSelectCourse'
import homeimg from './19-home-img'
import interviewMainVue from './interviewMain.vue';
  export default {
    name: "home",
    data() {
      return {
        courseData: {
          latestCourse: {
            msg: {
              enTitle: 'new Course',
              title: '最新课程',
              slogon: '优质课程，免费学习',
              linker: '/tracks/course/list/'
            },
            type: 'latest'
          },
          popularCourse: {
            msg: {
              enTitle: 'Top Course',
              title: '热门课程',
              slogon: '优质课程，免费学习',
              linker: '/tracks/course/list/'
            },
            type: 'popular'
          },
         recommendCourse: {
            msg: {
              enTitle: 'feature Course',
              title: '推荐课程',
              slogon: '优质课程，免费学习',
              linker: '/tracks/course/list/'
            },
            type: 'recommend'
          },
        }
      };
    },
    components:{
      homeSelectCourse:homeSelectCourse,
      CourseSelect:CourseSelect,
      homeimg:homeimg,
      interviewMainVue:interviewMainVue
    }
  };

</script>
