<template>
  <div>
    <div class="main">
      <MyHeader></MyHeader>
      <div class="top_img mw hc"></div>
      <!--<div v-html="str"></div>-->
      <SearchInput></SearchInput>
      <section class="project_list">
        <CardContainer v-if="project_lists.length" class="mw hc " :config="{num:3,card:ProjectStep,cardData:project_lists[0]}">
            <ProjectStep  v-for="(item, index) in project_lists" v-if="item" :key="index" :main_data="item" class="margin"></ProjectStep>
        </CardContainer>
      </section>
      <Pager class="mw hc" @pagerGetData="mainPagerData" :url="url" :addition-data="params"></Pager>
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
  import SearchInput from '../../components/04_project_list/02_search_input'

  export default {
    data() {
      return {
        ProjectStep: ProjectStep,
        url:'/tracks/projects/list/info',
        project_lists: [],
        params: {}
      }
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      ProjectStep: ProjectStep,
      Pager: Pager,
      SearchInput: SearchInput
    },
    methods: {
      //获取pager分页组件返回的分页数据
      mainPagerData(res) {
        this.project_lists = res.data.data
        // console.log( res.data.data )
      }
    },
    created(){
      let custom_user_id = localStorage.getItem('uid')
      this.params={
        'custom_user_id':custom_user_id,
      }
    }
  }
</script>
