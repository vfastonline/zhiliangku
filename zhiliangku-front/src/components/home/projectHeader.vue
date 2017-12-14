<template>
  <div class="project-header zindex10">
    <div class="ph-content mainwidth inmiddle clearfix">
      <div class="main">
        <div class="inner">
          <div class="ph-content">
            <span class="ph-tag pointer"> <a href="/tracks/courseSelect/"> 课程</a></span>
            <span class="ph-tag pointer">直播</span>
            <span class="ph-tag pointer"> <a href="/tracks/pathList/">职业路径</a></span>
            <span class="ph-tag pointer">社区</span>
            <span class="ph-tag last pointer">线下课程</span>
            <!--<span class="ph-search">
              <input type="text">
              <img class="phs-magnifier" src="../../assets/img/icons/Search-magnifier.svg" alt="">
            </span>-->
          </div>
        </div>
      </div>
      <div class="left">
        <img class='ph-logo' src='../../assets/img/icons/Logo.png' alt="">
      </div>
      <div class="right">
        <el-button @click="changShow()" class="ph-button" type="primary" :style="buttonStyle" round>岗位匹配</el-button>
        <span class="user-info ">
          <img  class="user-icon pointer" src="../../assets/img/user-icon.jpg" alt="">
        </span>
        <transition name='fade'>
        <postMatch v-if="show" class="floatr"></postMatch>
        </transition>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "projectHeader",
  data() {
    return {
      show: false,
      msg: "Welcome to Your Vue.js App",
      buttonStyle: {
        width: "121px",
        height: "42px",
        background: "23B8FF",
        "font-family": "PingFangSC-Light",
        "font-size": "18px"
      }
    };
  },
  methods: {
    changShow() {
      this.show = !this.show;
    }
  },
  created() {},
  mounted() {}
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang='scss'>
.left {
  // background: red;
  width: 132px;
  float: left;
  margin-left: -100%;
  height: 100%;
  /*position: relative;*/
  /*left:-100px;*/
}
.fade-enter-active,
.fade-leave-active {
  transition: all 0.25s ease;
}
.fade-enter,
.fade-leave-active {
  opacity: 0;
}
.main {
  // background: blue;
  width: 100%;
  float: left;
  height: 100%;
}

.right {
  // background: red;
  width: 285px;
  float: left;
  margin-left: -285px;
  height: 100%;
  /*position:relative;*/
  /*right:-200px;*/
}

//新增inner元素
.inner {
  margin-left: 132px;
  margin-right: 285px;
}
.ph-content {
  padding-left: 50px;
}
.project-header {
  width: 100%;
  height: 70px;
  // background: brown;
  position: relative; // background: #FFFFFF;
  border-bottom: 1px solid #cccccc;
  box-shadow:0 3px 2px rgba(0,0,0,0.1);
  .ph-content {
    height: 70px;
    line-height: 70px;
    // background: skyblue;
  }
  .ph-logo {
    width: 132px;
    height: 48px;
    vertical-align: middle;
  }
  .ph-tag {
    opacity: 0.8;
    font-family: PingFangSC-Light "微软雅黑" "宋体";
    font-size: 18px;
    color: #3a3c50;
    margin-right: 35px;
    vertical-align: text-bottom;
  }
  .ph-search {
    margin-right: 5.556%;
    vertical-align: text-bottom;
  }
  .phs-magnifier {
    vertical-align: text-bottom;
    width: 24px;
    height: 24px;
  }
  .ph-button {
    vertical-align: middle;
  }
  .user-info {
    float: right;
  }
  .user-icon {
    height: 48px;
    width: 48px;
    vertical-align: middle;
    border-radius: 24px;
  }
}
</style>
