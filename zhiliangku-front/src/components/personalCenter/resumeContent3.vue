<template>
  <div id="anchor3" class="rise resume-model">
     <resumetitle @editor="showeditor=!showeditor">
       <span><img class="imgmiddle imgr" src="../../assets/img/icons/个人中心和积分商城图标/简历_公文包.svg" alt="">工作经历</span>
     </resumetitle>
      <div class="resumewidth incenter">
        <timerbox :config="{title:'company'}" 
        v-if="mainData.length" 
        v-for="(item,index) in mainData" 
        :key="index" 
        :mainData="item" 
        :first="!index"><experience v-if="mainData.length" :mainData="item"></experience></timerbox>
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
import personalexperience from './personalExperience'
import editor from './resumeContent3.0'
export default {
  name: 'HelloWorld',
  data () {
    return {
      showeditor:false
    }
  },
  props:{
    mainData:Array
  },
  components:{
    resumetitle:resumetitle,
    timerbox:timerbox,
    experience:personalexperience,
    editor:editor
  }
}
</script>


