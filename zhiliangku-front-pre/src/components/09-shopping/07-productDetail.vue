<template>
  <div class="detail_container mainwidth incenter">
    <div class="content_main">
      <div v-lazy:background-image="mainData.images" class="img_container detail_img">
      </div>
      <ul class="info_list">
        <li class="font20pl5A646E">{{mainData.gtype_name}}</li>
        <li class="font20pl3a3c50">{{mainData.name}}</li>
        <li>
          <span class="integral num">{{mainData.integral}}积分</span>
          <span class="integral1">请勿刷分，违者积分清零</span>
        </li>
        <li>
          <el-button @click="convertion" class="convert_butotn">立即兑换</el-button>
          <span class="remain">剩余{{mainData.residue_stock}}</span>
          /
          <span class="font14pl5A646E">共{{mainData.stock}}</span>
        </li>
      </ul>
    </div>
    <div class="good_resume">
      <div class="title_info">商品详情</div>
      <div v-html="mainData.detail">
      </div>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .detail_container {
    margin-top: 70px;
  }

  .content_main {
    display: flex;
    justify-content: space-between;
    margin-bottom: 64px;
  }

  .detail_img {
    height: 360px;
    width: 360px;
    flex: 0 0 360px;
  }

  .integral {
    font-size: 20px;
    font-family: "PingFangSC-Light", "Microsoft YaHei";
    color: #E57373;
  }
  .integral1{
    font-size: 14px;
    font-family: "PingFangSC-Light", "Microsoft YaHei";
    color: #E57373;
  }
  .info_list {
    margin-left: 40px;
    flex-grow: 1;
  }

  .info_list li {
    margin-bottom: 24px;
  }

  .info_list li:nth-child(1) {
    margin-bottom: 8px;
  }

  .num {
    margin-right: 64px;
  }

  .convert_butotn {
    margin-right: 24px;
  }

  .remain {
    font-size: 14px;
    color: #09B7FF;
  }

  .title_info {
    margin-bottom: 40px;
  }

</style>
<script>
  import VueLazyLoad from 'vue-lazyload'
  Vue.use(VueLazyLoad, {})
  export default {
    name: 'HelloWorld',
    data() {
      return {
        mainData: {

        }
      }
    },
    props: {

    },
    methods: {
      convertion() {
          this.$post('/integral/exchange/goods',{custom_user_id:localStorage.uid,goods_id:this.mainData.id})
          .then(res=>{
              if(res.data.msg=='success'){
                  this.$fn.showNotice(this,'您已兑换成功','success');
                  this.mainData.residue_stock--;
              }
          })
      },
      getData() {
        this.$get('/integral/goods/detail/info?goods_id=' + this.$fn.funcUrl('id')).then(res => {
          this.mainData = res.data.data;
          this.$fn.addObjString(this.$myConst.httpUrl, this.mainData, 'images')
        })
      }
    },
    created() {
        this.getData()
    },
    components: {

    }
  }

</script>
