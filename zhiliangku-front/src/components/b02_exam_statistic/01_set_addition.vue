<template>
  <div class="mw hc addition_container">
    <el-select class="type_select" v-model="type" placeholder="请选择">
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>
    <span class="r">
      <el-input class="key_word" v-model="key_word" placeholder="请输入考试名称">
      </el-input>
      <span class="search_icon cp dib">
        <img class=" hc vm" src="./img/01_search.png" alt="">
      </span>
    </span>
    <el-date-picker
      class="date_picker"
      v-model="time_range"
      type="daterange"
      range-separator="到"
      start-placeholder="开始日期"
      end-placeholder="结束日期">
    </el-date-picker>
    <span>
      <BlueButton><span class="button_text">查看报表</span></BlueButton>
      <BlueButton><span class="button_text">添加考试</span></BlueButton>
    </span>
    <add_exam></add_exam>
  </div>
</template>

<script>
  import Vue from 'vue'
  import BlueButton from '../00_common/04_blue_button'
  import {Option, Input, DatePicker, Select} from 'element-ui'
  import add_exam from './05_add_exam'

  Vue.use(Select)
  Vue.use(Option)
  Vue.use(Input)
  Vue.use(DatePicker)
  export default {
    name: "set_addition",
    data() {
      return {
        type: 0,
        key_word: '',
        time_range: '',
        options: [
          {value: 0, label: '全部'},
          {value: 1, label: '日考'},
          {value: 2, label: '阶段考试'},
          {value: 3, label: '课程考试'},
          {value: 4, label: '项目考试'},
          {value: 5, label: '结业考试'},
        ]
      }
    },
    components: {
      BlueButton: BlueButton,
      add_exam:add_exam
    }
  }
</script>

<style scoped>
  .addition_container {
    margin-top: 50px;
    display: flex;
    justify-content: space-between;
  }

  .type_select {
    width: 134px;
  }

  .key_word {
    width: 405px;
  }

  .date_picker {
    width: 305px;
  }

  .search_icon {
    position: absolute;
    right: 0;
    top: 0;
    height: 100%;
    width: 50px;
    box-sizing: border-box;
    border:1px solid #999;
    border-radius: 0 4px 4px 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .button_text{
    padding: 0 8px;
  }
</style>
