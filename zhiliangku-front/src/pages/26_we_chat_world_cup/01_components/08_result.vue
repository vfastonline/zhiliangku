<template>
  <div class="result_info">
    <div class="info_container">
      <div class="ftc">
        <img class="top_image"
             src="../img/13_win.png"
             alt="">
      </div>
      <div class="result_title ">
        <div class="ftc success">恭喜你猜球成功！</div>
        <div class="ftc mark">获得100积分</div>
      </div>
      <div class="text_info">

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
}
.result_info {
  height: 100%;
  width: 100%;
  background: rgba(0, 0, 0, 0.8);
}
</style>
