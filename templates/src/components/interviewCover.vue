<template>
  <div class="ic-container ofhid floatl">
      <ul class="icc-content">
          <li class="iccc-title fontcenter textellipsis font20pr5a646e">Python开发工程师</li>
          <li class="iccc-img"><img class="iccc-img" src="../assets/img/interviewCover.png" alt=""></li>
          <li class="iccc-info fontjustify">
              <div class="iccci-tag clearfix">
                  <span class="icccit-1 floatl font14prb2bbbf">月薪</span>
                  <span class="icccit-2 floatr font14pr002800">10k-12k</span>
              </div>
              <div class="iccci-tag clearfix">
                  <span class="icccit-1 floatl font14prb2bbbf">试题数量</span>
                  <span class="icccit-2 floatr font14pr002800">4</span>
              </div>
          </li>
          <li class="iccc-name fontcenter textellipsis font20pr5a646e">深圳市正义隆农业悠闲公司</li>
      </ul>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.ic-container {
  width: 362px;
  height: 445px;
}
.iccc-title,
.iccc-name {
  letter-spacing: 2.86px;
}
.iccc-title {
  padding: 17px 0px;
}
.iccc-img {
  width: 362px;
  height: 272px;
}
.iccc-info{
    padding:0px 32px;
    width:298px;
    height:20px;
    line-height:20px;
    margin-top:27px;
    margin-bottom:16px;
    display: flex;
    justify-content: space-between;
}
.iccci-tag{
    display: inline;
}
.iccci-tag{
    width:133px;
}
.iccc-name{
    margin-bottom:28px;
}
</style>
<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      msg: "Welcome to Your Vue.js App"
    };
  }
};
</script>


