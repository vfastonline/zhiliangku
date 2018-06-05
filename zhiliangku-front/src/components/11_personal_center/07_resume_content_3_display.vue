<template>
  <div id="anchor3" class=" resume-model">
    <resumetitle @add="add()">
      <tag_0>
        <img class="vs " src="./img/01_briefcase.svg" alt="">
        <span class="font1_22_6">工作经历</span>
      </tag_0>
    </resumetitle>
    <div class="resumewidth hc">
      <timerbox @editor="editorInfo(index)" :config="{title:'company'}" v-if="mainData.length" v-for="(item,index) in mainData" :key="index" :mainData="item"
        :first="!index">
        <experience v-if="mainData.length" :mainData="item"></experience>
      </timerbox>
    </div>
    <editor :key="editorKey" :url="editorUrl" :editorIndex="editorIndex"  :mainData="mainData" @close="close()" v-if="showeditor"></editor>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .resume-model {
    /*min-height:170px;*/
    /*padding-bottom:70px;*/
  }

</style>
<script>
  import resumetitle from './resumePartTitle'
  import timerbox from './timerbox'
  import personalexperience from './personalExperience'
  import editor from './07_resume_content_3_modigy'
  import tag_0 from './08_tag_0'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        showeditor: false,
        editorUrl: '',
        editorIndex: '-1',
        editorKey:'1',
      }
    },
    props: {
      mainData: Array
    },
    methods: {
      close(){
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
        if (this.editorIndex == index||this.editorIndex == -1) {
          this.$fn.changeShow(this.getSelf(), 'showeditor');
        }
        this.editorIndex = index;
        this.editorKey=new Date()+''
        console.log(index)
      }
    },
    components: {
      resumetitle: resumetitle,
      timerbox: timerbox,
      experience: personalexperience,
      editor: editor,
      tag_0:tag_0
    }
  }

</script>
