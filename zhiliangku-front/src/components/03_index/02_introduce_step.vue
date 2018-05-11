<template>
  <div class="introduce_step">
    <img src="./img/achievement.png" alt="">
    <h3 class="step_title ftc font1_32_6">理解</h3>
    <p class="step_text font1_18_9">
      这个世界上有一个传说那就是这个世界上有个传说，有一个神奇的双手，造出了形形色色的声明。
    </p>
  </div>
</template>

<script>
  export default {
    name: "introduce_step",
    data() {
      return {}
    },
    props: {
      stepData: Object
    }
  }
</script>

<style scoped>
  .introduce_step {
    height: 456px;
  }

  .step_title {
    margin: 30px 0 20px 0;
  }

  .step_text {
    padding: 20px;
  }
</style>
