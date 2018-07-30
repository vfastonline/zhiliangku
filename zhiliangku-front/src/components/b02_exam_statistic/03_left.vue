<template>
  <div class="tag_container">
    <div v-for="item in [1,2,3,4]" :key="item" class="tag rose">
      <div class="ftc font1_16_6">日考核</div>
      <div class="ftc">
        <span class="font1_22_3 count">30</span>
        <span class="font1_14_9">次</span>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "03_left"
  }
</script>

<style scoped>
  .tag_container {
    width: 110px;
  }

  .tag {
    background-color: white;
    height: 80px;
    border-radius: 10px;
    margin-bottom: 12px;
    box-sizing: border-box;
    padding: 4px 0 6px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
  }
  .count{
    letter-spacing: 2px;
    font-weight: 600;
  }
</style>
