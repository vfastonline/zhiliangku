<template>
  <div class="choiceQuestion mw hc">
    <div v-if="!show" class="defen">
      <div>
        <div class="ftc score">本次得分</div>
        <div class="ftc score" :class="{'redscore':score.score<60}">{{score.score}}</div>
        <div class="tags-container">
          <div class="tags-container-item">
            <span class="status-tag status-black "></span>
            {{score.s}}
          </div>
          <div class="tags-container-item">
            <span class="status">
              <img class="status_icon" src="./img/wrong.svg" alt="">
            </span> {{score.w}}
          </div>
          <div class="tags-container-item">
            <span class="status">
              <img class="status_icon" src="./img/right.svg" alt="">
            </span> {{score.r}}
          </div>
        </div>
        <!-- <div class="ftc">失败是成功的开始</div> -->
      </div>
      <div class="ftc">
        <el-button @click="reload()">重新作答</el-button>
        <el-button @click="nextSection()">下一节</el-button>
      </div>
    </div>
    <div v-if="show">
      <div class="choiceQuestion-title font1_24_3">{{mainData.title}}</div>
      <ul class="choiceQuestion-options">
        <li v-for="(item ,index ) in mainData.answers" :key="index"
            class="choiceQuestion-option  "
            @click="verifyAnswer(mainData,item,index)"
            >
          <div class="cp">
            <div class="fl option_name font1_22_6">
              <img class="option_pre_icon" src="./img/right.png" alt="">
              <img class="option_pre_icon" src="./img/wrong.png" alt="">
              <span class="option_pre_icon dib" ></span>
              {{item.option_name}}.</div>
            <div class="choiceQuestion-content font1_22_9" v-html="item.content"></div>
          </div>
        </li>
      </ul>
      <!--<div class="choiceQuestion-button">-->
        <!--<el-button @click="emit('aheadQuestion')" v-if="buttonInfo.index+1>1">上一题</el-button>-->
        <!--<el-button @click="emit('nextQuestion')" v-if="buttonInfo.index+1<buttonInfo.length">下一题</el-button>-->
        <!--<el-button @click="emit('submitPaper')" v-if="buttonInfo.index+1==buttonInfo.length">完成</el-button>-->
      <!--</div>-->
      <!--<div class="choiceQuestion-answer">-->
        <!--<div class="cqa-title ftc">-->
          <!--<div class="cqat-bar inmiddle zindex1"></div>-->
          <!--<span class="cqat-title font16pr3a3c50 zindex10 relative">习题详解</span>-->
        <!--</div>-->
      <!--</div>-->
    </div>
  </div>
</template>
<style lang='scss'>
  .option_name{
    width: 194px;
    padding-left: 40px;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
  }
  .option_pre_icon{
    height: 32px;
    width: 32px;
    margin-right: 30px;
  }
  .score {
    font-size: 22px;
    margin: 10px;
  }

  .tags-container {
    display: flex;
    justify-content: center;
  }

  .defen {
    width: 500px;
    margin: auto;
    min-height: 300px;

  }

  .redscore {
    color: #ef6360
  }

  .status-tag {
    height: 20px;
    width: 20px;
    position: relative;
    border-radius: 50%;
    display: inline-block;
    vertical-align: bottom;
  }

  .status-black {
    border: 2px solid #CFD8DC;
  }

  .status {
    vertical-align: bottom;
    height: 24px;
    width: 24px;
    display: inline-block;
  }

  .tags-container-item {
    margin: 10px;
  }

  .status_icon {
    height: 24px;
    width: 24px;
  }

</style>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
  import Vue from 'vue'
  import Bus from '../../assets/js/02_bus'
  import func from '../../assets/js/01_other/01_dispatch'
  import {Button} from 'element-ui'
  Vue.use(Button)
  Vue.prototype.$func = func;
  export default {
    name: 'HelloWorld',
    data() {
      return {
        mainData: {},
        buttonInfo: {},
        score: {},
        show: true
      }
    },
    watch: {},
    methods: {
      reload() {
        window.location.reload()
      },
      nextSection() {
        this.$get('/tracks/next/video?course_id=' + this.$fn.funcUrl('course_id') + '&video_id=' + this.$fn.funcUrl(
          'video_id')).then(res => {
          var data = res.data.data;
          this.$func.goCourse(data.type, data.course_id, data.video_id)
        })
      },
      emit(event) {
        Bus.$emit(event)
      },
      verifyAnswer(maindata, item, index) {
        if (maindata.selectedIndex != -1) {
          return
        }
        maindata.selectedOptionName = item.option_name;
        maindata.selectedIndex = index;
        this.$get('/exercise/right/answer/info?question_id=' + maindata.id).then(res => {
          res.data.data.index = this.mainData.index;
          Bus.$emit('verifyAnswer', res.data.data)
        })
      }
    },
    created() {
      Bus.$on('changeQuestion', (item, buttonInfo) => {
        this.mainData = item;
        this.buttonInfo = buttonInfo;
      })
      Bus.$on('haveScoreReady', obj => {
        obj.score=Math.ceil(obj.score*100);
        this.score = obj;
        this.show = false;
      })
    },
    mounted() {}
  }

</script>
<style scoped>
  .choiceQuestion-title {
    padding: 8px 0px;
    margin-bottom: 40px;
  }

  .choiceQuestion-option {
    /*padding: 33px 40px;*/
  }

  .choiceQuestion-button {
    text-align: right;
  }

  .other-option {
    background: white;
  }

  .other-option:hover {
    background: #fafafa;
  }

  .choiceQuestion-resault {
    height: 500px;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .right-option {
    color: white;
    background: #66bb6a;
  }

  .wrong-option {
    color: white;
    background: #ffc107;
  }

  .right-option div {
    color: white;
  }

  .wrong-option div {
    color: white;
  }

  .choiceQuestionTags {
    width: 75px;
  }

  .choiceQuestion-content {
    margin-left: 160px;
  }

  .choiceQuestion-options {
    margin-bottom: 56px;
  }

  .cqa-title {
    height: 22px;
    position: relative;
    margin-bottom: 16px;
  }

  .cqat-bar {
    height: 2px;
    background: #cfd8dc;
    width: 100%;
  }

  .cqat-title {
    padding: 0 6px;
    background: #fafafa;
  }

  .answerContent {}

</style>
