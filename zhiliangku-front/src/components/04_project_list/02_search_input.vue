<template>
  <div class="addition_bar ftj mw hc">
          <span class="dib addition_tags">
            <span class="dib addition_tag font1_24_6 ftc cp" v-for="(item,index) in tags_arr"
                  :key="index" @click="get_data_addition(item)"
                  :class="{'font1_24_f':item.active,'selected':item.active}">{{item.name}}</span>
          </span>
          <span class="dib search_block">
            <input v-model="search_value" @keydown.enter="get_search_data(search_value)" class="search_input "
                   type="text" placeholder="请输入关键字">
            <img @click="get_search_data(search_value)" class="vb" src="./img/search.png" alt="">
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
    margin-top: 80px;
    margin-bottom: 60px;
  }

</style>
<script>
  import Bus from '../../assets/js/02_bus'
  export default {
    name: "search_input",
    data() {
      return {
        tags_arr: [],
        search_value: '',
        technology_id:''
        // search_data: ''
      }
    },
    methods: {
      get_data_addition(item) {
        // 这里面写入处理函数，目标为：将所有item的active属性变为false，然后将选中的item加上active属性。切记如果item中无active则要在刚刚请求到active的时候写入这个属性。
        this.handle_active(item)
        Bus.$emit('additionEnter', {
          'technology_id': item.id,
        })
      },
      handle_active(item) {
        this.tags_arr.forEach(el => {
          el.active = false
        })
        item.active = true
        this.technology_id=item.id
      },
      get_search_data(search_data) {
        if (search_data) {
          var id=this.technology_id
          Bus.$emit('additionEnter', {'name':search_data,'technology_id':id})
        }
      },
      //获取tags数据
      get_tags() {
        this.$get('/tracks/technology/list/info').then(res => {
          res.data.data.forEach(el => {
            el.active = false
          })
          this.tags_arr = res.data.data;
          if (res.data.data.length) {
            this.get_data_addition(res.data.data[0])
            // console.log(res.data.data[0]);
          }
        })
      }
    },
    created() {
      this.get_tags()
    },
  }
</script>

<style scoped>

</style>
