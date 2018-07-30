<template>
  <div class="block_title font1_34_f r" >
    {{block_title}}
    <div class="a icon_container">
      <img @click="close" class="close_icon cp vm" src="./img/01_close_icon.png" alt="">
    </div>
  </div>
</template>

<script>
  export default {
    name: "block_title",
    props: {
      block_title: {
        type: String,
        required: true
      }
    },
    methods:{
      close(){
        this.$emit('close',this)
      }
    }
  }
</script>

<style scoped>
  .icon_container{
    right: 0;
    top:0;
    height: 82px;
  }
  .block_title {
    height: 82px;
    line-height: 82px;
    background: #515c6e;
  }
  .close_icon{
    margin-right: 20px;
  }
</style>
