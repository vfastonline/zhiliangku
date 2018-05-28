<template>
  <section class="join_us" v-lazy:background-image="$myConst.httpUrl+'/media/image/static/index_02_wave.png'">
    <WhiteButton @click.native="join_us">加入我们</WhiteButton>
    <WhiteButton @click.native="show_img=true">用户手册</WhiteButton>
    <el-dialog :visible.sync="show_img" width="390px">
      <img class="we_chat_img" src="./img/we_chat_img.png" alt="">
      <p class="info_container font1_14_f ftc">
        请使用微信扫描二维码进入 <br>
        智量酷
      </p>
    </el-dialog>
  </section>
</template>
<style>
  .we_chat_img {
    height: 350px;
    width: 350px;
  }
  .info_container{
    border-radius: 50px;
    margin: auto;
    padding: 6px 0;
    width: 300px;
    border-radius: 50px;
    background-color: rgba(35,35,35,0.85);
  }

</style>
<script>
  import WhiteButton from '../../components/00_common/03_white_button'
  import Vue from 'vue'
  import Bus from '../../assets/js/02_bus'
  import {Dialog} from 'element-ui'

  Vue.use(Dialog)
  Vue.use(window.VueLazyload)
  export default {
    name: "join_us",
    data() {
      return {
        show_img: false
      }
    },
    methods: {
      join_us() {
        Bus.$emit('specify_display', {show_key: 'log_up', title_key: '用户注册'})
      }
    },
    components: {
      WhiteButton: WhiteButton
    }
  }
</script>

<style scoped>
  .join_us {
    margin-top: 160px;
    height: 170px;
    padding: 52px 0;
    background-position: center center;
    background-size: cover;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
  }
</style>
