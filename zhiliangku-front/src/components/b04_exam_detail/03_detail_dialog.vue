<template>
  <div class="detailInfo__block_main">
    <el-dialog
      class="detailInfo__dialog--note"
      :visible.sync="dialogVisible"
      width="'1200px'"
      :before-close="handleClose">
      <div class="inner_box">
        <left_block></left_block>
        <right_block></right_block>
      </div>
    </el-dialog>
  </div>
</template>

<script>
  import Vue from 'vue'
  import left_block from './04_left'
  import right_block from './05_right'
  import {Dialog} from 'element-ui'
  Vue.use(Dialog)
  export default {
    name: "detail_dialog",
    data() {
      return {
        dialogVisible: true
      }
    },
    components: {
      left_block: left_block,
      right_block:right_block
    }
  }
</script>

<style lang="scss" scoped>
  .detailInfo__block_main {
    .inner_box {
      padding: 70px 0;
      margin: 0 90px;
      display: flex;
      justify-content: space-between;
    }
  }

</style>
<style>
  .detailInfo__dialog--note {
  @import "../b02_exam_statistic/style/01_dialog.scss";
  }
</style>
