<template>
  <div class="mw hc note_container rise">
    <div class="ftr"><span class="dib font1_16_6 cp">删除</span></div>
    <p></p>
    <div class="ftr"><span class="dib font2_16_9"></span></div>
  </div>
</template>

<script>
  export default {
    name: "student_notes_li",
    props:{
    }
  }
</script>

<style scoped>
  .note_container {
    padding: 20px 30px 20px 40px;
    box-sizing: border-box;
    margin-bottom: 20px;
    background-color: #fcfcfc;
    min-height: 140px;
  }

  .note_container:hover {
    background-color: #fff;
  }
</style>
