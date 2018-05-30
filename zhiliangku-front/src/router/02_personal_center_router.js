// vue路由配置文件
import Vue from 'vue'
import Router from 'vue-router'
import occupational from '../components/11_personal_center/occupational.vue'
import mycourse from '../components/11_personal_center/myCourse.vue'
import myresume from '../components/11_personal_center/myresume.vue'
import mysettings from '../components/11_personal_center/mysettings.vue'
import baseInfo from '../components/11_personal_center/mysettingsBaseInfo.vue'
import bindAccount from '../components/11_personal_center/mysettingsBindAccount.vue'
import password from '../components/11_personal_center/mysettingsPassword.vue'
import address from '../components/11_personal_center/mysettingsAddress.vue'
import matchingrate from '../components/11_personal_center/matchingRate.vue'
import comprehensiveevalution from '../components/11_personal_center/comprehensiveEvaluation.vue'
import focusonme from '../components/11_personal_center/focusOnMe.vue'
import recentlylearning from '../components/11_personal_center/recentlyLearing.vue'
import mycollection from '../components/11_personal_center/myCollectionCourse.vue'
import mypath from '../components/11_personal_center/myPath.vue'
import myVIP from '../components/11_personal_center/43-vip.vue'
import recommondCourse from '../components/11_personal_center/44-recommendCourse.vue'

Vue.use(Router)

export default new Router({
  routes: [{
    path: '/',
    redirect: '/occupational'
  },
    {
      path: '/occupational',
      component: occupational,
      children: [
        {path: '', redirect: '/matchingRate'},
        {path: '/matchingRate', component: matchingrate},
          {path: 'comprehensiveEvalution', component: comprehensiveevalution},
          {path: 'focusOnMe', component: focusonme},
      ]
    },
    {
      path: '/myCourse',
      component: mycourse,
      children: [
        {path: '', redirect: 'recentlyLearing'},
        {path: 'recentlyLearing', component: recentlylearning},
        {path: 'myCollection', component: mycollection},
        {path: 'myPath', component: mypath},
        {path: 'recommondCourse', component: recommondCourse}
      ]
    },
    {
      path: '/myResume',
      component: myresume
    },
    {
      path: '/mySettings',
      component: mysettings,
      children: [
        {path: '', redirect: 'baseInfo'},
        {path: 'baseInfo', component: baseInfo},
        {path: 'bindAccount', component: bindAccount},
        {path: 'password', component: password},
        {path: 'address', component: address}
      ]
    },
    {
      path: '/myVIP',
      component: myVIP,
    },
  ]
})
