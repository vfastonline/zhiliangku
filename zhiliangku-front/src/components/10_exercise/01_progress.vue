<template>
  <div class="mw hc progress-container">
    <div class="mw progress-bar">
      <!-- 已知此进度条的宽度为总宽度减去32并且除以（length-1） -->
      <div class="progress-background-bar " :style="{'width':barWidth+'px'}"></div>
      <span v-for="(item,index) in mainData" :key="index" @click="mainfun(index)" class="progress-dot cp "
            :class="item.className">
        <img v-if="item.className=='right-selected'" src="./img/right.svg" alt="">
        <img v-if="item.className=='wrong-selected'" src="./img/wrong.svg" alt="">
      </span>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
  import Bus from '../../assets/js/02_bus'
  export default {
    name:'exercise_progress',
    data() {
      return {
        mainData: {},
        barWidth: 0,
        //这里相当于是点击的最大index的一个记录
        barWidthIndex: -1,
        buttonInfo: {},
        activeIndex: ''
      }
    },
    methods: {
      mainfun(index) {
        var item = this.mainData[index];
        if (index > this.barWidthIndex) {
          this.barWidthIndex = index;
          this.barWidth = 1168 * index / (this.mainData.length - 1);
        }
        var mainData = this.mainData;
        mainData.forEach((element, elindex) => {
          if (element.className == 'max-index-selected') {
            element.className = 'unselected'
          }
        })
        if (item.className == 'unselected') {
          item.className = "max-index-selected"

        }
        //   记录当前激活的题目
        this.activeIndex = index;
        //   将控制按钮显示和隐藏的信息传递过去
        this.buttonInfo = {
          length: this.mainData.length,
          index: index
        }
        Bus.$emit('changeQuestion', item, this.buttonInfo);
      },
      handleClassName(obj) {
        if (obj.right_answer_name != obj.selectedOptionName) {
          obj.answers[obj.selectedIndex].className = 'wrong-option';
          obj.className = "wrong-selected"
          obj.answers.forEach(element => {
            if (element.option_name == obj.right_answer_name) {
              element.className = 'right-option'
            }
          })
        }
        if (obj.right_answer_name == obj.selectedOptionName) {
          obj.answers[obj.selectedIndex].className = 'right-option'
          obj.className = 'right-selected'
        }
      },
      get_data(){
        this.$get('/exercise/list/info?video_id=' + this.$fn.funcUrl('video_id')).then(res => {
          res.data.data.forEach((element, index) => {
            element.right_answer_name = ''
            element.index = index;
            element.selectedIndex = -1
            element.className = 'unselected'
            element.answers.forEach(item => {
              item.className = 'other-option'
            })
          })
          this.mainData = res.data.data
          this.mainfun(0, this.mainData[0])
        })
      }
    },
    created() {
      Bus.$on('verifyAnswer', res => {
        this.mainData[res.index].right_answer_name = res.right_answer_option_name;
        this.handleClassName(this.mainData[res.index])
      })
      Bus.$on('aheadQuestion', res => {
        this.mainfun((this.activeIndex - 1))
      })
      Bus.$on('nextQuestion', () => {
        this.mainfun((this.activeIndex + 1))
      })
      Bus.$on('submitPaper', () => {
        // 这是计算得分的模块
        var r = 0,w=0,s=0,value=0;
        for (var i = 0; i < this.mainData.length; i++) {
          var obj = this.mainData[i];
          if (obj.selectedOptionName) {
            if (obj.selectedOptionName == obj.right_answer_name) {
              r++
            }else{w++}
          }else{
            s++
          }
        }
        if(this.mainData.length){
          value=r/this.mainData.length;
        }
        var obj1={'r':r,'w':w,'s':s,'score':value};
        Bus.$emit('haveScoreReady',obj1);
      })
      this.get_data()
    },
    mounted() {}
  }

</script>
<style scoped>
  .progress-container {
    padding: 56px 0 64px 0;
  }

  .progress-bar {
    height: 32px;
    border-radius: 16px;
    box-sizing: border-box;
    padding: 0 6px;
    position: relative;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #ECEFF1;
  }

  .progress-background-bar {
    height: 32px;
    width: 373px;
    padding-left: 32px;
    border-radius: 16px;
    position: absolute;
    top: 0px;
    left: 0px;
    background: #CFD8DC;
    transition: all ease 0.2s;
  }

  .progress-dot {
    height: 20px;
    width: 20px;
    position: relative;
    border-radius: 50%;
    justify-content: center;
    align-items: center;
  }

  .unselected {
    background: white;
  }

  .right-selected {
    background-color: #66BB6A;
  }

  .wrong-selected {
    background: #FFC107;
  }

  .max-index-selected {
    background: white;
    box-sizing: border-box;
    border: 2px solid #66BB6A;
  }

</style>
