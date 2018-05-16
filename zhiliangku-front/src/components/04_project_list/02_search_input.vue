<template>
  <div class="addition_bar ftj mw hc">
          <span class="dib addition_tags">
            <span @click="get_data_addition" class="dib addition_tag font1_24_4 ftc" v-for="(item,index) in testArr"
                  :key="index" :class="{'font1_24_f':item.active,'selected':item.active}">{{item}}</span>
          </span>
    <span class="dib search_block">
            <input class="search_input " type="text" placeholder="请输入关键字">
            <img @click="get_search_data" class="vb" src="./img/search.png" alt="">
          </span>
    <span class="line2"></span>
  </div>
</template>
<style>
  .selected {
    background-color: #00bcd5;
  }

  .addition_tag {
    width: 160px;
    line-height: 42px;
    border-radius: 4px;
  }

  .search_input {
    border-top: 0px;
    border-left: 0px;
    border-right: 0px;
    border-bottom: 0;
    padding-left: 20px;
    outline: none;
    width: 330px;
    font-size: 22px;
    line-height: 42px;
  }

  .search_block {
    width: 410px;
    border-bottom: 1px solid #ccc;
  }

  .addition_tags {
    max-width: 650px;
  }

  .addition_bar {
    margin-bottom: 60px;
  }

</style>
<script>
    export default {
        name: "search_input",
      data(){
          return {
            testArr: ['大数据', '运维', '大数据', '运维', '大数据', '运维', '大数据', '运维', '大数据', '运维', '大数据', '运维'],
          }
      },
      methods: {
        get_data_addition() {
          // 这里面写入处理函数，目标为：将所有item的active属性变为false，然后将选中的item加上active属性。切记如果item中无active则要在刚刚请求到active的时候写入这个属性。
        },
        get_search_data(){

        }
      },
    }
</script>

<style scoped>

</style>
