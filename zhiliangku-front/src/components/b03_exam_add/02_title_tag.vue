<template>
  <div class="titleTag__tag">
    <slot name="icon"></slot>
    <span class="dib vm font1_26_3" slot="title">{{text}}</span>
  </div>
</template>

<script>
  export default {
    name: "title_tag",
    props: {
      text: ''
    },
    created() {
    }
  }
</script>
<style lang="scss" scoped>
  @import "../../assets/style/baseConstScss";

  .titleTag__tag {
    height: 52px;
    width: 230px;
    background-color: $cy;
    padding: 0 39px 0 51px;
    border-radius: 10px 10px 0 0;
    box-sizing: border-box;
    white-space: nowrap;
    display: flex;
    justify-content: space-between;
    align-items: center;
   img{
     margin-right: 10px;
   }

  }

  .titleTag__tag--icon {
    margin-right: 10px;
  }
</style>
