<template>
  <div id="anchor2" class="rise resume-model">
    <resumetitle @editor="showeditor=!showeditor" :mainData="titleData">
        <span><img class="imgmiddle imgr" src="../../assets/img/icons/个人中心和积分商城图标/简历_钱币.svg" alt="">求职意向</span>
    </resumetitle>
    <div v-for="(item,index) in mainData" :key="index" class="resumewidth incenter rc2-container2 ">
      <span class="floatl rc2-c2-tag">{{item.position}}</span>
      <span class="floatl rc2-c2-tag">期望城市：{{item.city}}</span>
      <span class="floatl rc2-c2-tag">期望行业：{{item.industry}}</span>
      <span class="floatl rc2-c2-tag">{{item.expect_salary_high}}-{{item.expect_salary_low}}</span>
      <span>
        <img @click="showeditor=!showeditor" class="imgmiddle imgr" src="../../assets/img/icons/个人中心和积分商城图标/简历_铅笔.svg" alt="">编辑</span>
    </div>
    <editor :mainData="mainData" @close="showeditor=!showeditor"  v-if="showeditor"></editor>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .rc2-container1 {
    border-bottom: 2px solid #eef0f2;
  }
  .rc2-container2 {
    display: flex;
    justify-content: space-between;
    margin-top: 15px;
    padding-right:15px;
  }
  .rc2-container2{
    margin-bottom: 12px;
  }
</style>
<script>
  import resumetitle from './resumePartTitle'
  import editor from './resumeContent2.0.vue'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        titleData:{label:'求职意向'},
        showeditor:false
      }
    },
    props:{
      mainData:Array
    },
    components: {
      resumetitle: resumetitle,
      editor:editor
    }
  }

</script>
