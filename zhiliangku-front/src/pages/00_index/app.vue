<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <Carousal></Carousal>
      <IntroduceTitle :title="'智量酷是什么？'"></IntroduceTitle>
      <div class="introduce_block mw hc">
        <IntroduceStep v-for="(item,index) in introduce_list" :key="index" class="step"
                       :stepData="item"></IntroduceStep>
      </div>
      <IntroduceTitle :title="'企业人才招聘方案'"></IntroduceTitle>
      <p class="hc font1_22_6 mw ftc" v-if="enterprise_need[0]" v-html="enterprise_need[0].title"></p>
      <EnterpriseRecruitment :main_data="enterprise_need"></EnterpriseRecruitment>
      <IntroduceTitle :title="'项目说明书'"></IntroduceTitle>
      <ProjectFace v-for="(item,index) in project_home_lists" :key="index" :main_data="item"></ProjectFace>
      <!--<ProjectFace></ProjectFace>-->
      <!--<JoinUs></JoinUs>-->
      <Joined></Joined>
    </div>
    <F></F>
  </div>
</template>

<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import Carousal from '../../components/03_index/01_carouse'
  import IntroduceStep from '../../components/03_index/02_introduce_step'
  import IntroduceTitle from '../../components/03_index/03_introduce_title'
  import EnterpriseRecruitment from '../../components/03_index/07_enterprise_recruitment'
  import ProjectFace from '../../components/03_index/04_project_block'
  import JoinUs from '../../components/03_index/05_join_us'
  import Joined from '../../components/03_index/06_joined'
  import F from '../../components/01_header_footer/03_footer'

  export default {
    data() {
      return {
        introduce_list: [],
        enterprise_need: [],
        project_home_lists:[],

      }
    },
    methods: {
      get_introduce_list() {
        this.$get('/slides/websiteintroduce/list').then(res => {
          this.introduce_list = res.data.data;
        })
      },
      get_enterprise_need() {
        this.$get('/slides/recruitmentplan/list').then(res=>{
            this.enterprise_need = res.data.data
          this.$fn.addString(this.$myConst.httpUrl,res.data.data,'pathwel')
        })
      },
      get_project_list() {
        this.$get('/tracks/projects/list/info?home_show=1').then(res=>{
          this.$fn.addString(this.$myConst.httpUrl,res.data.data,'pathwel')
          this.project_home_lists = res.data.data;
        })
      }
    },
    created() {
      this.get_introduce_list()
      this.get_enterprise_need()
      this.get_project_list()
    },
    components: {
      MyHeader: MyHeader,
      Carousal: Carousal,
      IntroduceStep: IntroduceStep,
      IntroduceTitle: IntroduceTitle,
      ProjectFace: ProjectFace,
      JoinUs: JoinUs,
      Joined: Joined,
      F: F,
      EnterpriseRecruitment: EnterpriseRecruitment
    }
  }
</script>
<style scoped lang='scss'>
  .introduce_block {
    display: flex;
  }

  .step {
    flex: 0 0 33.3%;
    max-width: 33.3%;
  }

</style>
