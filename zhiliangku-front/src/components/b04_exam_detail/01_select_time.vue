<template>
  <div class="mw hc select_time">
    <el-date-picker
      v-model="value"
      type="daterange"
      range-separator="到"
      start-placeholder="开始日期"
      end-placeholder="结束日期">
    </el-date-picker>
  </div>
</template>

<script>
  import Vue from 'vue'
  import {DatePicker} from 'element-ui'

  Vue.use(DatePicker)
  export default {
    name: "01_select_time",
    data() {
      return {
        value:''
      }
    }
  }
</script>

<style scoped>
.select_time{
  text-align: right;
  margin-top: 30px;
  margin-bottom: 25px;
}
</style>
