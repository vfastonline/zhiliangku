<template>
<!--20180102  面试题详情 -->
  <div class="test-information mainwidth incenter clearfix">
  <!--左侧  测评须知   -->
    <div class="inter-info-notice left ">
     <div class="notice-title font14pr3a3c50 top"><span>测评须知：</span></div>
      <div class="notice-content font14pl5a646e bottom">
       <p>1.请确保网络传输稳定，建议使用内核版本59.0及以上的Chrome浏览器；<br>
      2.请在倒计时内完成题目，到了结束时间就无法继续答题了，请提前安排好时间；<br>
      3.答题过程中，系统将自动计时，请在规定时间内完成，时间一到，将自动交卷；<br>
      4.右上角有整场测评倒计时，请在倒计时前完成测评，提交后不可返回更改；<br>
      5.该试卷只允许单次作答，计时结束或提交后不可重答；<br>
      6.客观题系统采用计算机自动阅卷方式判定结果，系统不对结果做任何形式的干预；<br>
      7.诚信测评：过程中请勿离开作答界面，系统将自动记录您的操作日志。<br>
      </p>
      </div>
    </div>
  <!--左侧结束-->
  <!--右侧 题型-->
    <div class = "inter-info-kinds right">   
      <div class = "right-title top font14pr3a3c50">
        <p>本试卷专门用于入职面试考试，如何对Linux系统进行管理，包括进程管理、工作管理、
        系统资源查看和定时任务，每个部分讲师都进行了详细的讲解。相信通过本课程的学习，你
        的Linux技能会有进一步提升。</p>
      </div> 
      <div class="right-kinds bottom">
        <table class="font14pr3a3c50">
          <tr class="rk-title">
            <td class="td-left">题型</td>
            <td class="td-mid">题目数</td>
            <td class="td-right">分值</td>
          </tr>
          <tr v-for="(item,index) in items":key="index">
            <td class="td-left">{{item.kinds}}</td>
            <td class="td-mid">{{item.number}}</td>
            <td class="td-right">{{item.score}}</td>
          </tr>
        </table>
      </div>

    </div>
  <!--右侧结束-->
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.test-information{
  height:320px;
  margin-top:54px;
}
.left{
  width:320px;
  height:320px;
  float:left;
}
.right{
  width:752px;
  height:320px;
  float:right;
}
.top{
  height:40px;
}
.bottom{
  height:280px;
}

.left .notice-content{
  text-align:justify;
}

.bottom table{
  width:752px;
}
.rk-title{
  background:#EEF0F2;
}
table td{
  line-height:40px;
}
table .td-left{
  text-align:left;
  padding-left:42px;
}
table .td-mid{
  text-align:center;
}
table .td-right{
  text-align:right;
  padding-right:42px;
}

</style>
<script>

export default {
  name: 'HelloWorld',
  data () {
    return {
      items: [
        {kinds:'判断题',number:'10道',score:'10分'},
        {kinds:'单选题',number:'8道',score:'16分'},
        {kinds:'多选题',number:'7道',score:'24分'},
        {kinds:'编程题',number:'5道',score:'60分'}
        
      ]
    }
  }
}
</script>


