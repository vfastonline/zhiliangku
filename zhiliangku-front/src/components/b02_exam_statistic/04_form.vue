<template>
  <div class="content_container rose">
    <div class="tr form_title font1_22_3">
      <div class="column_0 ftc">考试名称</div>
      <div class="column_1 ftc">考试性质</div>
      <div class="column_2 ftc">考试方式</div>
      <div class="column_3 ftc">考试时间</div>
      <div class="column_4 ftc">参加人数</div>
      <div class="column_5 ftc">操作</div>
    </div>
    <div v-for="item in [1,2,3,4]" :key="item" class=" tr form_li font1_18_6">
      <div class="column_0">考试名称askldnfalskdjfiajsp 噢诶发我IE飞牛网微微佛窝囊废你看</div>
      <div class="column_1 ftc">考试性质</div>
      <div class="column_2 ftc">考试方式</div>
      <div class="column_3 ftc">考试时间</div>
      <div class="column_4 ftc">参加人数</div>
      <div class="column_5 ftc operation_container">
        <span class="operation cp dib">编辑</span>
        <span class="operation cp dib">详情</span>
        <span class="operation cp dib">录入成绩</span>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "04_form"
  }
</script>

<style lang="scss" scoped>
  @import "../../assets/style/baseConstScss";

  @mixin flex() {
    display: flex;
    justify-content: space-between;
  }

  @mixin box_type {
    width: 1080px;
    box-sizing: border-box;
  }

  .content_container {
    @include box_type
  }

  .tr {
    @include flex();
    padding: 0 20px 0 40px;

  }

  .form_title {
    height: 60px;
    line-height: 60px;
    font-weight: 700;
    background-color: $cy;
    border-radius: 10px 10px 0 0;
    margin-bottom: 15px;
  }
  @for $i from 0 through 5{
    .column_#{$i}{
      display: flex;
      justify-content: center;
      align-items: center;
    }
  }
  .column_0 {
    width: 285px;
  }

  .column_1 {
    width: 90px;
  }

  .column_2 {
    width: 90px;
  }

  .column_3 {
    width: 170px;
  }

  .column_4 {
    width: 90px;
  }

  .column_5 {
    width: 174px;
  }

  .form_li {
    @include box_type;
    margin-bottom: 24px;
    @include flex();

  }

  .operation_container {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .operation:hover {
    color: $cb4;
  }
</style>
