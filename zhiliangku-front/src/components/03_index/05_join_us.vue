<template>
  <section class="join_us" v-lazy:background-image="$myConst.httpUrl+'/media/image/static/index_02_wave.png'">
    <a href="#">
      <WhiteButton>加入我们</WhiteButton>
    </a>
    <a href="#">
      <WhiteButton>用户手册</WhiteButton>
    </a>
  </section>
</template>

<script>
  import WhiteButton from '../../components/00_common/03_white_button'
  import Vue from 'vue'
  Vue.use(window.VueLazyload)
  export default {
    name: "join_us",
    components: {
      WhiteButton: WhiteButton
    }
  }
</script>

<style scoped>
  .join_us {
    margin-top: 160px;
    height: 170px;
    padding: 52px 0;
    background-position: center center;
    background-size: cover;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
  }
</style>
