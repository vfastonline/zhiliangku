<template>
  <div class="border_style_block r">
    <div class="float_tag a">
      <span class="font1_20_3 dib vm">今天</span>
      <span class="tag_dot dib vm"></span>
    </div>
    <slot></slot>
  </div>
</template>

<script>
    export default {
        name: "progress_block_container"
    }
</script>

<style scoped>
  .border_style_block{
    border-left: 2px solid #999;
    padding-left:76px ;
    height: 250px;
  }
  .float_tag{
    right: 100%;
    transform: translate(9px,-24%);
    z-index: 1;
    white-space: nowrap;
  }
  .tag_dot{
    width: 14px;
    height: 14px;
    border-radius: 50%;
    z-index: 10;
    border: 2px solid #999;
    background-color: white;
  }
</style>
