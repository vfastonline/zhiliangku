// vue路由配置文件
import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)
import allProduct from '../components/09-shopping/01-allProduct.vue'
import crl from '../components/09-shopping/04-convertionRecordList.vue'
export default new Router({
  routes: [{
      path: '/',
      redirect: {
        path: '/allProduct',
        query: {
          type: 0
        }
      }
    },
    {
      path: '/allProduct',
      component: allProduct,
      props: {
        type: 0
      }
    },
    {
      path: '/virtualProduct',
      component: allProduct,
      props: {
        type: 2
      }
    },
    {
      path: '/entityProduct',
      component: allProduct,
      props: {
        type: 1
        
      }
    },
    {
      path: '/convertionRecordList',
      component: crl,
    }

  ]
})
