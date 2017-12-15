<template>
  <div class="im-container">
    <subtitle :msg="msg"></subtitle>
    <div class="interviewmain-content test-1">
      <div class="mainwidth incenter imc-question test-1">
          <el-carousel  :interval="400000" type="card" height="440px">
            <div class="idea">
            <el-carousel-item v-for="item in interviewData" :key="item.id">
              <interview-cover :layout="layout" :mainData="item" :myStyle="{'className':['incenter']}"></interview-cover>
            </el-carousel-item>
            </div>
          </el-carousel>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        msg: {
          enTitle: 'Interview Question',
          title: '企业面试题',
          slogon: '知己知彼，百战不殆',
          myStyle: {
            'color': '#ffffff'
          },
          enTitleStyle:{
            'color':'#ffffff','opacity':'0.1'
          }
        },
        interviewData:{},
        layout:['company','number']
      }
    },
    created(){
        this.$ajax.get('interview_questions/index/list').then(res=>{
            this.interviewData=this.$fn.addString(this.$myConst.httpUrl,res.data.data,'question_img')
            // console.log(this.interviewData)
        })
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .im-container {
    background: #1A94CE;
  }
  .idea{
      width:784px;
      margin:auto;
  }
  .interviewmain-content {
    width: 100%;
    height: 500px;
    height: 552px;
    overflow: auto;
    position: relative;
  }
  .imc-question {
    overflow: auto;
  }
  .imc-questionContainer {
    background: pink;
  }
  .imcq-content {
    width: 2800px;
    height: 445px;
  }
  /* 滚动条样式，现在存在兼容性，需要完善兼容代码，可以参照el-scrollbar的样式进行修改 */

  .test-1::-webkit-scrollbar {
    /*滚动条整体样式*/
    width: 10px;
    /*高宽分别对应横竖滚动条的尺寸*/
    height: 10px;
  }

  .test-1::-webkit-scrollbar-thumb {
    /*滚动条里面小方块*/
    border-radius: 10px;
    -webkit-box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
    background: #535353;
  }

  .test-1::-webkit-scrollbar-track {
    /*滚动条里面轨道*/
    -webkit-box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
    border-radius: 10px;
    background: #EDEDED;
  }

</style>
