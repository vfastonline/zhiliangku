<template>
  <div class="footer_image" v-lazy:background-image="src">

  </div>
</template>

<script>
  import Vue from 'vue'
  import VueLazyLoader from 'vue-lazyload'

  Vue.use(VueLazyLoader)
  export default {
    name: "footer_image",
    data() {
      return {
        src:''
      }
    }
  }
</script>

<style scoped>
  .footer_image {
    height: 440px;
  }
</style>
