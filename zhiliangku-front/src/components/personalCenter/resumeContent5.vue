<template>
  <div id="anchor5" class="rise resume-model">
    <resumetitle @add="add()">
      <span>
        <img class="imgmiddle imgr" src="../../assets/img/icons/个人中心和积分商城图标/简历_项目.svg" alt="">项目经验</span>
    </resumetitle>
    <div class="resumewidth incenter">
      <p v-if="!mainData.length">你可以描述一下之前工作中所参与的项目，一段精彩的项目经历可以最直观的突出你的优势</p>
    </div>
    <div v-for="(item,index) in mainData" :key="index" class="resumewidth incenter">
      <timerbox :config="{title:'name',linkTitle:true}" 
      :first="!index" :mainData="item">
      <projectExp @editor="editorInfo(index)" :mainData="item">
        </projectExp></timerbox>
    </div>
    <editor :key="editorKey" :url="editorUrl" :editorIndex="editorIndex"  :mainData="mainData" @close="close()" v-if="showeditor"></editor>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


</style>
<script>
  import resumetitle from './resumePartTitle'
  import timerbox from './timerbox'
  import editor from './resumeContent5.0'
  import projectExp from './projectExperience'
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
    created(){
      console.log(this.mainData)
    },
    components: {
      resumetitle: resumetitle,
      timerbox: timerbox,
      editor: editor,
      projectExp:projectExp
    }
  }

</script>
