<template>
  <div class="footer_image"  :style="S" v-lazy:background-image="src">
  </div>
</template>

<script>
  import Vue from 'vue'
  import VueLazyLoader from 'vue-lazyload'

  Vue.use(VueLazyLoader)
  export default {
    name: "footer_image",
    props:{
      src:{},
      S:{}
    }
  }
</script>

<style scoped>
  .footer_image {
    height: 440px;
    background-size: cover;
    background-position: center center;
  }
</style>
