import Vue from 'vue'
import Router from 'vue-router'
import teacher_note from '../components/07_video_detail/02_teacher_note.vue'
import student_note from '../components/07_video_detail/09_student_notes'
import FAQ from '../components/07_video_detail/05_FAQ.vue'
import QA_interaction from '../components/07_video_detail/03_QA_interaction'

Vue.use(Router)
export default new Router({
  routes: [
    {path: '/', redirect: '/teacher_note'},
    {path: '/teacher_note', name: 'teacher_note', component: teacher_note},
    {path: '/student_note', name: 'student_note', component: student_note},
    {path: '/FAQ', name: 'FAQ', component: FAQ},
    {path: '/QA_interaction', name: 'QA_interaction', component: QA_interaction},
  ]
})
