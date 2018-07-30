<template>
  <div class="editorBlock__section mw hc">
    <title_tag :text="'录入成绩'">
      <img src="./img/01_editor.png" alt="">
    </title_tag>
    <div class="rose editorBlock__section--table">
      <div class="column_01 ftc">
        <div class="th row_01 font1_24_3">姓名</div>
      </div>
      <div class="column_02">
        <div class="th row_01 font1_24_3">姓名</div>
      </div>
      <div class="column_03">
        <div class="th row_01 font1_24_3">姓名</div>
      </div>
    </div>
  </div>
</template>

<script>
  import title_tag from './02_title_tag'

  export default {
    name: "editor",
    components: {
      title_tag: title_tag
    }
  }
</script>

<style lang="scss" scoped>
  .editorBlock__section {
    margin-top: 60px;
    &--table {
      padding: 35px 200px 25px 70px;
      display: flex;
      justify-content: space-between;
    }
    .column_01{
      width: 140px;
    }
    .column_02{
      width: 142px;
    }
    .column_01{
      width: 660px;
    }
  }
</style>
