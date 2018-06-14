<template>
  <div class="swiper-slide slide-1"
       :style="{'background-image':url}">
    <div class="slide_1_content a ftc">
      <img class="studen_icon db hc"
           v-lazy="$myConst.httpUrl+main_data.avatar"
           alt="">
      <div class="send_word  ftc">寄语</div>
      <div class="ftc line_1"
           v-html="main_data[1].remark"></div>
      <div class="ftc"
           v-html="main_data[1].english"></div>
    </div>
  </div>
</template>
<style lang="scss">
.slide-1 {
  .line_1 {
    font: 300 0.38rem/0.38rem 'MicroSoft YaHei';
    margin-bottom: 0.2rem;
  }
  .line_2 {
    font: 300 0.18rem/0.18rem 'MicroSoft YaHei';
    opacity: 0.5;
  }
}
</style>

<style lang="scss" scoped>
.slide_1_content {
  width: 100%;
  top: 9.68%;
}
.studen_icon {
  width: 1.8rem;
  height: 1.8rem;
  margin-bottom: 0.54rem;
}
.send_word {
  font: normal normal 400 0.64rem/0.64rem 'MicroSoft YaHei';
  margin-bottom: 0.54rem;
  color: #333333;
}
</style>

<script type="text/ecmascript-6">

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
</style>
