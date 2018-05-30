<template>
  <div class="experience-container">
      <div @click="handleClick" class="editor pointer"><img src="./img/简历_铅笔.svg" alt=""><span>编辑</span></div>
      <div class="marginbottom16">{{mainData.position}}</div>
      <div v-html="mainData.content"></div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.experience-container{
    position: relative;
}
.editor{
    position: absolute;
    top:0;
    right:0;
}
.editor img{
    margin-right:15px;
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
  props:{
    mainData:Object
  },
  methods:{
    handleClick(){
      this.$emit('editor')
    }
  },
  created(){
    console.log(this.mainData)
  }
}
</script>


