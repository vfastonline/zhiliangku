<template>
  <div class="main_antainner">
    <div class="nav_bar mw hc">
        <span class="dib font1_20_6">
          <span class="dib tab_bar ">最新</span>
          <span class="dib tab_bar">已读</span>
          <span class="dib tab_bar">未读</span>
        </span>
      <span class=" font1_20_6 dib tab_bar_right">
          全部标记为已读
        </span>
    </div>
    <message></message>
  </div>
</template>

<script>
  import message from './02_message_unit'

  export default {
    name: "01_message_center",
    components: {
      message: message
    }
  }
</script>

<style scoped>
  .nav_bar {
    display: flex;
    justify-content: space-between;
    padding:50px 0 30px;
  }
  .tab_bar {
    padding: 5px 30px;
    margin-right:20px;
  }
  .tab_bar_right {
    padding: 5px 40px 5px 0;
  }
  .main_antainner {
    background-color:#fafafa;
  }
</style>
