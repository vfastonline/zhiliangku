<template>
  <div>
    <el-dialog
      class="set_task_dialog"
      :visible.sync="show_dialog"
      width="'1200px'"
      :before-close="handleClose">
      <task_content></task_content>
    </el-dialog>
  </div>
</template>

<script>
  import Vue from 'vue'
  import {Dialog} from 'element-ui'
  import task_content from './02_set_task'
  import Bus from '../../assets/js/02_bus'


  Vue.use(Dialog)

  export default {
    name: "dialog_index",
    data() {
      return {
        show_dialog: false

      }
    },
    props: {},
    components: {
      task_content: task_content
    },
    created() {
      Bus.$on('close_task_set', () => {
        this.show_dialog = false
      })
      Bus.$on('dialog_open', () => {
        this.show_dialog = true
      })
    }
  }
</script>

<style lang="scss">
  .set_task_dialog {
    .el-dialog__header {
      display: none;
    }
    .el-dialog__body {
      padding: 30px 55px 30px 125px;
    }
  }

</style>
