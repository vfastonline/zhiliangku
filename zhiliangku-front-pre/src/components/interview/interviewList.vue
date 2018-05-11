<template>
  <div class="mainwidth interview-list-container relative incenter">
    <div class="tags-container mainwidth incenter rised">
      <span>方向：</span>
      <span class="font16pr3a3c50 tags pointer" 
      :class="{'font16prffffff':item.id==activeId,'active':item.id==activeId}"
       v-for="(item,index) in tagsarr" :key="index" 
       @click="handleClick(item)"
        >{{item.name}}</span>
      <span  class="font16pr3a3c50 right-tags tags pointer vmiddle"
      :class="{'font16prffffff':completed,'active':completed}"
      @click="haveFinished()"
      >我已经完成的面试题</span>
    </div>
  </div>
</template>
<script>
import Bus from '../../assets/js/bus'
export default {
  name: 'HelloWorld',
  data () {
    return {
      tagsarr:[],
      activeId:'',
      completed:0
    }
  },
  props:{

  },
  methods:{
    handleClick(item){
      this.activeId=item.id;
      this.sendMsg(this.orgnizeData())
    },
    haveFinished(){
      this.completed=!this.completed*1;
      this.sendMsg(this.orgnizeData())
    },
    orgnizeData(){
      var obj={'is_completed':this.completed}
      if(this.activeId){
        obj.path_id=this.activeId
      }
      return obj
    },
    sendMsg(data){
      Bus.$emit('additionEnter',data)
    },
    getTags(){
      this.$get('/tracks/course/list/info').then(res=>{
        this.tagsarr=res.data.filter.course_path;
      console.log(this.tagsarr)
    })
    }
  },
  created(){
    this.getTags();
    this.activeId=this.$fn.funcUrl('path_id')||0;
    this.completed=this.$fn.funcUrl('is_completed')*1||0;
  },
  components:{
    
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.interview-list-container{
  margin-top:-35px;
  background: white;
}
.tags-container{
  height:70px;
  line-height: 70px;
  padding: 0 40px;
  box-sizing: border-box;
}
.tags{
  padding:4px 16px;
}
.right-tags{
  height:29px;
  line-height:29px;
  right:40px;
}
.active{
  background: #23B8FF;
}
</style>