<template >
  <div class="carousel ">
    <el-carousel :style="{ width: '100%'}" :interval="5000">
      <el-carousel-item v-for="item in urls"
                        :key="item.id">
        <!--<img class="carouselimg" :src="item.pathwel" alt=""> -->
        <div v-lazy:background-image="item.pathwel"
             :style="{height:'100%',width:'100%'
      ,'background-repeat':'no-repeat','background-size':'cover','background-position':'center'}"></div>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>
<script>
  import Vue from 'vue'
  import {Carousel, CarouselItem} from 'element-ui'
  import VueLazyLoad from 'vue-lazyload'

  Vue.use(Carousel)
  Vue.use(CarouselItem)
  Vue.use(VueLazyLoad)
  export default {
    data() {
      return {
        urls: [],
        address: '/slides/list?category=1'
      }
    },
    created() {
      if (this.requestUrl) {
        this.address = this.requestUrl
      }
      this.$get(this.address).then(
        res => {
          this.urls = this.$fn.addString(this.$myConst.httpUrl, res.data.data, 'pathwel')
        }
      )
    },
    components: {},
    props: {
      requestUrl: String
    }
  }
</script>

<style lang="scss">
  .carousel {
    height: 720px;
    width: 100%;
    .el-carousel__arrow {
      border: none;
      outline: 0;
      padding: 0;
      margin: 0;
      height: 36px;
      width: 36px;
      cursor: pointer;
      -webkit-transition: .3s;
      transition: .3s;
      border-radius: 50%;
      /*background-color: rgba(31, 45, 61, .11);*/
      background-color: rgba(31, 45, 61, 0);
      color: #fff;
      position: absolute;
      top: 50%;
      z-index: 10;
      -webkit-transform: translateY(-50%);
      transform: translateY(-50%);
      text-align: center;
      font-size: 12px
    }

    .el-carousel__arrow--left {
      left: 136px
    }

    .el-carousel__arrow--right {
      right: 136px
    }

    .el-carousel__arrow:hover {
      /*background-color: rgba(31, 45, 61, .23)*/
      background-color: rgba(31, 45, 61, 0)
    }
    .el-carousel__button {
      display: block;
      opacity: .48;
      width: 20px;
      height: 20px;
      -webkit-border-radius: 50%;
      -moz-border-radius: 50%;
      border-radius: 50%;
      background-color: #fff;
      border: none;
      outline: 0;
      padding: 0;
      margin: 0;
      cursor: pointer;
      -webkit-transition: .3s;
      transition: .3s
    }

    .el-icon-arrow-left ,.el-icon-arrow-right{
      margin-top: -70px;
      font-size: 140px;
    }
    .el-carousel__container {
      height: 720px;
    }

    .carouselimg {
      width: 100%;
      height: 100%;
    }
  }
</style>
