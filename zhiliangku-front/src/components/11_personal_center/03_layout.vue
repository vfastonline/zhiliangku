<template>
  <div class="mw hc container">
    <div class="left">
      <router-link class="db router_unit" v-for="item in router_data" :key="item.path" :to="item.path" >
        <span class="router_label font1_24_6">{{item.label}}</span>
      </router-link>
    </div>
    <div class="right">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
  export default {
    name: "layout",
    data() {
      return {
        router_data:[
          {label:'基本信息',path:'/base_info'},
          {label:'学习进度',path:'/learning_progress'},
          {label:'我的勋章',path:'/medal'},
          {label:'我的简历',path:'/resume'},
          {label:'账号管理',path:'/account_management'}
        ]
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../assets/style/baseConstScss";
  .router_unit{
    width: 200px;
    height: 60px;
    line-height: 60px;
    margin-bottom: 20px;
    text-align: center;
  }
  .router-link-exact-active{
    background: $cb4;
    .router_label{
      color: white;
    }
  }
  .container {
    min-height: 80vh;
    margin-top: 96px;
    display: flex;
    justify-content: space-between;
  }

  .left {
    width: 290px;
    flex: 0 0 initial;
  }

  .right {
    width: 910px;
    flex: 0 0 initial;
  }
</style>
