<template>
  <div class="im-container">
    <subtitle :msg="msg"></subtitle>
    <div v-if="showList" class="interviewmain-content ">
      
          <el-scrollbar >
            <div class="clearfix" :style="{'width':boxWidth,position:'absolute',left:'50%','margin-left':'-576px'}">
               <interview-cover  @click="go(item)" v-for="item in interviewData" :key="item.id"  :layout="layout" :mainData="item" :myStyle="{className:['floatl'],outerStyle:{'margin-right':'32px'}}"></interview-cover>
            </div>
          </el-scrollbar>
      
    </div>
  </div>
</template>
<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        msg: {
          linker:'/interview_questions/enterpriseinfo/list/',
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
        showList:false,
        boxWidth:'',
        interviewData:{},
        layout:['company','number']
      }
    },
    methods:{
      go(item){
        window.location.href='http://'+window.location.host+'/interview_questions/enterpriseinfo/detail/?enterpriseinfo_id='+item.id;
      }
    },
    created(){
        this.$get('/interview_questions/index/list').then(res=>{
            this.interviewData=this.$fn.addString(this.$myConst.httpUrl,res.data.data,'question_img')
            this.boxWidth=this.interviewData.length*394+'px';
            this.showList=true;
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
    height:500px;
    overflow: auto;
    position: relative;
  }
  .imc-question {
    overflow: auto;
  }
  .imc-questionContainer {
    background: pink;
  }
</style>
