<template>
  <div class="bdr">
    <el-dialog
      class="add_exam_dialog "
      :visible.sync="show_dialog"
      width="880px"
    >
      <div class="addExam_title_title font1_26_f ">添加考试</div>
      <div class="hc form_container ftj">
        <form_unit class="form_unit_container" :main_data="form_data.name">
          <span slot="label" class="font1_20_6 label">考试名称</span>
        </form_unit>
        <form_unit class="form_unit_container" :main_data="form_data.time">
          <span slot="label" class="font1_20_6 label">考试时间</span>
        </form_unit>
        <form_unit class="form_unit_container" :main_data="form_data.type">
          <span slot="label" class="font1_20_6 label">考试性质</span>
        </form_unit>
        <form_unit class="form_unit_container" :main_data="form_data.way">
          <span slot="label" class="font1_20_6 label">考试方式</span>
        </form_unit>
        <form_unit class="form_unit_container" :main_data="form_data.num">
          <span slot="label" class="font1_20_6 label">考试人数</span>
        </form_unit>
      </div>
      <div slot="footer" class="ftc">
        <BlueButton><span class="font1_20_f addExam__button--submit">提交</span></BlueButton>
      </div>
    </el-dialog>
  </div>
</template>

<script>
  import BlueButton from '../../components/00_common/04_blue_button'
  import Vue from 'vue'
  import {Dialog, Button} from 'element-ui'
  import form_unit from '../00_common/09_form_unit'

  Vue.use(Dialog)
  Vue.use(Button)
  export default {
    name: "add_exam",
    data() {
      return {
        show_dialog: true,
        form_data: {
          name: {
            type: 1,
            value: '',
            width: '590px',
          },
          time: {
            type: 3,
            value: '',
            width: '200px'
          },
          type: {
            type: 2,
            value: '',
            width: '200px'
          },
          way: {
            type: 2,
            value: '',
            width: '200px'
          },
          num: {
            type: 1,
            value: '',
            width: '200px'
          }
        }
      }
    },
    components: {
      form_unit: form_unit,
      BlueButton: BlueButton
    }
  }
</script>
<style scoped lang="scss">
  @import "../../assets/style/baseConstScss";

  @mixin flex {
    display: flex;
    justify-content: space-between;
  }

  .addExam__button--submit {
    padding: 2px 28px;
  }

  .addExam_title_title {
    height: 50px;
    line-height: 50px;
    background-color: $cp;
    padding-left: 30px;
    border-radius: 10px 10px 0 0;
    margin-bottom: 40px;
  }

  .label {
    margin-right: 14px;
  }

  .form_container {
    width: 690px;
    margin-bottom: 38px;
  }

  .form_unit_container {
    margin-bottom: 20px;
  }
</style>
<style lang="scss">
  .add_exam_dialog {
    @import "./style/01_dialog";
  }

</style>
