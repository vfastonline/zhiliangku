<template>
  <div>
    <career-path-carousel></career-path-carousel>
    <div class="career-path-list-subtitle mainwidth incenter font20pl3a3c50">选择你的职业</div>
    <container :myStyle="containerStyle">
      <interview-cover 
      v-for="(item,index) in pathList"
      :layout="['course']" 
      :mainData="item" 
      :key="index"
      :myStyle="itemStyle"
      :index="index"
      ></interview-cover>
    </container>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.career-path-list-subtitle{
  padding:80px 0px 32px;
}
</style>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      containerStyle:{className:['incenter','clearfix','mainwidth']},
      pathList:[],
      itemStyle:{
        className:['floatl','rise'],
      outerStyle:{
        'margin-right':'33px'
      },
      num:3
      }
    }
  },
  created(){
    this.$ajax.get('tracks/path/list/info').then(res=>{
      this.pathList=res.data.data
      this.$fn.addString(this.$myConst.httpUrl,res.data.data,'path_img')
      this.$fn.exchangeArrayObjectKey(this.pathList,['path_img','highest_salary','lowest_salary','name'],
      ['question_img','highest_monthly_salary','lowest_monthly_salary','position'],true)
      console.log(this.pathList)
    })
    
  }
}
</script>


