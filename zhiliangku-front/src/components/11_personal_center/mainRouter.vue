<template>
  <div class="mainRouter-container  r">
    <div class="mw hc  mynav ">
      <div class="persona-center-navbar rose">
        <router-link v-for="(item,index) in routerInfo" :key="index" :to="item.to " >{{item.name}}</router-link>
      </div>
    </div>
    <div style="height:1px;"></div>
    <router-view></router-view>
  </div>
</template>
<style scoped>
  .mainRouter-container {
    background: #fafafa;
  }

  .mynav {
    position: absolute;
    left: 50%;
    top: -35px;
    transform: translate(-50%, 0)
  }

  .persona-center-navbar {
    height: 70px;
    line-height: 70px;
    box-sizing: border-box;
    display: flex;
    justify-content: space-between;
    padding: 0 140px;
    background: white;
  }

  .persona-center-navbar .router-link-active {
    color: #23B8FF;
  }

</style>
<script>

  export default {
    data() {
      return {

      }
    },
    props: {routerInfo:Array,refresh:Boolean},
    methods: {
    },
    components: {},
    created() {
    }
  }

</script>
