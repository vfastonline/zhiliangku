<template>
  <div class="block  fontcenter">
    <el-pagination 
    background
    @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="currentPage4" :page-sizes="[100, 200, 300, 400]"
      :page-size="12" layout="  prev, pager, next,total, jumper" :total="400">
    </el-pagination>
  </div>
</template>
<script>
//页码组件目标，外界仅可通过对象来初始化该组件
//本组件自身根据传入对象参数，进行请求，并且，请求之后的内容派给父实例
  export default {
    methods: {
      handleSizeChange(val) {
        console.log(`每页 ${val} 条`);
      },
      handleCurrentChange(val) {
        //这里需要一个将对象转换为search字段的函数，而且属于公用函数
        this.$get(this.mainData.linker)
      }
    },
    props:{
      mainData:Object,
      initData:Object
    },
    data() {
      return {
        currentPage1: 5,
        currentPage2: 5,
        currentPage3: 5,
        currentPage4: 4
      };
    },
    created(){

    }
  }

</script>
