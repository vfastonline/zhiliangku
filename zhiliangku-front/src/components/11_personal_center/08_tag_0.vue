<template>
    <span class="dib tag_0">
      <slot></slot>
    </span>
</template>

<script>
  export default {
    name: "button_0",
  }
</script>

<style lang="scss">
  /*默认icon右侧10px间距 组件加“tag_edit”类名后右侧变为20px间距*/
  .tag_0 {
    img:nth-child(1) {
      margin-right: 15px;
    }
  }
  .tag_edit {
    img:nth-child(1) {
      margin-right: 5px;
    }
  }
</style>
