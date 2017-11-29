<template>
  <div class="post-match">
      <div class="font16pl3a3c50 pm-mymatch">我匹配的岗位</div>
      <div ></div>
      <div class="pm-font font14pr424242">您目前还没有匹配的岗位，快来这里学习吧</div>
      <div class="pm-font blue"><span class="font14pr23b8ff inmiddle" > 课程库</span></div>
      <div class="pm-font blue"><span class="font14pr23b8ff inmiddle" > 职业路径</span></div>
  </div>
</template>
<script>

export default {
  name: "postMatch",
  data() {
    return {};
  }
};
</script>
<style scoped lang="scss">
.post-match {
//   background: #ffffff;
background: pink;
width:298px;
height:377px;
padding:32px;
box-shadow: 0 2px 5px 5px rgba(0, 0, 0, 0.1);
.pm-font{
    position: relative;
    height:20px;
    padding: 4px 0px;
}
}
</style>


