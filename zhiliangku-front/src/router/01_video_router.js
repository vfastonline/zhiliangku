import Vue from 'vue'
import Router from 'vue-router'
import note from '../components/07_video_detail/02_teacher_note.vue'
import qa from '../components/07_video_detail/03_question_answer.vue'
import sa from '../components/07_video_detail/05_FAQ.vue'
import question from '../components/07_video_detail/07_submit_question.vue'

Vue.use(Router)
export default new Router({
  routes: [
    {path: '/', redirect: '/note'},
    {path: '/note', name: 'note', components: {'videoContent': note}},
    {path: '/question', name: 'question', components: {'videoContent': qa}},
    {path: '/section', name: 'section', components: {'videoContent': sa}},
    {path: '/submitQuestion', name: 'submitQuestion', components: {'videoContent': question}},
  ]
})
