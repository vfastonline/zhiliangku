<template>
  <div class="button-container" :style="styleData">
    <el-button v-if="layer.indexOf('delete')!==-1" @click="handleClick('delete')">删除本条</el-button>
    <el-button v-if="layer.indexOf('cancel')!==-1" @click="handleClick('cancel')">取消</el-button>
    <el-button v-if="layer.indexOf('submit')!==-1" @click="handleClick('submit')">完成</el-button>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.button-container{
    text-align:right;
}
</style>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  methods:{
      handleClick(str){
          this.$emit(str)
      }
  },
  props:{
    styleData:Object,
    layer:Array,
  }
}
</script>


