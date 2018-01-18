<template>
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


