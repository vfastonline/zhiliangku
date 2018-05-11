<template>
  <div class="all_product">
    <div  class="mainwidth incenter product_card_container">
      <productCard v-for="(item,index) in mainData" :key="index" :mainData="item" class="item rise"></productCard>
    </div>
    <noInfo v-show="show" :str="'暂无商品，敬请期待'"></noInfo>
  </div>
</template>
<style scoped>
  .all_product {
    background: #fafafa;
    margin-top: 83px;
  }

  .product_card_container {
    display: flex;
    flex-wrap: wrap;
  }
  .no_product{
    min-height: 400px;
    line-height: 400px;
  }
</style>
<style lang="scss">
  .item {
    flex: 0 1 33.33%;
  }
</style>

<script>
  import productCard from './03-productCard.vue'
  import noInfo from './06-noInfo'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        mainData: [],
        show:false
      }
    },
    props: {
      type: Number
    },
    watch: {
      type: function () {
        console.log(123)
        this.getData();
      }
    },
    methods: {
      getData() {
        this.$get('/integral/all/goods?gtype=' + this.type).then(res => {
          this.mainData = res.data.data;
          this.$fn.addString(this.$myConst.httpUrl, res.data.data, ['images'])
          if(this.mainData.length){
            this.show=false;
          }else{
            this.show=true
          }
          console.log(this.mainData)
        })
      }
    },
    created() {
      console.log(this)
      this.getData()
    },
    components: {
      productCard: productCard,
      noInfo:noInfo
    }
  }

</script>
