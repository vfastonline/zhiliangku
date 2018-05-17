<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <SubjectList></SubjectList>
      <CardContainer class="card_container mw hc" :config="{num:3,card:SubjectBlock,cardData:true}">
        <SubjectBlock v-for="item in arr" :key="item" class="subject_block"></SubjectBlock>
      </CardContainer>
      <pager></pager>
    </div>
    <F></F>
  </div>
</template>
<style>
  .card_container{
    min-height: 80vh;
  }
  .subject_block{
    margin-bottom: 40px;
  }
</style>
<script>
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
        arr:[1,2,3,4]
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
      get_project_detail_lists() {
        this.$get("/tracks/projects/detail/info?project_id=1").then(res => {
          console.log(res.data)
        })
      }
    },
    created() {
      this.get_project_detail_lists()
    }
  }
</script>
