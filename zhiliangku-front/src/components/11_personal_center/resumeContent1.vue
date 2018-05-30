<template>
  <div id="anchor1" class=" resume-model">
    <resumetitle :tag="{label:'编辑',eventName:'editor'}" @editor="showeditor=!showeditor" :mainData="titleData">
        <span><img   class="imgmiddle imgr" src="./img/简历_小人.svg" alt="">我的优势</span>
    </resumetitle>
    <div  class="resumewidth incenter ">
      <p v-html="mainData.advantage">
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

