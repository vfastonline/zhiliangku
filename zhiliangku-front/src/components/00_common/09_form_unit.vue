<template>
  <!--这是一个伟大的组件，节约了大量的时间，也让以后再实现大量表单的填入和验证的程序员有了较好的心情-->
  <div class="formUnit__container dib">
    <slot name="label"></slot>
    <span class="dib " :style="{'width':main_data.width||'auto'}">
        <el-input v-if="main_data.type===1" v-model="main_data.value"></el-input>
        <el-date-picker
          v-if="main_data.type===2"
          v-model="main_data.value"
          type="date"
          placeholder="选择日期">
        </el-date-picker>
        <el-select
          v-if="main_data.type===3"
          v-model="value" placeholder="请选择">
          <el-option
            v-for="item in main_data.options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
       </el-select>
      </span>
  </div>
</template>

<script>
  import Vue from 'vue'
  import {Option, Select, Input, DatePicker, Form, FormItem} from 'element-ui'

  Vue.use(Option)
  Vue.use(Select)
  Vue.use(Input)
  Vue.use(DatePicker)
  Vue.use(Form)
  Vue.use(FormItem)

  export default {
    name: "form_unit",

    props: {
      main_data: {type: Object, require: true}
    }
  }
</script>
<style lang="scss">
  .formUnit__container {
    .el-select, .el-input, .el-date-editor {
      width: 100% !important;
    }
  }
</style>

