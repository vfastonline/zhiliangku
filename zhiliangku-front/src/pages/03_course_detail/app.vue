<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <SubjectInfo :show_id="2"></SubjectInfo>
      <div class="mw hc course_info">
        <CourseSection ></CourseSection>
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
      return {}
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      SubjectInfo:SubjectInfo,
      CourseSection:CourseSection
    }
  }
</script>
