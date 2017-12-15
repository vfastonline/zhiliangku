<template>
  <div class="mainwidth incenter">
    <el-pagination class="fontcenter"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="currentPage"
      :page-sizes="[100, 200, 300, 400]"
      :page-size="100"
      layout="total, sizes, prev, pager, next, jumper"
      :total="400">
    </el-pagination>
  </div>
</template>
<style lang='scss'>

</style>
<script>
export default {
  data(){
      return {
          currentPage:1
      }
  },
  methods:{
      handleCurrentChange(val){
          this.currentPage=val
      }
  },
  props:{
    //   currentPage:[],
  }
}
</script>


