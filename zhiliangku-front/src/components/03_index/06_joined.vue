<template>
  <section class="join_us" v-lazy:background-image="$myConst.httpUrl+'/media/image/static/index_01_tree_wave.png'">
  </section>
</template>

<script>
  import Vue from 'vue'
  import VueLazyLoader from 'vue-lazyload'
  Vue.use(VueLazyLoader)
  export default {
    name: "joined",
  }
</script>

<style scoped>
  .join_us{
    margin-top: 120px;
    height: 210px;
    padding: 52px 0;
    background-position: center center;
    background-size: cover;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
  }
</style>
