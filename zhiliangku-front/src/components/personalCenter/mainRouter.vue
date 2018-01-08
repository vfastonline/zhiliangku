<template>
<div class="mainRouter-container">
    <div class="mainwidth incenter">
      <div class="persona-center-navbar">
        <router-link   :to="{path:'/occupational'}" class="font16pr3a3c50 pointer vc-nav-tag">职业信息</router-link>
        <router-link   :to="{path:'/myCourse'}" class="font16pr3a3c50 pointer vc-nav-tag">我的课程</router-link>
        <router-link   :to="{path:'/myResume'}" class="font16pr3a3c50 pointer vc-nav-tag">我的简历</router-link>
        <router-link   :to="{path:'/mySettings'}" class="font16pr3a3c50 pointer vc-nav-tag">个人设置</router-link>
      </div>
      <router-view ></router-view>
    </div>
</div>
</template>
<style  scoped>
.mainRouter-container{
  background: #fafafa;
}
.persona-center-navbar{
  height:70px;
  line-height:70px;
  box-sizing: border-box;
  display:flex;
  justify-content: space-between;
  padding:0 140px;
}
.persona-center-navbar .router-link-active{
  color:#23B8FF;
}
</style>
<script>
import '../../router/personalCenterRouter'
  import Bus from '../../assets/js/bus'
  export default {
    data() {
      return {

      }
    },
    props:{
    },
    methods: {
      jj() {
        console.log(111)
      }
    },
    components: {},
    methods: {},
    created() {}
  }

</script>

