<template>
  <div class="product_container ">
    <div class="product_img" v-lazy:background-image="mainData.images" ></div>
    <ul class="product_info">
      <li class="fontcenter">
        <span  class="font14pr23b8ff">{{mainData.gtype_name}}</span>
      </li>
      <li class="fontcenter">
        <span @click="goDetailInfo" class="font20pl3a3c50 pointer">{{mainData.name}}</span>
      </li>
      <li class="fontcenter ">
        <span class="font20pl23b8ff">{{mainData.integral}}</span>
      </li>
    </ul>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .product_img {
    height: 320px;
    width: 320px;
    display: block;
    margin: auto;
    margin-bottom:32px;
    background-size: cover;
    background-position: center;
  }
  .product_container{
    height: 500px;
    width:383px;
    box-sizing: border-box;
    padding:32px 32px 24px 32px;
  }
  .product_info{
    margin: auto;
  }
</style>
<script>
  import VueLazyLoad from 'vue-lazyload'
  Vue.use(VueLazyLoad, {})
  export default {
    name: 'HelloWorld',
    data() {
      return {}
    },
    props: {
      mainData:Object,
    },
    methods: {
      goDetailInfo(){
        window.open('/integral/goods/detail/?id='+this.mainData.id)
      }
    },
    created() {

    },
    components: {

    }
  }

</script>
