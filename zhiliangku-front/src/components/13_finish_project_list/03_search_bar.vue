<template>
  <div class="resultTab mw hc clearfix">
    <span class="dib tabText font1_34_f">完成项目</span>
    <span class="dib search_block fr vm">
        <input v-model="search_value" @keydown.enter=" handleSearch(search_value)" class="search_input "
               type="text" placeholder="请输入关键词">
        <img @click="handleSearch(search_value)" class="vm cp searchBox" src="./img/search.png" alt="">
      </span>
  </div>
</template>
<script>
  import Bus from '../../assets/js/02_bus'
  export default {
    data() {
      return {
        search_value: ''
      }
    },
    methods: {
      handleSearch(data) {
        if(data) {
          Bus.$emit("additionEnter",{name: data})
        }
      }
    }
  }
</script>
<style scoped lang="scss">
  .resultTab {
    border-radius: 10px;
    background-color: #233b47;

  }

  .search_block {
    width: 300px;
    height: 60px;
    line-height: 60px;
  }

  .tabText {
    line-height: 60px;
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
    font-size: 16px;
    line-height: 36px;
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
</style>
