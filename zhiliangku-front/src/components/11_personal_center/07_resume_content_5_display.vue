<template>
  <div id="anchor5"  class="  resume-model">
    <resumetitle @add="add()" :tag="{label:'添加'}">
      <tag_0>
        <img class="vs " src="./img/简历_项目.svg" alt="">
        <span class="font1_22_3">项目经验</span>
      </tag_0>
    </resumetitle>
    <div class="resumewidth hc">
      <p v-if="!mainData.length" class="font1_18_6">你可以描述一下之前工作中所参与的项目，一段精彩的项目经历可以最直观的突出你的优势</p>
    </div>
    <div v-for="(item,index) in mainData" :key="index" class="resumewidth hc">
      <timerbox :config="{title:'name',linkTitle:true}"
                :first="!index" :mainData="item">
        <projectExp @editor="editorInfo(index)" :mainData="item">
        </projectExp>
      </timerbox>
    </div>
    <editor :key="editorKey" :url="editorUrl" :editorIndex="editorIndex" :mainData="mainData" @close="close()"
            v-if="showeditor"></editor>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .resume-model {
    min-height:176px;
    padding-bottom:70px;
  }

</style>
<script>
  import resumetitle from './resumePartTitle'
  import timerbox from './timerbox2'
  import editor from './07_resume_content_5_modify'
  import projectExp from './projectExperience'
  import tag_0 from './08_tag_0'

  export default {
    name: 'HelloWorld',
    data() {
      return {
        showeditor: false,
        editorUrl: '',
        editorIndex: '-1',
        editorKey: '1',
      }
    },
    props: {
      mainData: Array
    },
    methods: {
      close() {
        this.$fn.changeShow(this.getSelf(), 'showeditor');
        this.editorIndex = -1;
      },
      add() {
        this.editorIndex = -1;
        this.editorUrl = "/personal_center/resume/add";
        this.$fn.changeShow(this.getSelf(), 'showeditor');
      },
      editorInfo(index) {
        this.editorUrl = "/personal_center/resume/update";
        if (this.editorIndex == index || this.editorIndex == -1) {
          this.$fn.changeShow(this.getSelf(), 'showeditor');
        }
        this.editorIndex = index;
        this.editorKey = new Date() + '';

      }
    },
    created() {
      console.log(this.mainData)
    },
    components: {
      resumetitle: resumetitle,
      timerbox: timerbox,
      editor: editor,
      projectExp: projectExp,
      tag_0: tag_0
    }
  }

</script>
