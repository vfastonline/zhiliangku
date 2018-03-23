<template>
  <div class="button-container" :style="styleData">
    <el-button class="button_style_1" v-if="layer.indexOf('delete')!==-1" @click="handleClick('delete')">删除本条</el-button>
    <el-button class="button_style_1" v-if="layer.indexOf('cancel')!==-1" @click="handleClick('cancel')">取消</el-button>
    <el-button class="button_style_1" v-if="layer.indexOf('submit')!==-1" @click="handleClick('submit')">完成</el-button>
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
      str0:'删除本条',
      str1:'取消',
      str2:'完成'
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
    config:Object
  }
}
</script>


