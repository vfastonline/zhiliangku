<template>
  <!--20180103 面试题测试反馈-->
  <div v-if="mainData" class="inter-result floatl">
    <!--******** -->
    <p class="is-title font14pr3a3c50">面试题测试反馈</p>
    <p class="is-job font14pl5A646E">职位：{{mainData.position}}</p>
    <p class="is-from font14pl5A646E">出题方：{{mainData.company}}</p>
    <!--******** -->
    <div class="result-data">
      <div>
        <div class="rd-number">
          <span class="font24pr23b8ff">{{getnum(qtype_list,1,1)}}</span>
          <span class="font14pr23b8ff">/ {{getnum(qtype_list,1)}}</span>
        </div>
        <p class="font14pr5a646e">选择题正确率</p>
      </div>
      <div>
        <div class="rd-number">
          <span class="font24pr23b8ff">{{getnum(qtype_list,3,1)}}</span>
          <span class="font14pr23b8ff">/ {{getnum(qtype_list,1,1)}}</span>
        </div>
        <p class="font14pr5a646e">编程题正确率</p>
      </div>
      <div>
        <div class="rd-number">
          <span class="font24pr23b8ff">0</span>
          <span class="font14pr23b8ff">次</span>
        </div>
        <p class="font14pr5a646e">离开次数</p>
      </div>
    </div>
    <!--******** -->
    <div class="result-choice">
      <el-button>投递面试结果</el-button>
      <el-button>挑战更多面试题</el-button>
    </div>
  </div>
</template>
<script>
import Bus from '../../assets/js/bus'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        qtype_list: [],
         mainData: Object
      }
    },
    props: {
     
    },

    methods: {
      getnum(arr, type, right) {
        var num=0;
        arr.forEach((ele) => {
          if (type == ele.qtype) {
            num = ele.qtype__count;
            if (right == '1') {
              num = ele.right_qtype__count;
            }
          }
        })
        return num;
      }
    },
    created() {
      this.$get('/interview_questions/enterprise/result/info?custom_user_id=' + localStorage.uid +
        '&enterpriseinfo_id=' + this.$fn.funcUrl('enterpriseinfo_id')).then(res => {
        this.mainData = res.data.data;
         this.qtype_list = this.mainData.qtype_list;
        console.log(res)
      })
    }

  }

</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  /* ******** */

  .inter-result {
    width: 320px;
  }

  .inter-result .is-title {
    line-height: 20px;
  }

  .inter-result .is-job {
    margin-top: 27px;
    line-height: 20px;
  }

  .inter-result .is-from {
    margin-top: 24px;
    line-height: 20px;
  }
  /* ******** */

  .result-data {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin-top: 25px;
  }

  .result-data .rd-number {
    height: 33px;
    text-align: center;
  }

  .result-data p {
    height: 20px;
    line-height: 20px;
  }
  /* ******** */

  .result-choice {
    margin-top: 24px;
  }

</style>
