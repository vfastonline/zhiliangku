<template>
  <h1 :style="S" class="introduce_title font1_40_3 ftc" v-text="title"></h1>
</template>

<script>
  export default {
    name: "introduce_title",
    props: {
      S: Object,
      title: {
        type: String,
        // require:true,
        default:' :text 方式传入标题'
      }
    }
  }
</script>

<style scoped>
  .introduce_title {
    margin: 100px 0 60px;
  }
</style>
