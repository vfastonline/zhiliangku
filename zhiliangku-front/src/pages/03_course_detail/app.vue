<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <SubjectInfo :show_id="2" :project_detail_lists="course_detail_lists"></SubjectInfo>
      <div class="mw hc course_info">
        <CourseSection v-for="(item,index) in course_detail_lists.sections" :key="index" :main_data="item"></CourseSection>
      </div>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>

</style>

<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import F from '../../components/01_header_footer/03_footer'
  import SubjectInfo from '../../components/05_project_detail/02_subject_info'
  import CourseSection from '../../components/06_course_detail/01_course_section'

  export default {
    data() {
      return {
        url: "/tracks/course/detail/info",
        params: {},
        course_detail_lists: [],

      }
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      SubjectInfo:SubjectInfo,
      CourseSection:CourseSection,
    },
    methods: {
      getMainData() {
        let custom_user_id = localStorage.getItem('uid')
        let course_id= this.$fn.funcUrl("course_id")||1
        this.$get("/tracks/course/detail/info?custom_user_id="+custom_user_id+"&course_id="+course_id).then(res => {
          console.log(res.data)
            this.course_detail_lists = res.data.data
        })
      }
    },
    created() {
      this.getMainData()
    }
  }
</script>
