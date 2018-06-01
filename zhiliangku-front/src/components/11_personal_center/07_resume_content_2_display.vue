<template>
  <div id="anchor2" class=" resume-model">
    <resumetitle @add="add()" :mainData="titleData">
      <span>
        <img class="imgmiddle imgr" src="./img/简历_钱币.svg" alt="">求职意向</span>
    </resumetitle>
    <div v-for="(item,index) in mainData" :key="index" class="resumewidth hc rc2-container2 ">
      <span class="fl rc2-c2-tag">{{item.position?item.position:'暂无'}}</span>
      <span class="fl rc2-c2-tag">期望城市：{{item.city}}</span>
      <span class="fl rc2-c2-tag">期望行业：{{item.industry}}</span>
      <span class="fl rc2-c2-tag">{{item.expect_salary}}</span>
      <span class="pointer" @click="editorInfo(index)">
        <img class="imgmiddle imgr" src="./img/简历_铅笔.svg" alt="">
        <span>编辑</span>
      </span>
    </div>
    <editor :key="editorKey" :url="editorUrl" :editorIndex="editorIndex" :mainData="mainData" @close="close()" v-if="showeditor"></editor>
  </div>
</template>
<script>
  import resumetitle from './resumePartTitle'
  import editor from './07_resume_content_2_modify.vue'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        titleData: {
          label: '求职意向'
        },
        showeditor: false,
        editorUrl: '',
        editorIndex: '-1',
        editorKey:'a'
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
      }
    },
    components: {
      resumetitle: resumetitle,
      editor: editor
    }
  }

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .rc2-container1 {
    border-bottom: 2px solid #eef0f2;
  }

  .rc2-container2 {
    display: flex;
    justify-content: space-between;
    margin-top: 15px;
    padding-right: 15px;
  }

  .rc2-container2 {
    margin-bottom: 12px;
  }

</style>
