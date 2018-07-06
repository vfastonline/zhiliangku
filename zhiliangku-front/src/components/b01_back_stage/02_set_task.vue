<template>
  <div class=" hc r">
    <div class="task_title">
      <span class="dib font1_30_3">今日学习任务</span>
      <span class="font1_18_9 dib time_span">{{(new Date()) | moment('YYYY-MM-DD')}}(今日)</span>
    </div>
    <!--<div class="right_div a">-->
    <!--<div class="font1_20_6">昨日目标进度 <span class="b_num font1_28_b4">86</span>%</div>-->
    <!--<div class="font1_20_6">完成昨日目标人数占比 <span class="b_num font1_28_b4">90</span>%</div>-->
    <!--<div class="font1_20_6">今日预计目标进度 <span class="b_num font1_28_b4">96</span>%</div>-->
    <!--</div>-->
    <div class="recommend_progress font1_18_6">
      推荐学习到：{{main_data.today_task_name}}
    </div>
    <selected_task></selected_task>
  </div>
</template>

<script>
  import Vue from 'vue'
  import selected_task from './03_set_task_select_content'

  Vue.use(require('vue-moment'))
  export default {
    name: "_set_task",
    data() {
      return {
        main_data: {}
      }
    },
    methods: {
      get_recommend() {
        this.$get('/backstage/get/today/task/schedule').then(res => {
          this.main_data = res.data.data
        })
      }
    },
    components: {
      selected_task: selected_task
    },
    created() {
      // this.get_recommend()
    }
  }
</script>

<style scoped lang="scss">
  @import '../../assets/style/baseConstScss.scss';

  .recommend_progress {
    margin-bottom: 20px;
  }

  .right_div {
    right: 0;
    top: 20px;
  }

  .time_span {
    margin-left: 20px;
    font-weight: 600;
  }

  .task_title {
    margin-bottom: 20px;
  }

  .b_num {
    color: $cb4;
  }
</style>
