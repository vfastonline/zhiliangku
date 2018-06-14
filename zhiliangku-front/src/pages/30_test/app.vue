<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <div class="swiper-container">
        <div class="swiper-wrapper">
          <div class="swiper-slide swiper1">Slide 1</div>
          <div class="swiper-slide swiper2">Slide 2</div>
          <div class="swiper-slide swiper3">Slide 3</div>
        </div>
        <!-- 如果需要分页器 -->
        <div class="swiper-pagination"></div>

        <!-- 如果需要导航按钮 -->
        <div class="swiper-button-prev"></div>
        <div class="swiper-button-next"></div>

        <!-- 如果需要滚动条 -->
        <div class="swiper-scrollbar"></div>
      </div>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>
.swiper-wrapper,
.swiper-container {
  height: 700px;
  width: 700px;
}
.swiper1 {
  background-color: red;
}
.swiper2 {
  background-color: skyblue;
}
.swiper3 {
  background-color: salmon;
}
</style>
<script>
import MyHeader from '../../components/01_header_footer/01_header'
import F from '../../components/01_header_footer/03_footer'

export default {
  data () {
    return {}
  },
  components: {
    MyHeader: MyHeader,
    F: F
  },
  mounted () {
    this.mySwiper = new window.Swiper('.swiper-container', {
      autoplay: true,//可选选项，自动滑动
      onInit: function (swiper) {
        debugger
        //Swiper初始化了
        //alert(swiper.activeIndex);提示Swiper的当前索引
      }
    })
  }
}

</script>
