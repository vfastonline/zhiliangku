<template>
  <section class="mw hc student_note">
    <div class="student_note_content">
      <NoteLi v-for="(item,index) in student_note_datas" :key="index" :noteData="item"></NoteLi>
    </div>
    <Pager @pagerGetData="mainPagerData" :url="url" :addition-data="params"></Pager>
  </section>
</template>

<script>
  import NoteLi from './10_student_notes_unit'
  import Pager from '../00_common/06_pager'

  export default {
    name: "student_notes",
    data() {
      return {
        main_data: '',
        student_note_datas: '',
        url: '/tracks/student/notes/list/info',
        params: ''
      }
    },
    components: {
      NoteLi: NoteLi,
      Pager: Pager
    },
    methods: {
      mainPagerData(res) {
        console.log(res.data.data)
        this.student_note_datas = res.data.data
      }
    },
    created() {
      let video_id = this.$fn.funcUrl('video_id')
      this.params = {
        'custom_user_id': localStorage.uid,
        'video_id': video_id
      }
    },

  }
</script>

<style scoped>
  .student_note {
    min-height: 70vh;
    margin-bottom: 30px;
  }

  .student_note_content {
    min-height: 64vh;
  }
</style>
