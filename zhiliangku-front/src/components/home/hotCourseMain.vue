
<template>
  <div>
      <subtitle :msg="msg"></subtitle>
      <div class="hcm-content">
          <div class="hcmc-c incenter">
            <hot-course 
            :myStyle="{'num':4,'outerStyle':{'width':'276px','margin-right':'16px'}}"
            v-for="(item,index) in hotCourseData" :index="index" :key="item.id" :mainData="item" ></hot-course>
          </div>
      </div>
  </div>
</template>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: {
          enTitle:'Hot Course',
            title:'热门课程',
            slogon:'优质课程，免费学习'
      },
      hotCourseData:{}
    }
  },
  created(){
    this.$ajax.get('tracks/index_course/list').then(res=>{
      // console.log(res)
      this.hotCourseData=this.$fn.addString(this.$myConst.httpUrl,res.data.data,['course_img','avatar'])
      // console.log(this.hotCourseData)
    })
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hcm-content{
  width:100%;
  position: relative;
}
.hcmc-c{
  /* position: relative;
  left: 0px;
  right: 0px; */
  /* margin:auto; */
  display:flex;
  width:1152px;
  height: 490px;
  padding-bottom: 32px;
  justify-content:space-between;
  flex-wrap:wrap;
}
</style>



