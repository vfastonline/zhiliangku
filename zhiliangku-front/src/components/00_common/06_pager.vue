<template>
  <div class="block  pager">
    <!-- 注意这个是功能最完善的页码组件 -->
    <el-pagination background @current-change="handleCurrentChange" :current-page="mainData.page*1"
                   :page-size="mainData.per_page*1"
                   layout="  prev, pager, next,total, jumper" :total="mainData.total_count*1">
    </el-pagination>
  </div>
</template>
<style>
  .pager {
    text-align: center;
  }
</style>
<script>
  //页码组件目标，外界仅可通过对象来初始化该组件
  //本组件自身根据传入对象参数，进行请求，并且，请求之后的内容派给父实例
  // 组件说明：
  // 1.首先这里面的mainData实际上是页码信息。
  // 2.url是基础路径。
  // 3.主要通过bus.js来传递信息
  // 4.想要改版成不依赖bus.js的版本。
  // 5.initParam作用是:固定参数
  // 6.现在支持两种方式来传递消息，bus和父子组件
  import Bus from '../../assets/js/02_bus'
  //接下来要实现的是关联url这一增加功能
  import Vue from 'vue'
  import {Pagination} from 'element-ui'

  Vue.use(Pagination)
  export default {
    data() {
      return {
        urlAddition: '',
        // currentPage没啥用  先预留着吧
        currentPage: 1,
        mainData: {
          "per_page": 12,
          "total_count": 0,
          "num_pages": 1,
          "page": 1,
          "page_range": [
            1
          ]
        },
        addition:{},
        // 备份
        storeMainData: {
          "per_page": 12,
          "total_count": 0,
          "num_pages": 1,
          "page": 1,
          "page_range": [
            1
          ]
        }
      };
    },
    watch: {
      addition: {
        handler: function () {
          this.handleCurrentChange(1)
        },
        deep: true
      }
    },
    props: {
      //url为必传参数
      url: String,
      // 这里是外部传入的不变的参数
      initParam: Object,
      // 页码信息此处页码信息不用关心，除非后端调整了页码信息所在的层级
      pageData: Object,
      // 附加的可变条件
      additionData: Object,
      // 是否保持urlAddition
      keep: Boolean,
      // 页码组件加载之后，是否立即请求数据。
      firstData: Boolean
    },
    methods: {
      orgnizeUrl(val) {
        // 这里是组织url将各种条件混合起来
        // 首先将传递的条件序列化
        var search1 = '', search2 = '';
        var search = this.objToSearch(this.addition);
        // 这里传递的是固定不变的参数。理论上讲此处与urlAddition无差别，但是可以将urlAddition进行配置，来决定是否要它；
        if (this.initParam) (
          search1 = '&' + this.objToSearch(this.initParam)
        );
        if (this.urlAddition && this.keep) {
          search2 = '&' + this.objToSearch(this.urlAddition);
        }
        var pageInfo = '';
        if (val) {
          pageInfo = 'page=' + val;
          if (search + search1) {
            pageInfo = '&' + pageInfo;
          }
        }
        return this.url + '?' + search + search1 + search2 + pageInfo;
      },
      handleCurrentChange(val) {
        this.getData(val)
      },
      getData(val) {
        this.$get(this.orgnizeUrl(val)).then(res => {
          // res.data.paginator.total_count = 100;
          //利用返回的页码信息来初始化页码
          if (JSON.stringify(res.data.paginator) != '{}') {
            this.mainData = res.data.paginator;
          } else {
            this.mainData = this.storeMainData;
          }
          //向父组件传递消息,同时也可通过Bus的方式进行传递，遗憾的是目前不支持import在函数中使用，所以
          //无法通过传参数的形式确定Bus的路径，建议使用时候，直接定义好全局Bus的路径
          this.$emit('pagerGetData', res)
          Bus.$emit('pagerGetData', res)
        })
      },
      objToSearch(obj) {
        var str = '';
        for (var k in obj) {
          str = str + k + '=' + obj[k] + '&';
        }
        if (str.length == 1) {
          return str
        }
        return str.slice(0, -1);
      },
      initMainData(initData) {
        this.mainData = initData;
      },
      getAddition() {
        //这里主要是获取url中自带的初始参数，而且这个参数相当于initParam的一部分
        var str = window.location.search;
        if (!str) return true;
        var tstr = str.substr(1);
        var arr = tstr.split('&');
        var obj = {};
        arr.forEach((i) => {
          obj[i.split('=')[0]] = i.split('=')[1]
        })
        if (JSON.stringify(obj) != '{}') {
          this.urlAddition = obj;
        }
      },
      upData() {
        var count = this.mainData.total_count;
        var size = this.mainData.per_page;
        var cpage = this.mainData.page;
        console.log(count % size)
        if (!(count % size) && count) {
          this.getData(cpage + 1);
          return
        }
        this.getData(this.mainData.page);
      }
    },
    created() {
      if(this.additionData){
      this.addition=this.additionData
      }
      this.getAddition();
      Bus.$on('additionEnter', res => {
        this.addition = res
      })
      if (this.firstData) {
        this.getData(1)
      }
      Bus.$on('updated', () => {
        this.upData()
      })
      //目前不觉的有用
      // if (this.pageData) {
      //   this.mainData = this.pageData
      // }
    }
  }

</script>
