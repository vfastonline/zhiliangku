<template>
  <div class="mainwidth incenter progress-container">
    <div class="mainwidth progress-bar">
      <!-- 已知此进度条的宽度为总宽度减去32并且除以（length-1） -->
      <div class="progress-background-bar zindex1" :style="{'width':barWidth+'px'}"></div>
      <span v-for="(item,index) in mainData" :key="index" @click="mainfun(index)" class="progress-dot pointer zindex10 fontcenter"
        :class="item.className">{{index+1}}</span>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
  import Bus from '../../assets/js/bus'
  export default {
    data() {
      return {
        barWidth: 0,
        //这里相当于是点击的最大index的一个记录
        barWidthIndex: -1,
        buttonInfo: {},
        activeIndex: 0,
        mainData: {}
      }
    },
    props: {

    },
    watch: {
      activeIndex: function (nvalue, ovalue) {
        console.log(ovalue);
        this.verifyAnswer(ovalue)
        console.log(nvalue)
        // 这个时候去校验答案。
      }
    },
    methods: {
      jj() {
        this.mainData[0].className = 'max-index-selected';
        console.log(this.mainData[0])
      },
      orgnizeUrl(index) {
        var item = this.mainData[index];
        var str = '/interview_questions/examinationquestion/answer/info?examination_question_id=' +
          item.id +
          '&custom_user_id=' + localStorage.uid;
        var flag = true;
        item.answers.forEach((ele) => {
          if (ele.selected) {
            flag = false;
            str += '&option=' + ele.option
          }
        })
        if (flag) {
          str += '&option=' + null;
        }
        return str
      },
      verifyAnswer(index) {
        this.$get(this.orgnizeUrl(index)).then(res => {
          console.log(res)
        })
      },
      mainfun(index) {
        console.log(index)
        var item = this.mainData[index];
        // 只有当前激活的索引比最大索引大时才能进入此函数
        if (index > this.barWidthIndex) {
          this.barWidthIndex = index;
          this.barWidth = 1120 * index / (this.mainData.length - 1);
          var mainData = this.mainData;
          //目前来看是没有问题的
          //给当前激活的索引加上最大索引类名
          item.className = "max-index-selected"
          console.log(item.className)
          mainData.forEach((element, elindex) => {
            //清除索引比当前点击的索引小的元素的最大样式
            if (elindex < index) {
              if (element.className == 'max-index-selected') {
                element.className = 'haveNoAnwser'
              }
            }
          })
        }
        //   记录当前激活的题目
        this.activeIndex = index;
        //   将控制按钮显示和隐藏的信息传递过去
        this.buttonInfo = {
          length: this.mainData.length,
          index: index
        }

        console.log(item)
        Bus.$emit('changeQuestion', item, this.buttonInfo);
      },
      initMainData(data) {
        data.forEach((element, index) => {
          element.index = index;
          element.selectedIndex = -1;
          element.className = 'haveNoAnwser'
          element.answers.forEach(item => {
            item.className = 'unselected'
          })
          this.mainData = JSON.parse(JSON.stringify(data))
        });
      }
    },
    created() {
      Bus.$on('aheadQuestion', res => {
        this.mainfun((this.activeIndex - 1))
      })
      Bus.$on('nextQuestion', () => {
        this.mainfun((this.activeIndex + 1))
      })
      Bus.$on('submitPaper', () => {
        this.verifyAnswer(this.mainData.length - 1)
        this.$fn.go('/interview_questions/enterprise/result/?enterpriseinfo_id=' + this.$fn.funcUrl('enterprise_id'))
      })
      this.$get('/interview_questions/examinationquestion/list/info?enterprise_id=' + this.$fn.funcUrl('enterprise_id'))
        .then(res => {
          this.mainData = res.data.data;
          this.initMainData(this.mainData)
          this.mainfun(0)
        })
    },
    mounted() {}
  }

</script>
<style>
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
    line-height: 20px;
    width: 20px;
    position: relative;
    border-radius: 50%;
    justify-content: center;
    align-items: center;
    font-size: 12px;
  }

  .haveNoAnwser {
    background: white;
    color: #808B90;
  }

  .haveAnwser {
    background: #808B90;
    color: white;
  }

  .right-selected {
    background-color: #808B90;
  }

  .wrong-selected {
    background: #FFC107;
  }

  .max-index-selected {
    background: white;
    box-sizing: border-box;
    border: 2px solid #808B90;
    line-height: 16px;
  }

</style>
