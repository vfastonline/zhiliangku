<template>
  <div>
    <div class="main">
      <MyHeader></MyHeader>
      <div class="top_img mw hc"></div>
      <!--<div v-html="str"></div>-->
      <section class="project_list">
        <CardContainer v-if="project_lists.length" class="mw hc " :config="{num:3,card:ProjectStep,cardData:project_lists[0]}">
            <ProjectStep  v-for="(item, index) in project_lists" v-if="item" :key="index" :main_data="item" class="margin"></ProjectStep>
        </CardContainer>
      </section>
      <Pager class="mw hc"></Pager>
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
<<<<<<< HEAD
        project_lists:[]
=======
<<<<<<< HEAD
        str: ''
=======
        project_lists:''
>>>>>>> 2028d52fa6d348aec59f7aa249c3f8a5aee73cfb
>>>>>>> 44e428effa84f9af9260cb509cf07a058b06f713
      }
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      ProjectStep: ProjectStep,
      Pager: Pager
    },
<<<<<<< HEAD
    created() {
      this.$get('/tracks/projects/list/info?project_id=1').then(res => {
        this.str = res.data.breadcrumbs
=======
    created(){
      this.$get('/tracks/projects/list/info?home_show=0').then(res=>{
        console.table(res.data.data)
        this.project_lists = res.data.data;
>>>>>>> 2028d52fa6d348aec59f7aa249c3f8a5aee73cfb
      })
    }
  }
</script>
