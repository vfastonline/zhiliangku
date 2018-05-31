<template>
  <div class="result">
    <searchBar :main_data="custom_user"></searchBar>
    <resultInfo v-for="item in main_data" :key="item.id" :main_data="item" class="result_other"></resultInfo>
    <pager :url="url" :first-data="true" @pagerGetData="mainPagerdata" :style="{'margin': '50px 0 158px 0'}"></pager>
  </div>
</template>
<style scoped lang='scss'>
  .result_other {
    background-color: #fff;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.15);
    margin-bottom: 30px;
    border-radius: 10px;
  }

  .result-other :last-child {
    margin-bottom: 80px;
  }
</style>
<script>
  import resultInfo from './02_leaderboard_result_info'
  import pager from '../../components/00_common/06_pager'
  import searchBar from './03_search_bar'

  export default {
    data() {
      return {
        url: '/employment/leaderboard/list/info',
        params: '',
        main_data: '',
        custom_user: '',
      }
    },
    components: {
      resultInfo: resultInfo,
      searchBar: searchBar,
      pager: pager,
    },
    methods: {
      mainPagerdata(res) {
        if (!res.err) {
          console.log(res.data)
          this.main_data = res.data.data
          this.custom_user = res.data.custom_user
        }
      }
    },
  }
</script>
