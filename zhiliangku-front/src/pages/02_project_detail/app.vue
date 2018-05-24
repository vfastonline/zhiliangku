<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <div class="top_img  hc"></div>
      <Crumb class="crumb mw hc font1_20_6" :main_data="breadcrumbs" ></Crumb>
      <SubjectList :project_detail_lists="project_detail_lists"></SubjectList>
      <CardContainer class="card_container mw hc" :config="{num:3,card:SubjectBlock,cardData:true}">
        <SubjectBlock v-for="(item,index) in courses" :key="index" :main_data="item" class="subject_block"></SubjectBlock>
      </CardContainer>
      <pager :url="url" :additionData="params" @pagerGetData="mainPagerdata"></pager>
      <FooterImage :src="$myConst.httpUrl+'/media/image/static/project_list_02_bottom.png'"></FooterImage>
    </div>
    <F></F>
  </div>
</template>
<style stoped >
  .crumb{
    margin-top: 50px;
    line-height: 60px;
    height: 60px;
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
  import Crumb from '../../components/00_common/10_crumb'
  import SubjectList from '../../components/05_project_detail/02_subject_info'
  import '../../components/00_common/05_card_container'
  import SubjectBlock from '../../components/05_project_detail/01_subject_block'
  import pager from '../../components/00_common/06_pager'
  import FooterImage from '../../components/00_common/08_image_block'
  export default {
    data() {
      return {
        SubjectBlock:SubjectBlock,
        url: '/tracks/projects/detail/info',
        project_detail_lists: [],
        courses: [],
        pramas:{},
        breadcrumbs: '',
      }
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      Crumb:Crumb,
      SubjectList: SubjectList,
      SubjectBlock:SubjectBlock,
      pager:pager,
      FooterImage: FooterImage
    },
    methods: {
      mainPagerdata(res) {
        this.$fn.addString(this.$myConst.httpUrl,res.data.data.courses,'avatar')
        this.breadcrumbs = res.data.breadcrumbs
        this.project_detail_lists = res.data.data
        // console.log(this.project_detail_lists);
        this.courses = this.project_detail_lists.courses
      }
    },

    created() {
      let project_id= this.$fn.funcUrl("project_id")||1
      this.params={
        'project_id': project_id,
      }
    }
  }
</script>
