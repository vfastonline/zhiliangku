<template>
  <div id="anchor1" class=" resume-model">
    <resumetitle :tag="{label:'编辑',eventName:'editor'}" @editor="showeditor=!showeditor" :mainData="titleData">
      <tag_0>
        <img class="vs" src="./img/简历_小人.svg" alt="">
        <span class="font1_22_6">我的优势</span>
      </tag_0>
    </resumetitle>
    <div  class="font1_18_9 hc ">
      <p v-html="mainData.advantage">
      </p>
    </div>
    <el-dialog
      :visible.sync="showeditor"
      width="970px">
      <editor :mainData="mainData" @close="showeditor=!showeditor" v-if="showeditor"></editor>
    </el-dialog>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
import resumetitle from './resumePartTitle'
import editor from './07_resume_content_1_modify'
import tag_0 from  './08_tag_0'
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
      editor:editor,
      tag_0:tag_0
    }

  }
</script>
<style scoped>
  .resumewidth {
    min-height: 90px;

  }
  .resumewidth p {
    font: 18px/1.5 "Microsoft YaHei";
    color:#666;
    margin-bottom:60px;
  }
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

