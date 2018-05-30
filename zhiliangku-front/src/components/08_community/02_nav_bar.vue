<template>
  <div class="mw">
    <span   class="nomoral cp font1_16_6" :class="{'active':activeTag==index}"  v-for="(item,index) in mainData" :key="index" @click="handleClick(item,index)" >{{item.label}}</span>
    <span class="dib search_block">
       <input v-model="search_value" @keydown.enter=" handleSearch(search_value)" class="search_input "
              type="text" placeholder="请输入关键字">
            <img @click="handleSearch(search_value)" class="vb searchBox" src="./img/search.png" alt="">
    </span>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .nomoral{
    background: none;
    padding:7px 30px;
  }
  .active{
    color: #ffffff;
    background: #23b8ff;
  }
  .search_block {
    width: 300px;
    margin-left:180px;
    border-bottom: 1px solid #ccc;
  }
  .search_input {
    border-top: 0px;
    border-left: 0px;
    border-right: 0px;
    border-bottom: 0;
    padding-left: 20px;
    outline: none;
    width: 220px;
    font-size: 16px;
    line-height: 30px;
  }
  .searchBox {
    cursor: pointer;
  }
  .foucusButton {
    corlor:white;
    background-color: #00bcd0;
  }
</style>
<script>
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
      handleSearch(data){

        this.$emit('searchClick',data)
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


