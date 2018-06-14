<template>
  <div class="swiper-slide slide-4"
       :style="{'background-image':url}">
    <MiddleContent :main_data="main_data[3]"></MiddleContent>
    <BM class="bm a"
        :image_url="main_data.photo4"></BM>
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
</style>
