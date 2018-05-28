<template>
  <div class="message_box mw hc">
    <div class="message_top ftc font1_28_f">
      <p>错误提示</p>
    </div>
    <div class="message_content font1_22_9">{{main_message.msg||"暂无消息"}}</div>
  </div>
</template>

<style>
  .message_box {
    height: 330px;
    margin-top: 40px;
    box-shadow: 0 0 18px rgba(0, 0, 0, 0.15);
  }
  
  .message_top {
    margin-top: 40px;
    height: 60px;
    line-height: 60px;
    background-color: #324e5c;
    border-radius: 10px;
  }
  
  .message_content {
    line-height: 30px;
    padding: 20px 60px 0 60px;
  }
  
  .message_content:p {
    margin-bottom: 30px;
  }
  
  .message_content:last-child {
    margin-bottom: 0;
  }
</style>

<script>
  export default {
    data() {
      return {}
    },
    props: {
      main_message: {}
    }
  }
</script>
