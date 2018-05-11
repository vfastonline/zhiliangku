<template>
<!-- 这个就是容器，不过实现容器适配的规则在卡片身上 -->
<!-- 按道理讲 容器适配的话 规则应该在容器身上啊 感觉很不合理-->
<!-- -所以利用flex布局,更容易实现grid布局-->
  <div class="incenter" :class="className" :style="myStyle">
    <slot></slot>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      className:[]
    }
  },
  props:{
      myStyle:Object,
  },
  created(){
      this.$fn.initStyle(this.$vueself(), 'myStyle', ['className'])
  }
}
</script>


