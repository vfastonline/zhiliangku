<template>
  <div class="block  fontcenter">
    <el-pagination background @current-change="handleCurrentChange" :current-page="mainData.page*1" :page-size="mainData.per_page*1"
      layout="  prev, pager, next,total, jumper" :total="mainData.total_count*1">
    </el-pagination>
  </div>
</template>
<script>
  //页码组件目标，外界仅可通过对象来初始化该组件
  //本组件自身根据传入对象参数，进行请求，并且，请求之后的内容派给父实例
  // 组件说明：
  // 1.首先这里面的mainData实际上是页码信息。
  // 2.url是基础路径。
  // 3.主要通过bus.js来传递信息
  // 4.想要改版成不依赖bus.js的版本。
  import Bus from '../../assets/js/bus'
  //接下来要实现的是关联url这一增加功能
  export default {
    data() {
      return {
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
        addition: {}
      };
    },
    watch: {
      mainData: function (val) {},
      addition: function (val) {
        this.handleCurrentChange()
      }
    },
    props: {
      //url为必传参数
      url: String,
      initParam: Object,
      pageData:Object
    },
    methods: {
      orgnizeUrl(val) {
        var search = this.objToSearch(this.addition);
        var search1 = '';
        if (this.initParam)(
          search1 = '&' + this.objToSearch(this.initParam)
        );
        var pageInfo = '';
        if (val) {
          pageInfo = '&page=' + val;
        }
        return this.url + '?' + search + search1 + pageInfo;
      },
      handleCurrentChange(val) {
        this.getData(val)
      },
      getData(val) {
        this.$get(this.orgnizeUrl(val)).then(res => {
          // res.data.paginator.total_count = 100;
          if(JSON.stringify( res.data.paginator)!='{}'){
            this.mainData = res.data.paginator;
          }
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
      getaddition() {
        var str = window.location.search;
        if (!str) return true;
        var tstr = str.substr(1);
        var arr = tstr.split('&');
        var obj = {};
        arr.forEach((i) => {
          obj[i.split('=')[0]] = i.split('=')[1]
        })
        // if(JSON.parse(JSON.stringify(obj)))
        this.addition = obj;
        return false
      }
    },
    created() {
      if (this.getaddition()) {
        this.getData()
      }
      if(this.pageData){this.mainData=this.pageData}
      Bus.$on('additionEnter', res => {
        debugger
        window.location.search = this.objToSearch(res)
        
      })
    }
  }

</script>
