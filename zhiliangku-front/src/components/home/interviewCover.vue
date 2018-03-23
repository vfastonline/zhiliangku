<template>
  <div class="ic-container ofhid pointer " @click="go()" :class="className" :style="outerStyle">
    <ul class="icc-content">
      <li class="iccc-title fontcenter textellipsis font20pr5a646e">{{mainData.position}}</li>
      <li class="iccc-img">
        <img class="iccc-img"  v-lazy="mainData.question_img" alt="">
      </li>
      <li class="iccc-info fontjustify">
        <div class="iccci-tag clearfix">
          <span class="icccit-1 floatl font14prb2bbbf">{{mainData.tag1?mainData.tag1:'月薪'}}</span>
          <span class="icccit-2 floatr font14pr002800">{{mainData.lowest_monthly_salary|turnToThu}}-{{mainData.highest_monthly_salary|turnToThu}}</span>
        </div>
        <div v-if="layout.indexOf('number')!=-1" class="iccci-tag clearfix">
          <span class="icccit-1 floatl font14prb2bbbf">{{mainData.tag2?mainData.tag2:'试题数量'}}</span>
          <span class="icccit-2 floatr font14pr002800">{{mainData.amount}}</span>
        </div>
        <div v-if="layout.indexOf('course')!=-1" class="iccci-tag clearfix">
          <span class="icccit-1 floatr font14prb2bbbf">{{mainData.tag3?mainData.tag2:'门课程'}}</span>
          <span class="icccit-2 icccit-2num floatr font14pr002800">{{mainData.courses_count}}</span>
        </div>
      </li>
      <li v-if="layout.indexOf('company')!=-1" class="iccc-name fontcenter textellipsis font20pr5a646e">{{mainData.company}}</li>
    </ul>
  </div>
</template>
<script>
import VueLazyLoad from 'vue-lazyload'
Vue.use(VueLazyLoad,{
})
  export default {
    name: "HelloWorld",
    data() {
      return {
        msg: "Welcome to Your Vue.js App",
        className: [],
        outerStyle: {},
        myStyleData: {}
      };
    },
    props: {
      mainData: Object,
      layout: Array,
      myStyle: Object,
      index: Number,
      linker: String
    },
    methods: {
      go() {
        this.$emit('click')
        if (!this.linker) {
          return
        }
        window.location.href = this.linker + '?path_id=' + this.mainData.id;
      }
    },
    filters: {
      turnToThu: function (value) {
        return parseInt(value / 1000) + 'k'
      }
    },
    created() {
      // debugger
      this.myStyleData = this.deepCopy(this.myStyle);
      if (this.myStyle) {

        if (this.myStyle.num) {
          if (!((this.index + 1) % this.myStyle.num)) {
          
            if (this.myStyle['outerStyle']['margin-right']) {
              this.myStyleData[['outerStyle']]['margin-right'] = '0';
            }
          }
        }
      }
      this.$fn.initStyle(this.$vueself(), 'myStyleData', ['className', 'outerStyle'])
    }
  };

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .ic-container {
    width: 362px;
    /* height: 445px; */
    background: white;
  }

  .iccc-title,
  .iccc-name {
    letter-spacing: 2.86px;
  }

  .iccc-title {
    padding: 17px 0px;
  }

  .iccc-img {
    width: 362px;
    height: 272px;
  }

  .iccc-info {
    padding: 0px 32px;
    width: 298px;
    height: 20px;
    line-height: 20px;
    margin-top: 27px;
    margin-bottom: 16px;
    display: flex;
    justify-content: space-between;
  }

  .iccci-tag {
    display: inline;
  }

  .iccci-tag {
    width: 133px;
  }

  .iccc-name {
    margin-bottom: 28px;
  }

  .icccit-2num {
    margin-right: 32px;
    text-align: right;
  }

</style>
