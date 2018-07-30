<template>
  <div class="layout_container mw hc">
    <left></left>
    <right></right>
  </div>
</template>

<script>
  import left from './03_left'
  import right from './04_form'
  export default {
    name: "content_layout",
    components:{
      left:left,
      right:right
    }
  }
</script>

<style scoped>
.layout_container{
  margin-top: 30px;
  margin-bottom: 20px;
  display: flex;
  justify-content: space-between;
}
</style>
