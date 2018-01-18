<template>
  <div class="block  fontcenter">
    <el-pagination 
    background
    @current-change="handleCurrentChange" :current-page="mainData.page" 
    :page-size="mainData.per_page" layout="  prev, pager, next,total, jumper" :total="mainData.total_count">
    </el-pagination>
  </div>
</template>
<script>
//页码组件目标，外界仅可通过对象来初始化该组件
//本组件自身根据传入对象参数，进行请求，并且，请求之后的内容派给父实例
import Bus from '../../assets/js/bus'
  export default {
    data() {
      return {
        currentPage:1
      };
    },
     props:{
      mainData:Object,
      initData:Object
    },
    methods: {
      handleCurrentChange(val) {
        //这里需要一个将对象转换为search字段的函数，而且不用属于公用函数
        this.mainData.page=val;
        console.log(this.mainData)
        this.$get(this.mainData.url+this.objToSearch(this.mainData.params)+'page='+val).then(res=>{
    
    Bus.$emit('pagerHaveData',res)
        })
      },
      objToSearch(obj){
        var str='?';
        for(var k in obj){
          str=str+k+'='+obj[k]+'&';
        }
        return str;
      }
    },
    created(){
      console.log('hehei')
      console.log(this.mainData)
    }
  }

</script>
