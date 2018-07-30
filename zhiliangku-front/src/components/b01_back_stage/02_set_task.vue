<template>
  <div class=" hc r">
    <div class="task_title">
      <span class="dib font1_30_3">今日学习任务</span>
      <span class="font1_18_9 dib time_span">{{(new Date()) | moment('YYYY-MM-DD')}}(今日)</span>
    </div>
    <div  class="right_div a">
      <div class="font1_20_6">
        昨日目标进度
        <span class="b_num font1_28_b4">{{yesterday_data.yesterday_task_schedule}}</span>
        %
      </div>
      <div class="font1_20_6">
        完成昨日目标人数占比
        <span class="b_num font1_28_b4">{{yesterday_data.yesterday_completion_ratio}}</span>
        %
      </div>
      <div  v-if="main_data.today_task_schedule" class="font1_20_6">
        今日预计目标进度
        <span class="b_num font1_28_b4">{{main_data.today_task_schedule}}</span>
        %
      </div>
    </div>
    <!--<div class="recommend_progress font1_18_6">-->
      <!--推荐学习到：{{main_data.today_task_name}}-->
    <!--</div>-->
    <selected_task></selected_task>
  </div>
</template>

<script>
  import Vue from 'vue'
  import selected_task from './03_set_task_select_content'
  import Bus from '../../assets/js/02_bus'

  Vue.use(require('vue-moment'))
  export default {
    name: "_set_task",
    data() {
      return {
        main_data: {},
        yesterday_data:{}
      }
    },
    methods: {
      get_recommend() {
        this.$get('/backstage/get/today/task/schedule').then(res => {
          this.main_data = res.data.data
        })
      },
      get_yesterday_data() {
        this.$get('/backstage/get/yesterday/task/schedule').then(res => {
          //其实这里这样用是错误的，因为set的第一个参数不能使vue实例。但是这里已经辽预处理（data中的key）
          //此时调用此方法也不出错就是了。本质上一样。
          this.$set(this,'yesterday_data', res.data.data)
        })
      }
    },
    components: {
      selected_task: selected_task
    },
    created() {
      this.get_yesterday_data()
      Bus.$on('recommend_enter',res=>{
        this.main_data=res
      })
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
