<template>
  <div id="anchor4" class="rise resume-model">
    <resumetitle @editor="showeditor=!showeditor">
      <span>
        <img class="imgmiddle imgr" src="../../assets/img/icons/个人中心和积分商城图标/简历_学士帽.svg" alt="">教育经历</span>
    </resumetitle>
    <div v-for="(item,index) in mainData" :key="index" class="resumewidth incenter">
      <timerbox :config="{title:'school'}" :first="!index" :mainData="item">
        <educationExp :mainData="item"></educationExp></timerbox>
    </div>
    <editor :mainData="mainData" @close="showeditor=!showeditor" v-if="showeditor"></editor>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


</style>
<script>
  import resumetitle from './resumePartTitle'
  import timerbox from './timerbox'
  import editor from './resumeContent4.0'
  import educationExp from './educationExperience'
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
    components: {
      resumetitle: resumetitle,
      timerbox: timerbox,
      editor: editor,
      educationExp:educationExp
    },
    created(){
      console.log(this.mainData)
    }
  }

</script>
