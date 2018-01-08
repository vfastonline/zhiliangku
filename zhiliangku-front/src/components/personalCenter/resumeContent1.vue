<template>
  <div id="anchor1" class="rise resume-model">
    <resumetitle @editor="showeditor=!showeditor" :mainData="titleData">
        <span><img   class="imgmiddle imgr" src="../../assets/img/icons/个人中心和积分商城图标/简历_钱币.svg" alt="">优势描述</span>
    </resumetitle>
    <div  class="resumewidth incenter ">
      <p>
        {{mainData.advantage}}
      </p>
    </div>
    <editor :mainData="mainData" @close="showeditor=!showeditor" v-if="showeditor"></editor>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
import resumetitle from './resumePartTitle'
import editor from './resumeContent1.0'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        titleData:{label:'我的优势'},
        showeditor:false,
      }
    },
    props:{
      mainData:Object
    },
    components:{
      resumetitle:resumetitle,
      editor:editor
    }
    
  }
</script>
<style scoped>
  .rc-ma-container1 {
    padding-bottom: 15px;
    border-bottom: 2px solid #eef0f2;
  }

  .rc-mac-editor {
    position: absolute;
    right: 15px;
    bottom: 10px;
  }

</style>

