<template>
  <div class="progress_block_title ">
    <span class="font1_26_3  dib title_text">{{main_data.text}}</span>
  </div>
</template>

<script>
  export default {
    name: "progress_block_title",
    data() {
      return {}
    },
    props: {
      main_data: {}
    }
  }
</script>

<style scoped lang="scss">
  @import "../../assets/style/baseConstScss";

  .progress_block_title {
    height: 60px;
    line-height: 60px;
    box-sizing: border-box;
    border-bottom: 2px solid $c9;
    margin-bottom: 40px;
    margin-left: -70px;
  }

  .title_text {
    padding-left: 20px;
    font-weight: 400;
  }
</style>
