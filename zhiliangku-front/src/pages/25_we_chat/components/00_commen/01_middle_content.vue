<template>
  <div class="middle_content a">
    <img class="frame_img"
         src="../../img/01_frame.png"
         alt="">
    <div class="box a ftc"
         v-html="main_data.remark"></div>
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
.middle_content {
  top: 24.824%;
  width: 100%;
}
.frame_img {
  width: 100%;
  z-index: -1;
  height: 3.3rem;
}
.box {
  width: 100%;
  height: 2.48rem;
  font: 300 0.4rem/0.6rem 'MicroSoft YaHei';
  color: #333333;
  top: 50%;
  transform: translate(0, -50%);
}
</style>
