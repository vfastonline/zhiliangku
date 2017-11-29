<template>
  <div>
      <div class="hc-imgContainer">
          <img class="hcic-img" src="../assets/img/hotCourse.png" alt="">
          <div class="hcic-tag">
              <el-button>默认按钮</el-button>
          </div>
      </div>
      <ul class="hc-info">
          <li class="hci-li font14pl2C343B textellipsis">Python 接口测试框架实战与自动化进阶</li>
          <li class="hci-li textellipsis">
              <img src="../assets/img/user-icon.jpg" alt="">
              <span class="font14prb2bbbf hcil-teachername">Annaa</span>
            </li>
      </ul>
  </div>
</template>
<style lang="scss">
.hc-imgContainer,
.hcic-img {
  width: 276px;
  height: 153px;
}
.hcic-tag {
  display: none;
}
.hc-info {
  width: 276px;
  height: 80px;
}
.hci-li {
  height: 40px;
  line-height: 40px;
  margin-left: 16px;
  img {
    width: 32px;
    height: 32px;
    vertical-align: middle;
  }
}
</style>
<script>
export default {
  data() {
    return {};
  },
  props:{
      imgsrc:String,
      tags:Array,
      subtitle:String,
      teacherIcon:String,
      teacherName:String,
  }
};
</script>


