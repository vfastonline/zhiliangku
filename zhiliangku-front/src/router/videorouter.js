import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)
import note from '../components/videoDetail/node.vue'
import qa from '../components/videoDetail/questionAndAnswer.vue'
import sa from '../components/videoDetail/sectionFrequentlyQuestion.vue'
import question from '../components/videoDetail/submitQuestion.vue'

export default new Router({
  routes: [
    {path:'/',redirect:'/note'},
    {path: '/note',name: 'note',components:{'videoContent':note}},
    {path: '/question',name: 'question',components:{'videoContent':qa}},
    {path: '/section',name: 'section',components:{'videoContent':sa}},
    {path: '/submitQuestion',name: 'submitQuestion',components:{'videoContent':question}},
  ]
})