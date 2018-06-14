<template>
  <div class="swiper-slide slide-2"
       :style="{'background-image':url}">
    <div class="time_block a">
      <img class="time_icon vm"
           src="../img/时间icon.png"
           alt="">
      <span class="time dib vm">5/31-6/13</span>
    </div>
    <MiddleContent :main_data="main_data[2]"></MiddleContent>
    <BM class="bm a"
        :image_url="main_data.photo2"></BM>
  </div>
</template>

<script>
import MiddleContent from './00_commen/01_middle_content'
import BM from './00_commen//02_bottom_img';
export default {
  data () {
    return {

    }
  },
  props: {},
  methods: {},
  created () { },
  components: {
    MiddleContent: MiddleContent,
    BM: BM
  }
}

</script>

<style scoped lang="scss">

.time_block {
  top: 2.99295774%;
}
.time_icon {
  margin: 0 0.2rem;
  height: 0.32rem;
  width: 0.32rem;
}
.time {
  font: 300 0.32rem/0.32rem 'MicroSoft YaHei';
  color: white;
}
</style>
