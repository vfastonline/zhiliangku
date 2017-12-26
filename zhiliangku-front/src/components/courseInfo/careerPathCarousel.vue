<template>
  <div class="carousel zindex1">
    <el-carousel height='670px' :interval="50000" indicator-position="none">
      <el-carousel-item v-for="item in urls" :style="{'background':'url('+item.pathwel+')'+'center center no-repeat fiexd'}" :key="item.id">
        <img class="carouselimg zindex1" :src="item.pathwel" alt="">
        <div class="mainwidth incenter cpc-word-div inmiddle  zindex10">
          <div class="cpcw-path font20pl3a3c50">职业路径</div>
          <div class="cpcw-path-name font20pm3a3c50">机器学习工程师</div>
          <div class="cpcw-path-desc font14pr3a3c50">掌握人工智能、大数据应用背后的核心技术</div>
          <div>
            <el-button class="font16pr23b8ff" :style="buttonStyle">了解详情</el-button>
          </div>
        </div>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        urls: [],
        address: '/slides/list?category=1',
        buttonStyle: {
          'border': ' 2px solid #23B8FF',
          'border-radius': ' 5px',
          'padding': '8px 32px',
          'background':'none'
        }
      }
    },
    created() {
      if (this.requestUrl) {
        this.address = this.requestUrl;
      }
      this.$get(this.address).then(
        res => {
          this.urls = this.$fn.addString(this.$myConst.httpUrl, res.data.data, 'pathwel')
        }
      )
    },
    props: {
      requestUrl: String
    }
  }

</script>

<style scoped>
  .carousel {
    width: 100%;
    height: 670px;
  }

  .carouselimg {
    width: 100%;
    height: 100%;
  }

  .cpc-word-div {
    margin-top: 95px;
  }

  .cpcw-path {
    margin-bottom: 24px;
  }

  .cpcw-path-desc {
    margin-bottom: 56px;
  }

</style>
