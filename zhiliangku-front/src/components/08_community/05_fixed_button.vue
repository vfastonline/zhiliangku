<template>
    <div class="fixed_button ftc cp">
      <span class="dib vm icon">
        <slot></slot>      
      </span>
      <p class="font1_20_f dib  fixed_button_text">{{text}}</p>
    </div>
</template>
<style scoped lang="scss">
  .fixed_button {
    width:60px;
    height:120px;
    background:#8c97cb;
  }
  .icon {
    height:50px;
    padding-top:10px;
  }
  .fixed_button_text {
    line-height:26px;
    padding:0 10px;
  }
</style>
<script>
  export default {
    data() {
      return {    
      }
    },
    props: {
      text: ''
    }
  }
</script>