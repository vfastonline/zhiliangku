<template>
    <div class="match-rate-part-inner rise" :style="outerStyle">
      <img class="mrpc-company-logo floatl" 
       src="../../assets/img/user-icon.jpg" alt=""
       :style="imgStyle"
       >
      <div class="mrpc-company-info" :style="boxStyle">
        <div class="font20pl3a3c50">凯奇谷</div>
        <div class="clearfix mrpc-company-line2">
          <span v-if="mainData.job" class="mrpc-job-name inlineblock font14pl5A646E">游戏开发工程师（Python）初级</span>
          <span v-if="mainData.course">4门课程</span>
          <span  class="mrpc-match-rate inlineblock  font14pl5A646E">匹配度：
            <span class="font20pl3a3c50">70%</span>
          </span>
          <el-button class="floatr" @click="handleClick()">查看详情</el-button>
        </div>
        <div class="mrpc-progress">
          <el-progress :percentage="70" :width="340" :stroke-width="16" :show-text="false"></el-progress>
        </div>
      </div>
    </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        imgStyle:{},
        outerStyle:{},
        boxStyle:{}
      }
    },
    methods:{
      handleClick(evt){
        // evt.stopPropagation();
        this.$emit('clickButton')
      }
    },
    props:{
      mainData:Object
    },
    created(){
      this.$fn.initStyle(this,'mainData',['imgStyle','outerStyle','boxStyle'])
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
