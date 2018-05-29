<template>
  <div class="mw hc progress-container">
    <div class="mw progress-bar">
      <!-- 已知此进度条的宽度为总宽度减去定宽度并且除以（length-1） -->
      <div class="progress-background-bar " :style="{'width':barWidth+'px'}"></div>
      <span
        v-for="(item,index) in mainData"
        :key="index"
        @click="main_func(index)"
        class="progress-dot cp ">
        <img v-if="item.state===2" class="v_icon" src="./img/right.png" alt="">
        <img v-if="item.state===1" class="v_icon" src="./img/default.png" alt="">
        <img v-if="item.state===0" class="v_icon" src="./img/wrong.png" alt="">
      </span>
    </div>
  </div>
</template>
<style>
  .v_icon {

  }
</style>
<!-- Add "scoped" attribute to limit CSS to this component only -->

<style scoped>
  .progress-container {
    padding: 56px 0 64px 0;
  }

  .progress-bar {
    padding: 0 9px;
    height: 60px;
    border-radius: 100px;
    box-sizing: border-box;
    position: relative;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #eaeaea;
  }

  .progress-background-bar {
    height: 60px;
    padding-left: 60px;
    border-radius: 100px;
    position: absolute;
    top: 0px;
    left: 0px;
    background: #CFD8DC;
    transition: all ease 0.2s;
  }

  .progress-dot {
    height: 42px;
    width: 42px;
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
<script>
  import Bus from '../../assets/js/02_bus'

  export default {
    name: 'exercise_progress',
    data() {
      return {
        mainData: {},
        barWidth: 0,
        //这里相当于是点击的最大index的一个记录
        barWidthIndex: -1,
        // 这是决定按钮排布显隐的信息
        buttonInfo: {},
        //  用途为上一题或者下一题的时候有一个参照能够准确找到题目
        activeIndex: ''
      }
    },
    methods: {
      rate_of_progress(index) {
        if (index > this.barWidthIndex) {
          this.barWidthIndex = index;
          this.barWidth = 1140 * index / (this.mainData.length - 1);
        }
      },
      main_func(index) {
        this.rate_of_progress(index)
        let item = this.mainData[index];
        this.activeIndex = index;
        //   将控制按钮显示和隐藏的信息传递过去
        this.buttonInfo = {
          length: this.mainData.length,
          index: index
        }
        Bus.$emit('changeQuestion', item, this.buttonInfo);
      },
      get_data() {
        this.$get('/exercise/list/info?video_id=' + this.$fn.funcUrl('video_id')).then(res => {
          res.data.data.forEach((element, index) => {
            element.index = index
            //下行代码是状态码0:错误，1：初始，3：正确。
            element.state = 1
            element.answers.forEach(item => {
              // 下行代码是每个选项的状态码，内容同上
              item.r_state = 1
              // 选项是否被选中了的状态码0：没有被选中，1：初始状态，2：选中状态
              item.s_state = 1
            })
          })
          this.mainData = res.data.data
          this.main_func(0)
        })
      },
      count_score() {
        // 这是计算得分的模块
        var r = 0, w = 0, s = 0, value = 0;
        this.mainData.forEach(el => {
          switch (el.state) {
            case 0:
              w++
              break
            case 1:
              s++
              break
            case 2:
              r++
              break
            default:break
          }
        })
        if (this.mainData.length) {
          value = r / this.mainData.length;
        }
        var obj1 = {'r': r, 'w': w, 's': s, 'score': value};
        Bus.$emit('haveScoreReady', obj1);
      }
    },
    created() {
      //获得数据
      this.get_data()
      // 上一题
      Bus.$on('aheadQuestion', res => {
        this.main_func((this.activeIndex - 1))
      })
      // 下一题
      Bus.$on('nextQuestion', () => {
        this.main_func((this.activeIndex + 1))
      })
      // 显示得分
      Bus.$on('submitPaper', () => {
        this.count_score()
      })
    },
    mounted() {
    }
  }

</script>
