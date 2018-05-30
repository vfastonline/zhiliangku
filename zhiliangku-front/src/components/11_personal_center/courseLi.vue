<template>
  <div class="match-rate-part-inner " :style="outerStyle">
    <img class="mrpc-company-logo fl"
         :src="mainData.logo" alt=""
         :style="imgStyle"
    >
    <div class="mrpc-company-info" :style="boxStyle">
      <div class="font20pl3a3c50">{{mainData.company}}</div>
      <div class="clearfix mrpc-company-line2">
        <span v-if="mainData.position" class="mrpc-job-name inlineblock font14pl5A646E">{{mainData.position}}</span>
        <span v-if="mainData.course_count">{{mainData.course_count}}门课程</span>
        <span class="mrpc-match-rate inlineblock  font14pl5A646E">
            <span>{{config.tag}}</span>
            <span class="font20pl3a3c50">{{Math.round((mainData.schedule?mainData.schedule:0)*100,0)}}%</span>
          </span>
        <el-button class="floatr button_style_0" @click="handleClick()">{{config.buttonStr}}</el-button>
      </div>
      <div class="mrpc-progress">
        <el-progress :percentage="(mainData.schedule?mainData.schedule:0)*100" :width="340" :stroke-width="16"
                     :show-text="false"></el-progress>
      </div>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
  import Vue from 'vue'
  import {Button, Progress} from 'element-ui'

  Vue.use(Button)
  Vue.use(Progress)
  export default {
    name: 'HelloWorld',
    data() {
      return {
        imgStyle: {},
        outerStyle: {},
        boxStyle: {}
      }
    },
    methods: {
      handleClick(evt) {
        // evt.stopPropagation();
        this.$emit('clickButton')
      }
    },
    props: {
      mainData: Object,
      styleData: Object,
      config: Object
    },
    created() {
      this.$fn.initStyle(this, 'mainData', ['imgStyle', 'outerStyle', 'boxStyle'])
    }
  }

</script>
<style>
  .match-rate-part-inner {
    padding: 16px 24px;
    background: white;
  }

  .match-rate-part-inner {
    height: 100px;
  }

  .mrpc-company-logo {
    height: 100px;
    width: 100px;
  }

  .mrpc-match-rate {
    margin-right: 32px;
  }

  .mrpc-company-info {
    margin-left: 130px;
  }

  .mrpc-progress .el-progress-bar__inner {
    border-radius: 0px
  }

  .mrpc-progress .el-progress-bar__outer {
    border-radius: 0;
  }

  .mrpc-company-line2 {
    height: 40px;
    text-align: justify;
  }

  .mrpc-job-name,
  .mrpc-progress {
    width: 340px;
  }
</style>
