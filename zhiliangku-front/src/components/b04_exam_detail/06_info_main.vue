<template>
  <div>
    <div class="infoUnit__li border_b">
      <span class="dib font1_18_3">姓名</span>
      <span class="dib font1_18_b4 weight">20</span>
    </div>
    <div class="infoUnit__li border_b">
      <span class="dib font1_18_3">姓名</span>
      <span class="dib font1_18_b4 weight">20</span>
    </div>
    <div class="infoUnit__li border_b">
      <span class="dib font1_18_3">姓名</span>
      <span class="dib font1_18_b4 weight">20</span>
    </div>
    <div class="infoUnit__li border_b">
      <span class="dib font1_18_3">姓名</span>
      <span class="dib font1_18_b4 weight">20</span>
    </div>
  </div>
</template>

<script>
  export default {
    name: "info_unit",

  }
</script>

<style scoped>
  .infoUnit__li {
    height: 38px;
    line-height: 38px;
    display: flex;
    justify-content: space-between;
    text-align: center;
  }

  .border_b {
    border-bottom: 1px solid #999;
  }
</style>
