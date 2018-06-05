<template>
  <div id="anchor2" class=" resume-model">
    <resumetitle @add="add()" :mainData="titleData">
      <tag_0>
        <img class="vs " src="./img/简历_钱币.svg" alt="">
        <span class="font1_22_6 weight">求职意向</span>
      </tag_0>
      <span>
        </span>
    </resumetitle>
    <div v-for="(item,index) in mainData" :key="index" class=" hc rc2-container2 ">
      <span class="font1_20_9 ">期望职位：{{item.position||'尚未填写'}}</span>
      <span class="font1_20_9 ">期望城市：{{item.city||'尚未填写'}}</span>
      <span class="font1_20_9 ">期望行业：{{item.industry||'尚未填写'}}</span>
      <span class="font1_20_6 ">期望薪资：{{item.expect_salary||'尚未填写'}}</span>
      <tag_0 class="cp" @click="editorInfo(index)">
        <img class="vs " src="./img/编辑icon.png" alt="">
        <span class="font1_22_9">编辑</span>
      </tag_0>
    </div>
    <editor :key="editorKey" :url="editorUrl" :editorIndex="editorIndex" :mainData="mainData" @close="close()"
            v-if="showeditor"></editor>
  </div>
</template>
<script>
  import resumetitle from './resumePartTitle'
  import editor from './07_resume_content_2_modify.vue'
  import tag_0 from './08_tag_0'

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
        editorKey: 'a'
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
      editor: editor,
      tag_0: tag_0
    }
  }

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .rc2-container1 {
    border-bottom: 2px solid #eef0f2;
  }

  .resume-model {
    min-height: 60px;
    padding-bottom:70px;
  }

  .rc2-container2 {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    margin-top: 15px;
    padding-right: 15px;
  }

  .rc2-container2 {
    margin-bottom: 12px;
  }

  .edit img {
    margin-right:5px;
    vertical-align: top;
  }

</style>
