<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <div class="top_img  hc"></div>
      <SubjectList :project_detail_lists="project_detail_lists"></SubjectList>
      <CardContainer class="card_container mw hc" :config="{num:3,card:SubjectBlock,cardData:true}">
        <SubjectBlock v-for="(item,index) in courses" :key="index" :main_data="item" class="subject_block"></SubjectBlock>
      </CardContainer>
      <pager :url="url" :additionData="params" @pagerGetData="mainPagerdata"></pager>
    </div>
    <F></F>
  </div>
</template>
<style>
  .footer_img{
    display: block;
  }
  .top_img {
    height: 300px;
    background: url("./img/banner.png") center center;
    background-size: cover;
  }
  .card_container{
    min-height: 80vh;
  }
  .subject_block{
    margin-bottom: 40px;
  }
</style>
<script>
  // import Bus from '../../assets/js/02_bus'
  import MyHeader from '../../components/01_header_footer/01_header'
  import F from '../../components/01_header_footer/03_footer'
  import SubjectList from '../../components/05_project_detail/02_subject_info'
  import '../../components/00_common/05_card_container'
  import SubjectBlock from '../../components/05_project_detail/01_subject_block'
  import pager from '../../components/00_common/06_pager'
  export default {
    data() {
      return {
        SubjectBlock:SubjectBlock,
        url: '/tracks/projects/detail/info',
        project_detail_lists: [],
        courses: [],
        pramas:{}
      }
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      SubjectList: SubjectList,
      SubjectBlock:SubjectBlock,
      pager:pager
    },
    methods: {
      mainPagerdata(res) {
        this.$fn.addString(this.$myConst.httpUrl,res.data.data.courses,'avatar')
        this.project_detail_lists = res.data.data
        this.courses = this.project_detail_lists.courses
      }
    },

    created() {
      let custom_user_id = localStorage.getItem('uid');
      let project_id= this.$fn.funcUrl("project_id")||1
      this.params={
        'project_id': project_id,
        'custom_user_id':custom_user_id,
      }
    }
  }
</script>
