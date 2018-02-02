// vue路由配置文件
import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)
import occupational from '../components/personalCenter/occupational.vue'
import test from '../components/personalCenter/test.vue'
import mycourse from '../components/personalCenter/myCourse.vue'
import myresume from '../components/personalCenter/myresume.vue'
import mysettings from '../components/personalCenter/mysettings.vue'
import baseInfo from '../components/personalCenter/mysettingsBaseInfo.vue'
import bindAccount from '../components/personalCenter/mysettingsBindAccount.vue'
import password from '../components/personalCenter/mysettingsPassword.vue'
import address from '../components/personalCenter/mysettingsAddress.vue'
import matchingrate from '../components/personalCenter/matchingRate.vue'
// import comprehensiveevalution from '../components/personalCenter/comprehensiveEvaluation.vue'
import focusonme from '../components/personalCenter/focusOnMe.vue'
import recentlylearning from '../components/personalCenter/recentlyLearing.vue'
import mycollection from '../components/personalCenter/myCollectionCourse.vue'
import mypath from '../components/personalCenter/myPath.vue'
import myVIP from '../components/personalCenter/43-vip.vue'
export default new Router({
  routes: [{
      path: '/',
      redirect: '/occupational'
    },
    {
      path: '/occupational',
      component: occupational,
      children:[
        {path:'',redirect:'matchingRate'},
        {path:'matchingRate',component:matchingrate},
        // {path:'comprehensiveEvalution',component:comprehensiveevalution},
        {path:'focusOnMe',component:focusonme},
      ]
    },
    {
      path:'/myCourse',
      component:mycourse,
      children:[
        {path:'',redirect:'recentlyLearing'},
        {path:'recentlyLearing',component:recentlylearning},
        {path:'myCollection',component:mycollection},
        {path:'myPath',component:mypath}
      ]
    },
    {
      path:'/myResume',
      component:myresume
    },
    {
      path:'/mySettings',
      component:mysettings,
      children:[
        {path:'',redirect:'baseInfo'},
        {path:'baseInfo',component:baseInfo},
        {path:'bindAccount',component:bindAccount},
        {path:'password',component:password},
        {path:'address',component:address}
      ]
    },
    {
      path:'/myVIP',
      component:myVIP,
    },
  ]
})
