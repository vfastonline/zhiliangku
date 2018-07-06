<template>
  <div class="clearfix">
    <div class="today_task_block fr">
      <div class="r top_section">
        <span class="font1_26_3 b">今日任务：</span><span class="font1_20_6">{{main_data.task}}</span>
        <div class="a sub_info">
          <!--<div class=""><span class="font1_26_3 b">昨日进度：</span><span class="font1_24_b4 num">98%</span></div>-->
          <!--<div class=""><span class="font1_26_3 b">今日进度：</span><span class="font1_24_b4 num">0%</span></div>-->
        </div>
      </div>
      <div class="m_b_section">
        <ul class="middle_section font1_20_9">
          <li class="li_unit"><span>视频：</span><span class="font1_20_b4 num">{{main_data.video_1}}</span><span>分钟</span></li>
          <li class="li_unit"><span>练习：</span><span class="font1_20_b4 num">{{main_data.video_2}}</span><span>个</span></li>
          <li class="li_unit"><span>考核：</span><span class="font1_20_b4 num">{{main_data.video_3}}</span><span>个</span></li>
        </ul>
        <div class="bottom_section font1_20_9">
          <div class="little_unit">
            <div class="ftv">视频观看时长</div>
            <div class="ftv"><span class="font1_20_b4 num">{{main_data.video_1_time}}</span><span>分钟</span></div>
          </div>
          <div class="little_unit">
            <div class="ftv">练习次数</div>
            <div class="ftv"><span class="font1_20_b4 num">{{main_data.video_2_time}}</span><span>次</span></div>
          </div>
          <div class="little_unit">
            <div class="ftv">考核</div>
            <div class="ftv"><span class="font1_20_b4 num">{{main_data.video_3_time}}</span><span>次</span></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "task_today",
    data(){
      return {
        main_data:{}
      }
    },
    methods:{
      get_data(){
        this.$get('/personal_center/today/task').then(res=>{
          this.main_data=res.data.data
          console.log(res)
        })
      }
    },
    created(){
      this.get_data()
    }
  }
</script>

<style scoped>
  .m_b_section{
    padding-left: 22px;
  }
  .li_unit {
    margin-bottom: 15px;
  }

  .middle_section {
    margin-bottom: 41px;
  }

  .bottom_section {
    display: flex;
    justify-content: space-between;
  }

  .little_unit {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
  }

  .top_section {
    margin-bottom: 24px;
  }

  .num {
    color: #00bdd4;
  }

  .b {
    font-weight: 400;
  }

  .today_task_block {
    padding: 40px 30px;
    width: 800px;
    box-sizing: border-box;
    border-radius: 10px;
    background-color: white;
  }

  .sub_info {
    min-width: 190px;
    right: 0;
    top: 0;
  }
</style>
