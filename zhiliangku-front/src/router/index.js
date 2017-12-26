// vue路由配置文件
import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

import Home from '../components/home/home.vue'
export default new Router({
  routes: [
    {path: '/',name: 'home',components:{'a':Home}}
  ]
})
