<template>
  <div>
    <div class="main">
      <MyHeader></MyHeader>
      <FooterImage :S="{height:'300px'}"
        :src="$myConst.httpUrl+'/media/image/static/project_list_01_top.png'"></FooterImage>
      <!--<div v-html="str"></div>-->
      <SearchInput></SearchInput>
      <section class="project_list">
        <CardContainer v-if="project_lists.length" class="mw hc " :config="{num:3,card:ProjectStep,cardData:project_lists[0]}">
            <ProjectStep  v-for="(item, index) in project_lists" v-if="item" :key="item.id" :top_color="color_arr[index%4]"  :main_data="item" class="margin"></ProjectStep>
        </CardContainer>
        <div v-else class="ftc font1_16_9">{{no_data_str}}</div>
      </section>
      <Pager class="mw hc" @pagerGetData="mainPagerData" :url="url" ></Pager>
      <FooterImage :src="$myConst.httpUrl+'/media/image/static/project_list_02_bottom.png'"></FooterImage>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>
  .bottom_image{
    background: url("./img/01_city.png");
  }
  .margin {
    margin-bottom: 40px;
  }


  .project_list {
    /*margin: 120px 0px;*/
    min-height: 70vh;
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
  import FooterImage from '../../components/00_common/08_image_block'

  export default {
    data() {
      return {
        ProjectStep: ProjectStep,
        url:'/tracks/projects/list/info',
        project_lists: [],
        no_data_str:'',
        color_arr: ['#647a90','#c25975','#59769f','#329577']
      }
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      ProjectStep: ProjectStep,
      Pager: Pager,
      SearchInput: SearchInput,
      FooterImage:FooterImage
    },
    methods: {
      //获取pager分页组件返回的分页数据
      mainPagerData(res) {
        this.project_lists = res.data.data
        // console.log( res.data.data )
      }
    },
    created(){
    }
  }
</script>
