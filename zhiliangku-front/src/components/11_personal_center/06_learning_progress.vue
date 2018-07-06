<template>
  <div>
    <title_block :main_data="{'text':'今日任务'}"></title_block>
    <task_today></task_today>
    <title_block :main_data="{'text':'当前项目'}"></title_block>
    <ProgressContainer v-for="(item,index) in main_data"
                       :key="index"
                       :main_data="item">
      <unit :main_data="item"></unit>
    </ProgressContainer>
  </div>
</template>
<script>
import unit from './09_learning_progress_unit'
import ProgressContainer from './11_progress_block_container'
import title_block from './13_progress_block_title'
import task_today from './12_task_today'

export default {
  name: "learning_progress",
  data () {
    return {
      main_data: '',
      translation_data: []
    }
  },
  methods: {
    change_timer_length (s) {
      return s > 9 ? (s + '') : ('0' + s)
    },
    data_add_month_day (data) {
      data.forEach(el => {
        let time = new Date(el.time)
        el.month_day = this.change_timer_length(time.getMonth() + 1) + '-' + this.change_timer_length(time.getDate())
      })
    },
    init_data (data) {
      let arr = []
      data = [...data]
      data.forEach(el => {
        let key = Object.keys(el)[0]
        el[key].time = key
        this.$fn.addString(this.$myConst.httpUrl, el[key], 'pathwel')
        arr.push(el[key])
      })
      this.main_data = arr
    },
    modify_data (arr) {
      let obj_arr = {}
      arr.forEach((el) => {
        el.year = new Date(el.time).getFullYear()
        obj_arr[el.year] = obj_arr[el.year] || []
        obj_arr[el.year].push(el)
      })
      let new_arr = []
      Object.keys(obj_arr).forEach(el => {
        let year_data = obj_arr[el]
        this.sort_data(year_data)
        year_data[0].year_tag = true
        new_arr = [...new_arr, ...year_data]
      })
      this.main_data = new_arr
    },
    sort_data (arr) {
      arr.sort(function (a, b) {
        return new Date(b.time).getTime() - new Date(a.time).getTime()
      })
      return arr
    },
    handle_data (data) {
      this.init_data(data)
      this.modify_data(this.main_data)
      this.main_data = this.sort_data(this.main_data)
      this.data_add_month_day(this.main_data)
      console.table(this.main_data)
    }
  },
  created () {
    this.$get("/personal_center/learning/progress").then(res => {
      if (!res.err) {
        this.handle_data(res.data.data)
        console.log(this.main)
      }
    })
  },
  components: {

    unit: unit,
    ProgressContainer: ProgressContainer,
    title_block:title_block,
    task_today:task_today
  }
}
</script>

<style scoped>
</style>
