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
            :class="{'cp':item.s_state===1,
            'unselected-option':item.s_state===0,
            'default-option':item.s_state===1,
            'selected-option':item.s_state===2}"
            @click="verifyAnswer(mainData,item)">
            <span class="option_name dib font1_22_6 ftj">
              <img v-if="item.r_state===2" class="option_pre_icon vm" src="./img/right.png" alt="">
              <img v-if="item.r_state===0" class="option_pre_icon vm" src="./img/wrong.png" alt="">
              <i v-if="item.r_state===1" class="option_pre_icon vm dib"></i>
              <span class="dib vm">{{item.option_name}}.</span>
              <span class="line2"></span>
            </span>
          <span class="choiceQuestion-content font1_22_9 dib" v-html="item.content">
            </span>
        </li>
      </ul>
      <div class="choiceQuestion-button">
        <el-button @click="emit('aheadQuestion')" v-if="buttonInfo.index+1>1">上一题</el-button>
        <el-button @click="emit('nextQuestion')" v-if="buttonInfo.index+1<buttonInfo.length">下一题</el-button>
        <el-button @click="emit('submitPaper')" v-if="buttonInfo.index+1==buttonInfo.length">完成</el-button>
      </div>
      <div class="choiceQuestion-answer">
        <div class="cqa-title ftc">
          <div class="cqat-bar inmiddle zindex1"></div>
          <span class="cqat-title font16pr3a3c50 zindex10 relative">习题详解</span>
        </div>
      </div>
    </div>
  </div>
</template>
<style lang='scss'>
  @import "../../assets/style/baseConstScss";

  .choiceQuestion-option {
    display: flex;
    justify-content: space-between;
    line-height: 32px;
    margin: 0 0 48px
  }

  .default-option:hover {
    span {
      color: $cb4;
    }
  }

  .selected-option {
    span {
      color: $c3;
    }
  }

  .selected-option:hover {
    span {
      color: $c3;
    }
  }

  .choiceQuestion-content {
    width: 1005px;
    line-height: 32px;
    padding-top: 3px;
  }

  .option_name {
    width: 70px;
    flex-shrink: 0;
    height: 32px;
    line-height: 32px;
    margin-left: 39px;
    margin-right: 86px;
  }

  .option_pre_icon {
    height: 32px;
    width: 32px;
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

  .choiceQuestion-title {
    padding: 8px 0px;
    margin-bottom: 28px;
  }

  .right-option div {
    color: white;
  }

  .wrong-option div {
    color: white;
  }

  .choiceQuestion-options {
    margin-bottom: 56px;
  }
</style>
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
      verifyAnswer(maindata, item) {
        // 杜绝重复答题
        let selected = maindata.answers.some(el => {
          if (el.s_state > 1) {
            return true
          }
        })
        if (selected) return
        // 添加选中以及未选中状态
        maindata.answers.forEach(el => {
          if (el === item) {
            el.s_state++
          } else {
            el.s_state--
          }
        })
        this.$get('/exercise/right/answer/info?question_id=' + maindata.id).then(res => {
          let data = res.data.data
          if (item.option_name === data.right_answer_name) {
            maindata.state++
            item.r_state++
          } else {
            maindata.state--
            item.r_state--
          }
          maindata.answers.forEach(el => {
            if (el.r_state === 2) return
            if (el.option_name === data.right_answer_name) {
              el.r_state++
            }
          })
        })
      }
    },
    created() {
      Bus.$on('changeQuestion', (item, buttonInfo) => {
        this.mainData = item;
        this.buttonInfo = buttonInfo;
      })
      Bus.$on('haveScoreReady', obj => {
        obj.score = Math.ceil(obj.score * 100);
        this.score = obj;
        this.show = false;
      })
      console.log(this)
    },
    mounted() {
    }
  }

</script>
