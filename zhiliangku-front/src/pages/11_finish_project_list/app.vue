<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <SearchBar class="topBar"></SearchBar>
      <section class="project_list">
        <CardContainer v-if="main_data.length" class="mw hc "
                       :config="{num:3,card:Finish_project_list,cardData:main_data[0]}">
          <Finish_project_list v-for="(item,index) in main_data" :key="item.id" :main_data="item"
                               :top_color="color_arr[index%6]" class="margin"></Finish_project_list>
        </CardContainer>
        <div v-else class="ftc font1_16_9">暂无信息</div>
      </section>
      <div class="throwBox  ftc">
        <BlueButton><span class="throwButton">投递简历</span></BlueButton>
      </div>
      <Pager class="mw hc" @pagerGetData="mainPagerData" :url="url" :firstData="true"  :style="{'margin-bottom': '80px'}"></Pager>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>
  .project_list {
    min-height:75vh;
  }
  .margin {
    margin-bottom: 30px;
  }

  .topBar {
    margin-top: 20px;
    margin-bottom: 40px;
  }

  .throwBox {
    margin: 20px 0 82px 0;
  }

  .throwButton {
    padding-left: 37px;
    padding-right: 37px;
  }

</style>

<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import '../../components/00_common/05_card_container'
  import Finish_project_list from '../../components/13_finish_project_list/01_finish_project_list'
  import F from '../../components/01_header_footer/03_footer'
  import Pager from '../../components/00_common/06_pager'
  import SearchBar from '../../components/13_finish_project_list/03_search_bar'
  import BlueButton from '../../components/00_common/04_blue_button'

  export default {
    data() {
      return {
        Finish_project_list: Finish_project_list,
        url: '/employment/finishprojectlistinfo/list/info',
        main_data: '',
        color_arr: ['#324e5c', '#c25975', '59769f', '8ea55e', '8d6e6e', '7b558e']
      }
    },
    components: {
      MyHeader: MyHeader,
      Finish_project_list: Finish_project_list,
      F: F,
      Pager: Pager,
      SearchBar: SearchBar,
      BlueButton: BlueButton
    },
    methods: {
      mainPagerData(res) {
        if (!res.err) {
          console.log(res.data)
          this.main_data = res.data.data
        }
      }

    }
  }
</script>
