<template>
  <div class="choiceQuestion mainwidth incenter">
    <div class="choiceQuestion-title font16pr3a3c50">{{mainData.title}}</div>
    <ul class="choiceQuestion-options">
        <li 
        v-for="(item ,index ) in mainData.answers" :key="index"
        class="choiceQuestion-option font16pr3a3c50 pointer"
        @click="verifyAnswer(mainData,item,index)"
        :class="item.className"
        >
            <div>
                <div class="floatl font20pl3a3c50" >{{item.option_name}}</div>
                 <div class="choiceQuestion-content font16pr3a3c50">{{item.content}}</div>
            </div>
        </li>
    </ul>
    <div class="choiceQuestion-button">
        <el-button @click="emit('aheadQuestion')" v-if="buttonInfo.index+1>1">上一题</el-button>
        <el-button @click="emit('nextQuestion')" v-if="buttonInfo.index+1<buttonInfo.length">下一题</el-button>
        <el-button @click="emit('submitPaper')" v-if="buttonInfo.index+1==buttonInfo.length">完成</el-button>
    </div>
    <div class="incenter mainwidth choiceQuestion-resault">

    </div>
    <div class="choiceQuestion-answer">
        <div class="cqa-title fontcenter">
            <div class="cqat-bar inmiddle zindex1"></div>
            <span class="cqat-title font16pr3a3c50 zindex10 relative">习题详解</span>
        </div>
        <div class="answerContent font16pr3a3c50">
            不会代码的ui不是好导演
        </div>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
import Bus from '../../assets/js/bus'
export default {
  name: 'HelloWorld',
  data () {
    return {
      mainData:{},
      buttonInfo:{},
    }
  },
  watch:{
  },
  methods:{
      emit(event){
          Bus.$emit(event)
      },
      verifyAnswer(maindata,item,index){
          if(maindata.selectedIndex!=-1){return}
          maindata.selectedOptionName=item.option_name;
          maindata.selectedIndex=index;
          this.$get('/exercise/right/answer/info?question_id='+maindata.id).then(res=>{
              res.data.data.index=this.mainData.index;
              Bus.$emit('verifyAnswer',res.data.data)
          })
      }
  },
  created(){
      Bus.$on('changeQuestion',(item,buttonInfo)=>{
          this.mainData=item;
          this.buttonInfo=buttonInfo;
          console.log(this.mainData)
      })
  },
  mounted(){
  }
}
</script>
<style scoped>
.choiceQuestion-title{
    padding:8px 0px;
    margin-bottom:40px;
}
.choiceQuestion-option{
    padding:33px 40px;
}
.choiceQuestion-button{
    text-align: right;
}
.other-option{
    background:white;   
}
.other-option:hover{
background:  #fafafa;
}
.choiceQuestion-resault{
    height:500px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.right-option{
    color: white;
    background: #66bb6a;
}
.wrong-option{
    color:white;
    background:#ffc107;
}
.right-option div{
    color:white;
}
 .wrong-option div {
    color:white;
}
.choiceQuestionTags{
    width:75px;
}
.choiceQuestion-content{
    margin-left:75px;
}
.choiceQuestion-options{
    margin-bottom:56px;
}
.cqa-title{
    height:22px;
    position: relative;
    margin-bottom:16px;
}
.cqat-bar{
    height:2px;
    background: #cfd8dc;
    width:100%;
}
.cqat-title{
    padding:0 6px;
    background:#fafafa;
}
.answerContent{

}
</style>



