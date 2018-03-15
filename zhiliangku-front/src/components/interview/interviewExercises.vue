<template>
  <div class="choiceQuestion mainwidth incenter">
    <div class="choiceQuestion-title font16pr3a3c50" v-html="mainData.title"></div>
    <ul class="choiceQuestion-options">
      <li v-for="(item ,index ) in mainData.answers" :key="index" class="choiceQuestion-option font16pr3a3c50 pointer" @click="selectedAnwser(mainData,item,index)"
        :class="item.className">
        <div>
          <div class="floatl font20pl3a3c50" v-html="item.option_name"></div>
          <div class="choiceQuestion-content font16pr3a3c50" v-html="item.content"></div>
        </div>
      </li>
    </ul>
    <div class="choiceQuestion-button">
      <el-button @click="emit('aheadQuestion')" v-if="buttonInfo.index+1>1">上一题</el-button>
      <el-button @click="emit('nextQuestion')" v-if="buttonInfo.index+1<buttonInfo.length">下一题</el-button>
      <el-button @click="emit('submitPaper')" v-if="buttonInfo.index+1==buttonInfo.length">完成</el-button>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
  import Bus from '../../assets/js/bus'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        mainData: {},
        buttonInfo: {},
      }
    },
    watch: {},
    methods: {
      emit(event) {
        Bus.$emit(event)
      },
      selectedAnwser(maindata, item, index) {
        //将该选项的选择状态取反
        item.selected = !item.selected;
        item.className = item.selected ? 'selected' : 'unselected';
        //如果是单选题，那么将别的选项清楚
        if (maindata.qtype == 1) {
          maindata.answers.forEach((ele, elei) => {
            if (elei != index) {
              ele.selected = false;
              ele.className = 'unselected';
            }
          })
        }
        console.log(maindata)
        maindata.haveAnswer = false;
        maindata.className = 'haveNoAnwser';
        maindata.answers.forEach((i) => {
          if (i.selected) {
            maindata.haveAnswer = true;
            maindata.className = 'haveAnwser'
          }
        })
      }
    },
    created() {
      Bus.$on('changeQuestion', (item, buttonInfo) => {
        this.mainData = item;
        this.buttonInfo = buttonInfo;
      })
    },
    mounted() {}
  }

</script>
<style scoped>
  .selected {
    box-sizing: border-box;
    border: 2px solid #23b8ff;
  }

  .choiceQuestion-title {
    padding: 8px 0px;
    margin-bottom: 40px;
  }

  .choiceQuestion-option {
    padding: 33px 40px;
  }

  .choiceQuestion-button {
    text-align: right;
  }

  .unselected {
    background: white;
  }

  .unselected:hover {
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
    margin-left: 75px;
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

</style>
