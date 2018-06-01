<template>
  <div class="clearfix info_content mw hc">
    <div class="info_left fl ftc">
      <div class="icon_box dib">
        <img class="info_icon" :src="$myConst.httpUrl + main_data.avatar" alt="">
      </div>
      <div class="info_left_index ftc font1_14_b4">第{{main_data.rank||"？"}}名</div>
    </div>
    <div class="info_right">
      <div class="info_right_text font1_18_6">{{main_data.nickname}}</div>
      <div class="info_right_content">
        <div class="info_tab_box dib">
          <div v-for="item in main_data.technologys" :key="item.id" class="info_tab dib ftc font1_14_f">{{item}}</div>
        </div>
        <div class="info_button dib fr">
          <!--<a href="" target="_blank">-->
          <BlueButton><span class="info_right_button font1_24_f ">查看详情</span></BlueButton>
          <!--</a>-->
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import BlueButton from '../00_common/04_blue_button'

  export default {
    data() {
      return {
        avatar: ''
      }
    },
    components: {
      BlueButton: BlueButton,
    },
    props: {
      main_data: {}
    }
  }
</script>
<style scoped lang="scss">
  .info_left {
    width: 160px;
    padding-top: 30px;
  }

  .icon_box {
    height: 100px;
    width: 100px;
  }

  .info_icon {
    width: 100px;
    height: 100px;
    border-radius: 50px;
  }

  .info_left_index {
    padding: 10px 0 6px 0
  }

  .info_right {
    margin-left: 160px;
    padding: 50px 30px 0 0;
  }

  .info_right_text {
    font-weight: bold;
  }

  .info_right_content {

  }

  .info_tab_box {
    width: 580px;
    padding: 30px 0;
    .info_tab {
      width: 100px;
      height: 30px;
      line-height: 30px;
      border-radius: 15px;
      background-color: #acbacf;
      margin-right: 15px;
      box-sizing: border-box;
    }
    .info_tab:nth-child(5n) {
      margin-right: 0;
    }
    .info_tab:nth-child(n+6) {
      margin-top: 10px;
    }
  }

  .info_right_button {
    padding-left: 67px;
    padding-right: 67px;
  }

</style>

