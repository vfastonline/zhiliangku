<template>
  <div class="sbuitle-container">
    <div class="subtitle ">
      <div :style="msg.enTitleStyle" class="entitle incenter ">
        {{msg.enTitle}}
      </div>
      <div class="inmiddle">
      <div :style="msg.myStyle" class="zhtitle1  font24pr2C343B fontcenter ">
        {{msg.title}}
      </div>
      <div class="zhtitle2  ">
        <div :style="msg.myStyle" class="zhtitle2  font14pr2C343B fontcenter ">{{msg.slogon}}</div>
        <div class="subtitle-link">
          <a :style="msg.myStyle" class=" font14pl5A646E" :href="msg.linker">更多>></a>
        </div>
      </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    data() {
      return {};
    },
    props: {
      msg: Object,
    },
    created(){
      if(this.msg.myStyle){
        for(var k in this.msg.myStyle){
          document.getElementsByClassName('.subtitle-container')
        }
      }
    }
  };

</script>

<style lang='scss'>
.sbuitle-container{
  padding-top:40px;
  height:100px;
}
  .subtitle {
    width: 1152px;
    height: 73px;
    line-height: 73px;
    position: relative;
    left: 0px;
    right: 0px;
    margin: auto;
    .entitle {
      text-align: center;
      opacity: 0.5;
      font-family: Copperplate-Bold;
      font-size: 72px;
      color: #eef0f2;
    }
    .zhtitle1 {
      margin-top: 6px;
      height: 33px;
      line-height: 33px;
    }
    .zhtitle2 {
      margin-top: 8px;
      height: 32px;
      line-height: 33px;
      letter-spacing: 2px;
      position: relative;
    }
    .subtitle-link {
      position: absolute;
      right: 0px;
      top: 0px;
      line-height: 32px;
    }
    .font14pl5A646E {
      font-family: PingFangSC-Light;
      font-size: 14px;
      color: #5A646E;
      letter-spacing: 0.4px;
    }
  }

</style>
