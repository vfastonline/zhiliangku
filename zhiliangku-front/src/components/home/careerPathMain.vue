<template>
  <div class="careerPath">
      <subtitle :msg="msg"></subtitle>
      <div class="cpm-content">
          <carrerps v-for="(item,index) in ajaxData" :key="index" :mainData="item"></carrerps>
      </div>
  </div>
</template>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: {
          enTitle:'Career Path',
            title:'职业路径',
            slogon:'升值加薪必学',
            linker:'/tracks/path/list/'
      },
      ajaxData:[]
    }
  },
  created(){
    // console.log(this.$myConst)
    this.$get('/tracks/index_path/list').then(res=>{
      // console.log(res)
      this.ajaxData=res.data.data;
      for(var i=0;i<this.ajaxData.length;i++){
      this.ajaxData[i].index=i%2;
      this.ajaxData[i]['path_img']=this.$myConst.httpUrl+this.ajaxData[i]['path_img']
    }
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style >
.careerPath{
      background:#fafafa; 
}
.cpm-content{
    display: flex;
    justify-content: center ;
    flex-wrap: wrap;
    padding-bottom:40px;
}
</style>


