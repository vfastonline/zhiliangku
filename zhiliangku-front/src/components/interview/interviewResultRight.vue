<template>
  <div class="">
      <div>
    <div>你尚未掌握的知识点有</div>
    <div><el-button v-for="(item, index) in  mainData.tech_name_list" :key="index" :class="{'firstbutton':!index}">{{item}}</el-button><el-button>Yaml</el-button></div>
    </div>
    <div>
        <div>你可以通过    以下课程补充学习到这些知识点</div>
        <container>
          <hotCourse :myStyle="hotCourseStyle" v-for="(item,index) in course_list" :key="index" :index="index" :mainData="item"></hotCourse>
        </container>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.firstbutton{
    margin-left:8px;
}
</style>
<script>
import container from '../courseInfo/container'
import hotCourse from '../home/hotCourse'
export default {
  name: 'HelloWorld',
  data () {
    return {
        hotCourseStyle:{
            outerStyle:{width:'264px','margin-right':'32px'},
            imgStyle:{height:'148px'},
            num:2
        },
        mainData:{},
        course_list:[],
    }
  },
  props:{
  },
  methods:{

  },
  created(){
      this.$get('/interview_questions/enterprise/result/info?custom_user_id=' + localStorage.uid +
        '&enterpriseinfo_id=' + this.$fn.funcUrl('enterpriseinfo_id')).then(res => {
            this.$fn.addString(this.$myConst.httpUrl,res.data.data.course_list,'course_img')
            this.$fn.addString(this.$myConst.httpUrl,res.data.data.course_list,'avatar')
         this.mainData = res.data.data;
         this.course_list = this.mainData.course_list;
        console.log(res)
      })
  },
  components:{
    container:container,
    hotCourse:hotCourse
  }
}
</script>


