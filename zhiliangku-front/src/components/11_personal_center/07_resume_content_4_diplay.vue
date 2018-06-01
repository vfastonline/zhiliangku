<template>
  <div id="anchor4" class=" resume-model">
    <resumetitle @add="add()">
      <tag_0>
        <img class="vs imgr" src="./img/简历_学士帽.svg" alt="">
        <span class="font1_22_6">教育经历</span>
      </tag_0>
    </resumetitle>
    <div v-for="(item,index) in mainData" :key="index" class="resumewidth hc">
      <timerbox @editor="editorInfo(index)" :config="{title:'school'}" :first="!index" :mainData="item">
        <educationExp :mainData="item"></educationExp>
      </timerbox>
    </div>
    <editor :key="editorKey" :url="editorUrl" :editorIndex="editorIndex" :mainData="mainData" @close="close()"
            v-if="showeditor"></editor>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


</style>
<script>
  import resumetitle from './resumePartTitle'
  import timerbox from './timerbox2'
  import editor from './07_resume_content_4_modify'
  import educationExp from './educationExperience'
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
        this.editorKey = new Date() + ''
      }
    },
    components: {
      resumetitle: resumetitle,
      timerbox: timerbox,
      editor: editor,
      educationExp: educationExp,
      tag_0: tag_0
    },
    created() {
      console.log(this.mainData)
    }
  }

</script>
