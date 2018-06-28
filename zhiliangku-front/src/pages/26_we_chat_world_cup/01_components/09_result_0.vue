<template>
  <div @touchmove="no_move"
       class="result_info a">
    <div class="info_container a">
      <div class="r segement"
           v-if="main_data.value>0">
        <div class="ftc text0">恭喜你猜球成功</div>
        <!-- <div class="ftc text1"></div> -->
        <div class="ftc text2">请注意查看积分变化</div>
        <div class="r ftc text4">
          <div class="text5 a">
            {{main_data.value}}
          </div>
          <img class="text6"
               src="../img/14_win.png"
               alt="">
        </div>
      </div>
      <div class="r segement"
           v-if="main_data.value<=0">
        <div class="fail_block">
          <div class="ftc text0">很遗憾猜球失败</div>
          <div class="ftc text1">想转运就再来一次吧</div>
          <div class="ftc">
            <img class="text7"
                 src="../img/15_fail.png"
                 alt="">
          </div>
        </div>
      </div>
      <img @touchstart="$emit('close')"
           class="a close"
           src="../img/17_close.png"
           alt="">
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {

    }
  },
  props: {
    main_data: {},
    bet_info: {}
  },
  methods: {
    no_move (e) {
      e.stopPropagation();

    }
  },
  created () { console.log(this.main_data.value) },
  components: {

  }
}
</script>

<style scoped lang="scss">
@import '../scss/_base';
.segement {
  height: 100%;
  width: 100%;
}
.close {
  left: 50%;
  top: 105%;
  transform: translate(-50%, 0);
}
.text0,
.text1,
.text2 {
  color: white;
}
.text0 {
  font-size: 0.34rem;
  padding-top: 0.7rem;
}
.text1,
.text2 {
  margin-top: 0.2rem;
  font-size: 0.24rem;
}
.text4 {
  margin-top: 0.4rem;
}
.text5 {
  font-size: 0.32rem;
  left: 50%;
  top: 0;
  transform: translate(-50%, -40%);
  color: $yellow;
}
.text6 {
  height: 1.8rem;
}
.text7 {
  margin-top: 0.4rem;
  height: 3.2rem;
}
.text_info {
  width: 3.8rem;
  height: 1.15rem;
}
.mark {
  color: #ffff01;
  font-size: 0.22rem;
}
.success {
  color: white;
  font-size: 0.36rem;
}
.result_title {
  height: 0.82rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
.top_image {
  height: 2.25rem;
}
.info_container {
  background-color: green;
  height: 6rem;
  width: 5rem;
  border-radius: 0.3rem;
  left: 50%;
  top: 40%;
  transform: translate(-50%, -50%);
  background: url('../img/16_red_pakage.png');
  background-size: 100% 100%;
}
.result_info {
  height: 100%;
  width: 100%;
  background: rgba(0, 0, 0, 0.8);
  // background-color: red;
}
</style>
