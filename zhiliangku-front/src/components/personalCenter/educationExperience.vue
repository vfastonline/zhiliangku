<template>
  <div class="experience-container">
      <div @click="handleClick" class="editor pointer"><img src="../../assets/img/icons/个人中心和积分商城图标/简历_铅笔.svg" alt=""><span>编辑</span></div>
      <div class="marginbottom16"><span>{{mainData.discipline}}</span> | <span>{{mainData.education}}</span></div>
      <p v-if="mainData.experience">{{mainData.experience}}</p>

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


