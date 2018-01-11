<template>
  <div id="anchor5" class="rise resume-model">
    <resumetitle @editor="showeditor=!showeditor">
      <span>
        <img class="imgmiddle imgr" src="../../assets/img/icons/个人中心和积分商城图标/简历_项目.svg" alt="">项目经验</span>
    </resumetitle>
    <div class="resumewidth incenter">
      <p>你可以描述一下之前工作中所参与的项目，一段精彩的项目经历可以最直观的突出你的优势</p>
    </div>
    <div v-for="(item,index) in mainData" :key="index" class="resumewidth incenter">
      <timerbox :config="{title:'name',linkTitle:true}" :first="!index" :mainData="item"><projectExp :mainData="item"></projectExp></timerbox>
    </div>
    <!-- <editor :mainData="mainData" @close="showeditor=!showeditor" v-if="showeditor"></editor> -->
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
        showeditor: false
      }
    },
    props: {
      mainData: Array
    },
    methods: {
      close() {
        this.$emit('close')
      },
      deleteInfo() {

      },
      submit() {
        if (!this.mainData.length) {
          this.url = '/personal_center/resume/add'
        }
        this.$post(this.url, {
          custom_user_id: localStorage.uid,
          resume_type: 'resume',
          resume_info_dict: {}
        }).then(res => {
          console.log(res)
          Bus.$emit('refreshResume')
        })
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
