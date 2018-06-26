<template>
  <div class="slid_03">
    <div class="rules_title ftc">
      <span class="rules_title_button">活动说明</span>
    </div>
    <div class="a text_container">
      <div class="text_area  hc">
        <h2>1.活动时间</h2>
        <p>同世界杯赛程同步，截止到2018年7月12日晚23:00</p>
        <h2>2.活动内容</h2>
        <p>参与世界杯内容答题，获取积分兑换豪礼</p>
        <h2>3.活动细节</h2>
        <p>（1）答题获取积分，通过转发微信好友或朋友圈，积分翻倍</p>
        <p>（2）投注积分赌球，可投注任一你心仪的国家，输赢倍率同意为1.0，没赢一场投注积分翻倍</p>
        <p>（3）球赛结束后/次日10：30公布结果，每场球赛投注于赛程开始后暂停</p>
        <p>（4）扫码参与荣新大数据积分换豪礼兑换</p>
        <h2>4.奖品说明</h2>
        <p>一等奖：价值
          <span class="bonuse">10000元</span>活动奖励（1名）</p>
        <p>二等奖：价值
          <span class="bonuse">5000元</span>活动好礼（2名）</p>
        <p>三等奖：价值
          <span class="bonuse">2999元</span>活动好礼（积分满1000）</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {

    }
  },
  props: {},
  methods: {},
  created () { },
  components: {

  }
}
</script>

<style scoped lang="scss">
@import '../scss/_base';
.bonuse {
  color: $red;
}
h2 {
  font-size: 0.28rem;
  color: #213888;
}
p {
  font-size: 0.24rem;
  color: #4b4b4b;
}
.text_container {
  width: 100%;
  top: 14.08%;
  height: 72.447%;

  .text_area {
    height: 100%;
    width: 5rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
}
.slid_03 {
  background: url('../img/11_rules_bg.png');
  background-color: white;
  background-size: 100% 100%;
}
.rules_title {
  margin: 0.5rem 0 0.2rem;
}
.rules_title_button {
  color: white;
  font-weight: 500;
  font-size: 0.38rem;
  padding: 0.1rem 0.3rem;
  border-radius: 4rem;
  background: url('../img/12_rules_button.png');
}
</style>
