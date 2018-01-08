<template>
  <div class="">
    <div class="timerbox-container timerbox-line">
      <div class="tbc-dote"></div>
      <div v-if="!first" class="vertical-line tbc-line-up"></div>
      <div class="vertical-line tbc-line-down"></div>
      <div class="tbc-time-tag">{{mainData.end_time}}</div>
      <div class="tbc-title">
        <span v-if="!config.linkTitle" class="font18pr5a646e">{{mainData[config['title']]}}</span>
        <a v-if="config.linkTitle" :href="mainData.url"><span class="font18pr5a646e">{{mainData[config['title']]}}</span></a>
        <span>{{mainData.start_time}}-{{mainData.end_time}}</span>
      </div>
    </div>
    <div class="tbc-content timerbox-container">
      <slot ></slot>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    },
    props:{
      first:Boolean,
      mainData:Object,
      config:Object
    }
  }
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .timerbox-container {
    padding-left: 64px;
    margin-left:40px;
    position: relative;
  }
  .timerbox-line{
    line-height:44px;
    height:44px;
  }
  .tbc-dote {
    box-sizing: border-box;
    height: 12px;
    width: 12px;
    background: white;
    border: 2px solid #d5dadf;
    position: absolute;
    top: 50%;
    margin-top: -6px;
    left: -5px;
    /* background: seagreen; */
    border-radius: 50%;
    z-index:10;
  }
  .vertical-line{
    width:2px;
    background: #eef0f2;
    /* background:red; */
    height:50%;
    position: absolute;
    left:0;
    z-index: 1;
  }
  .tbc-line-down{
    bottom:0;
  }
  .tbc-line-up{
    top:0;
  }
  .tbc-time-tag {
    width: 50px;
    position: absolute;
    left: -68px;
    top: 50%;
    transform: translate(0, -50%);
  }
  
  .tbc-title {
    display: flex;
    justify-content: space-between;
  }

  .tbc-content {
    border-left: 2px solid #eef0f2;
    /* background: salmon; */
    padding-bottom:32px;
  }

</style>
