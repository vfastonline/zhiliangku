<template>
  <div class="mw hc">
    <div class="resultTab mw hc clearfix">
      <span class="dib tabText font1_40_f">大牛排行榜</span>
      <span class="dib search_block fr vm">
        <input v-model="search_value" @keydown.enter=" handleSearch(search_value)" class="search_input "
               type="text" placeholder="请输入关键字">
        <img @click="handleSearch(search_value)" class="searchBox vm" src="./img/search.png" alt="">
      </span>
    </div>
    <SelfResultInfo :main_data="main_data" class="result_self"></SelfResultInfo>
  </div>

</template>
<script>
  import SelfResultInfo from './02_leaderboard_result_info'

  export default {
    data() {
      return {
        search_value: ''
      }
    },
    components: {
      SelfResultInfo: SelfResultInfo
    },
    props: {
      main_data: ''
    }
  }
</script>
<style scoped lang="scss">
  .resultTab {
    border-radius: 10px 10px 0 0;
    background-color: #233b47;

  }

  .search_block {
    width: 300px;
    height: 80px;
    line-height: 80px;
  }

  .tabText {
    line-height: 80px;
    margin-left: 100px;
  }

  .search_input {
    border-top: 0px;
    border-left: 0px;
    border-right: 0px;
    border-bottom: 1px solid #fff;;
    padding-left: 20px;
    outline: none;
    width: 246px;
    font-size: 18px;
    line-height: 43px;
    color: #fff;
    background-color: #233b47;
  }

  input::-moz-placeholder { /* Mozilla Firefox 19+ */
    color: #fff;
  }

  input::-webkit-input-placeholder {
    color: #fff;
  }

  .searchBox {
    margin-left: -36px;
  }

  .result_self {
    background-color: #fbfaf9;
    border-radius: 0 0 10px 10px;
    margin-bottom: 94px;
  }
</style>
