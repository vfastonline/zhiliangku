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
.course_info{
  min-height: 70vh;
}
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
        let totalTime=0
        this.$get("/tracks/course/detail/info?custom_user_id="+custom_user_id+"&course_id="+course_id).then(res => {
          console.log(res.data.data.sections)
            res.data.data.sections.forEach( el => {
              if(el.videos){
                el.videos.forEach(item => {
                    totalTime+= parseInt(this.timeToSecond(item.duration))
                })
                el.duration = this.secondToTime(totalTime)
                totalTime=0
              }
            })
            this.course_detail_lists = res.data.data
        })
      },
      timeToSecond(time) {
        var s = '';
        var hour = time.split(':')[0];
        var min = time.split(':')[1];
        var sec = time.split(':')[2];
        s = Number(hour*3600) + Number(min*60) + Number(sec);
        return s;
      },
      secondToTime(s) {
        var t;
        if(s > -1){
          var hour = Math.floor(s/3600);
          var min = Math.floor(s/60) % 60;
          var sec = s % 60;
          if(hour < 10) {
            t = '0'+ hour + ":";
          } else {
            t = hour + ":";
          }
          if(min < 10){t += "0";}
          t += min + ":";
          if(sec < 10){t += "0";}
          t += sec;
        }
        return t;
      }
    },
    created() {
      this.getMainData()
    }
  }
</script>
