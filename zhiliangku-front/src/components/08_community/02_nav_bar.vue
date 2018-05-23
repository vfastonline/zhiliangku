<template>
  <div class="mw">
    <span   class="nomoral cp font1_16_6" :class="{'active':activeTag==index}"  v-for="(item,index) in mainData" :key="index" @click="handleClick(item,index)" >{{item.label}}</span>
    <span class="dib search_block">
       <input v-model="search_value" @keydown.enter="get_search_data(search_value)" class="search_input "
              type="text" placeholder="请输入关键字">
            <img @click="get_search_data(search_value)" class="vb" src="./img/search.png" alt="">
    </span>
    <el-button @click="foucus" class="foucusButton fr">我要提问</el-button>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .nomoral{
    background: none;
    color: #3a3c50;
    padding:4px 16px;
  }
  .active{
    color: #ffffff;
    background: #23b8ff;
  }
  .search_block {
    width: 300px;
    margin-left:120px;
    border-bottom: 1px solid #ccc;
  }
  .search_input {
    border-top: 0px;
    border-left: 0px;
    border-right: 0px;
    border-bottom: 0;
    padding-left: 20px;
    outline: none;
    width: 200px;
    font-size: 16px;
    line-height: 30px;
    color: #ccc;
  }

  .foucusButton {
    corlor:white;
    background-color: #00bcd0;
  }
</style>
<script>
  import { Button } from 'element-ui'
  import Vue from 'vue'
  Vue.use(Button)
  export default {
    name: 'nav_bar',
    data () {
      return {
        activeTag:-1,
        search_value: '',
      }
    },
    props:{
      mainData:Array
    },
    methods:{
      handleClick(item,index){
        this.activeTag=index;
        this.$emit('haveClick',item)
      },
      foucus(){

      }
    },
    created(){

    },
    mounted(){
      this.handleClick({id:0},0)
    },
    components:{

    }
  }
</script>


