<template>
  <div>
    <div class="main">
      <MyHeader></MyHeader>
      <div class="top_img"></div>
      <!--<div v-html="str"></div>-->
      <section class="project_list">
        <CardContainer class="mw hc " :config="{num:3,card:ProjectStep,cardData:true}">
          <a href="/projectSubjectList/index.html" v-for="(item, index) in project_lists" :key="index">
            <ProjectStep :main_data="item" class="margin"></ProjectStep>
          </a>
        </CardContainer>
      </section>
      <Pager></Pager>
      <img class="bottom_image db" src="./img/tree_wave.png" alt="">
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>
  .margin {
    margin-bottom: 40px;
  }

  .top_img {
    height: 300px;
    background: url("./img/tree_wave.png") center center;
    background-size: cover;
  }

  .project_list {
    margin: 120px 0px;
  }

  .bottom_image {
    height: 440px;
    width: 100%;
  }
</style>

<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import F from '../../components/01_header_footer/03_footer'
  import ProjectStep from '../../components/04_project_list/01_project_step'
  import '../../components/00_common/05_card_container'
  import Pager from '../../components/00_common/06_pager'

  export default {
    data() {
      return {
        ProjectStep: ProjectStep,
        project_lists:''
      }
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      ProjectStep: ProjectStep,
      Pager: Pager
    },
    created(){
      this.$get('/tracks/projects/list/info?home_show=0').then(res=>{
        console.table(res.data.data)
        this.project_lists = res.data.data;
      })
    }
  }
</script>
