<template>
  <div @mouseenter="mouseenter()" v-on:mouseleave="mouseleave()" class="uim-container floatr rised">
    <div class="uim-username pointer">
      <span>
        <a href="/personal_center/page/#/occupational/matchingRate">{{nickname}}</a>
      </span>
    </div>
    <a href="/personal_center/page/#/myCourse/recentlyLearing">
      <div class="uim-select pointer">
        <span>我的课程</span>
      </div>
    </a>
    <a href="/personal_center/page/#/mySettings/baseInfo">
      <div class="uim-select pointer">
        <span>个人设置</span>
      </div>
    </a>
    <a href="/integral/redeem/">
      <div class="uim-select pointer">
        <span>积分兑换</span>
      </div>
    </a>
    <div class="uim-select pointer" @click="logout()">
      <span>退出登录</span>
    </div>
    <!--<div @click="logout()">退出登录</div>-->
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .uim-container {
    /*padding:24px 0 9px 0;*/
    position: absolute;
    top: 70px;
    right: 0px;
    width: 229px;
    line-height: 32px;
    background: white;
  }

  .uim-container .uim-username {
    width: 230px;
    height: 70px;
    line-height: 70px;
    font-family: 'PingFangSC-Light';
    font-size: 16px;
  }

  .uim-container .uim-username span {
    margin-left: 32px;
  }


  .uim-container {
    overflow: hidden;
    z-index: 1000;
  }

  .uim-container .uim-select {
    width: 239px;
    height: 40px;
  }

  .uim-select:hover {
    background: #fafafa;
  }

  .uim-container .uim-select span {
    width: 24px;
    height: 40px;
    line-height: 40px;
    margin: 9px 133px 9px 32px;
    font-family: 'PingFangSC-Light';
    font-size: 16px;
  }

  .uim-container .uim-select:hover span {
    color: #23B8FF;
  }

</style>
<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        nickname: "user_menu"
      }
    },
    created() {
      this.nickname = localStorage.nickname;
    },
    methods: {
      mouseleave(){
        this.$emit('mouseleave')
      },
      mouseenter(){
        this.$emit('mouseenter')
      },
      logout() {
        this.$post('/customuser/logout').then(res => {
          if (!res.data.err) {
            this.$parent.$emit('logout')
          }
        })
      },
    }
  }

</script>
