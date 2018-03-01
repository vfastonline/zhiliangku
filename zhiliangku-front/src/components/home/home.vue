<template>
  <div>
    <!-- <carousel></carousel> -->
    <!-- <plant></plant> -->
    <lvsm></lvsm>
    <div class="white">
    <CourseSelect :hometitle="true"></CourseSelect>
    </div>
    <!-- <homeSelectCourse></homeSelectCourse> -->
    <!-- <hcm :mainData="courseData.latestCourse"></hcm> -->
    <!-- <hcm :mainData="courseData.popularCourse" ></hcm> -->
    <!-- <hcm :mainData="courseData.recommendCourse" ></hcm> -->
    <!-- <cpm></cpm> -->
    <!-- <interview-main></interview-main> -->
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
      CourseSelect:CourseSelect
    }
  };

</script>
