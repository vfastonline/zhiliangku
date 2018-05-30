<template>
  <div class="">
    <div class="timerbox-container timerbox-line">
      <div class="tbc-dote"></div>
      <div v-if="!first" class="vertical-line tbc-line-up"></div>
      <div class="vertical-line tbc-line-down"></div>
      <div class="tbc-time-tag">{{mainData.end_time}}</div>
      <div class="tbc-title">
        <span v-if="!config.linkTitle" class="font18pr5a646e">{{mainData[config['title']]}}</span>
        <a v-if="config.linkTitle" :href="mainData.url">
          <span class="font18pr5a646e">{{mainData[config['title']]}}</span>
        </a>
        <span>{{mainData.start_time}}-{{mainData.end_time}}</span>
      </div>
    </div>
    <div class="tbc-content timerbox-container">
      <slot></slot>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        end_time1: '',
        end_time2: '',
        start_time2: ''
      }
    },
    props: {
      first: Boolean,
      mainData: Object,
      config: Object
    },
    methods: {
      getDate(data, str) {
        if (!data) {
          return
        }
        var time = new Date(data);
        if (str == 'year') {
          return time.getFullYear()
        }
        if (str == 'month') {
          return time.getFullYear() + '年' + time.getMonth().length > 1 ? time.getMonth() : ('0' + time.getMonth()) +
            '月'
        }
      }
    },
    created() {
      // var defaultConfig={time1:'month',time2:'month'};
      // for( var k in this.config){
      //   defaultConfig[k]=this.config[k]
      // }
      // this.config=defaultConfig;
      // if (this.mainData) {
      //   this.start_time2= this.getDate(this.mainData.start_time,this.config.time2)
      //   this.end_time2=this.getDate(this.mainData.end_time,this.config.time2)
      // }
    }
  }

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .timerbox-container {
    padding-left: 64px;
    margin-left: 40px;
    position: relative;
  }

  .timerbox-line {
    line-height: 44px;
    height: 44px;
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
    z-index: 10;
  }

  .vertical-line {
    width: 2px;
    background: #eef0f2;
    /* background:red; */
    height: 50%;
    position: absolute;
    left: 0;
    z-index: 1;
  }

  .tbc-line-down {
    bottom: 0;
  }

  .tbc-line-up {
    top: 0;
  }

  .tbc-time-tag {
    width: 70px;
    position: absolute;
    left: -72px;
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
    padding-bottom: 32px;
  }

</style>
