<template>
  <div class="info_block bdr ">
    <div class="info_form_title">
      <div class="infoBlock__dot--white"></div>
      <div class="infoBlock__dot--white"></div>
    </div>
    <div class="text_area">
      <infoMain></infoMain>
    </div>
  </div>
</template>

<script>
  import infoMain from './06_info_main'
  export default {
    name: "left",
    data() {
      return {}
    },
    components:{
      infoMain:infoMain
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../assets/style/baseConstScss.scss";

  .info_block {
    width: 240px;
    height: 358px;
    border: 1px solid #999;
    overflow: hidden;
  }

  .info_form_title {
    background-color: $cy;
    display: flex;
    justify-content: space-around;
    align-items: center;
    height: 40px;
    border-bottom: 1px solid #999;
  }
  .infoBlock__dot--white{
    width: 16px;
    height: 16px;
    background-color: white;
    border-radius: 50%;
    border:1px solid #999;
  }
  .text_area{
    padding: 0 16px;
  }
</style>
