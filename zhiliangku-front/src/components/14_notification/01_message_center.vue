<template>
  <div>
    <div class="nav_bar mw hc">
        <span class="dib">
          <span class="dib">最新</span>
          <span class="dib">已读</span>
          <span class="dib">未读</span>
        </span>
      <span class="dib">
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
  }
</style>
