<template>
  <div class="subtitle inmiddle">
      <div class="entitle inmiddle">
          {{enTitle}}
      </div>
      <div class="zhtitle1  font24pr2C343B fontcenter">
              {{title}}
      </div>
      <div class="zhtitle2  ">
              <div class="zhtitle2  font14pr2C343B fontcenter" >{{slogon}}</div>
              <div class="subtitle-link"><a class=" font14pl5A646E" href="">更多>></a></div>
      </div>
  </div>
</template>
<style lang='scss'>
.subtitle {
  width: 1152px;
  height: 73px;
  line-height: 73px;
  position: relative;
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
   .subtitle-link{
    position: absolute;
    right: 0px;top:0px;
      line-height:32px;
    }
    .font14pl5A646E{
    font-family: PingFangSC-Light;
    font-size: 14px;
    color: #5A646E;
    letter-spacing: 0.4px;
}
  
}
</style>
<script>
export default {
  data() {
    return {};
  },
  props: {
    title: String,
    slogon: String,
    enTitle: String
  }
};
</script>


