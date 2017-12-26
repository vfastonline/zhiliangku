import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)
import node from '../components/videoDetail/node.vue'
import qa from '../components/videoDetail/questionAndAnswer.vue'
import sa from '../components/videoDetail/sectionFrequentlyQuestion.vue'

export default new Router({
  routes: [
    {path: '/',name: 'node',components:{'videoContent':node}},
    {path: '/question',name: 'question',components:{'videoContent':qa}},
    {path: '/section',name: 'section',components:{'videoContent':sa}}
  ]
})