<template>
  <div id="anchor0" class="rise">
    <div  class="rc-pi resumewidth incenter">
      <div class="rc-pi-container1">
        <div class="rc-pi-content ">
          <img class="rc-pic-img floatl round" src="../../assets/img/user-icon.jpg" alt="">
          <div class="rc-pic-word">
            <div @click="showeditor=!showeditor" class="pointer rc-pic-editor">
              <img  class="imgmiddle imgr" src="../../assets/img/icons/个人中心和积分商城图标/简历_铅笔.svg" alt="">编辑</div>
            <div class="rc-pic-word-0">
              <span class="font20pl3a3c50">{{mainData.name}}</span>
              <img class="resume-sex-icon" v-if="mainData.sex=='女'" src="../../assets/img/icons/个人中心和积分商城图标/简历_性别女.svg" alt="">
              <img class="resume-sex-icon" v-if="mainData.sex=='男'" src="../../assets/img/icons/个人中心和积分商城图标/简历_性别男.svg" alt="">
              <span>{{mainData.age}}岁</span>
            </div>
            <div class="rc-pic-word-1">
              <span class="font14pl3a3c50">{{mainData.status}}</span>
              <span class="font14pl3a3c50">{{mainData.position}}</span>
              <span class="font14pl3a3c50">{{mainData.company}}</span>
            </div>
          </div>
        </div>
      </div>
      <div class="rc-pi-container2">
        <span>
          <img class="imgmiddle imgr" src="../../assets/img/icons/个人中心和积分商城图标/简历_公文包.svg" alt="">{{mainData.years_of_service}}年</span>
        <span>
          <img class="imgmiddle imgr" src="../../assets/img/icons/个人中心和积分商城图标/简历_学士帽.svg" alt="">{{mainData.education}}</span>
        <span>
          <img class="imgmiddle imgr" src="../../assets/img/icons/个人中心和积分商城图标/简历_小人.svg" alt="">{{mainData.status}}</span>
        <span>
          <img class="imgmiddle imgr" src="../../assets/img/icons/个人中心和积分商城图标/简历_钱币.svg" alt="">{{mainData.expect_salary_low}}-{{mainData.expect_salary_high}}</span>
      </div>
    </div>
    <editor :mainData="mainData"  @close="showeditor=!showeditor" v-if="showeditor"></editor>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
import editor from './resumeContent0.0'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        showeditor:false,
      }
    },
    components:{
      editor:editor
    },
    props:{
      mainData:Object
    },
    created(){
      console.log(this.mainData)
    }
  }

</script>
<style scoped>
  .rc-pi {
    padding-bottom: 24px;
    margin-bottom: 48px;
  }

  .rc-pi-container1 {
    height: 100px;
    padding: 15px 0;
    border-bottom: 2px solid #eef0f2;
  }
  .rc-pi-content{
    height:70px;
  }
    .resume-sex-icon{
    margin:0 38px;
  }
  .rc-pi-container2 {
    padding-top: 18px;
    padding-right:15px;
    display: flex;
    justify-content: space-between;
  }

  .rc-pi-content {
    position: relative;
  }

  .rc-pic-img {
    height: 100px;
    width: 100px;
  }

  .rc-pic-word {
    margin-left: 150px;
    padding-top:21px;
  }
  .rc-pic-word-0{
    margin-bottom: 12px;
  } 
 .rc-pic-word-1{

  }
  .rc-pic-editor {
    position: absolute;
    right: 0;
    top: 0;
  }

</style>

