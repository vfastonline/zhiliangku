<template>
    <span @click="$emit('click')" class="dib tag_0">
      <slot></slot>
    </span>
</template>

<script>
  export default {
    name: "button_0",
  }
</script>

<style lang="scss">
  .tag_0 {
    img:nth-child(1) {
      margin-right: 5px;
    }
  }
</style>
