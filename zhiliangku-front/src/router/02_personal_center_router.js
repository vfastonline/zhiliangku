import Vue from 'vue'
import Router from 'vue-router'
import base_info from '../components/11_personal_center/04_base_info'
import medal from '../components/11_personal_center/05_medal'
import learning_progress from '../components/11_personal_center/06_learning_progress'
import resume from '../components/11_personal_center/02_user_resume'
Vue.use(Router)
let router=new Router({
  routes:[
    {path:'/',redirect:'/base_info'},
    {path:'/base_info',name:'base_info',component:base_info},
    {path:'learning_progress',name:'learning_progress',component:learning_progress},
    {path:'/medal',name:'medal',component:medal},
    {path:'/resume',name:'resume',component:resume}
  ]
})
export default router
