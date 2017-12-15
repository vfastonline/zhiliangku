<template>
  <div class="mainwidth incenter ">
      <div class="courseSelect">
          <!-- 此处列表如何获取呢 -->
          <div class='cs-taglist'>
              <span class="cst-type floatl">方向：</span>
              <div class="clearfix cst-tagcontainer">
                  <ul class="cstt-tags">
                      <li class="font16pr3a3c50" 
                      v-for="(item,index) in allData.filter.course_path"
                      :key="index">
                          <span 
                          :class="{'cstt-selected':item.active}"
                          @click="changeSlected(item,'course_path')">{{item.name}}</span>
                      </li>
                  </ul>
              </div>
          </div>
          <div class='cs-taglist'>
              <span class="cst-type floatl">分类：</span>
              <div class="clearfix cst-tagcontainer">
                  <ul class="cstt-tags">
                      <li v-for="(item,index) in allData.filter.technology" :key="index">
                          <span @click="changeSlected(item,'technology')"
                          :class="{'cstt-selected':item.active}"
                          >{{item.name}}</span>
                      </li>
                  </ul>
              </div>
          </div>
      </div>
      <container :myStyle="{className:['clearfix']}">
              <hot-course
              v-for="(item,index) in allData.data"
              :key="index"
              :index="index"
              :myStyle="hotCourseStyle"
              :mainData="item"
              ></hot-course>
          </container>
  </div>
</template>
<script>
export default {
  data() {
    return {
        url:'tracks/course/list/info',
        allData:{filter:[]},
        containerStyle:{
            classname:['mainwidth incenter']
        },
        hotCourseStyle:{
            outerStyle:{width:'264px','margin-right':'32px'},
            imgStyle:{height:'148px'},
            num:4
        },
        course_path:0,
        technology:0,
        page_number:''
    };
  },
  methods:{
      addtionalString(){
          return this.url+'?coursepath_id='+this.course_path+'&technology_id='+this.technology;
      },
      changeSlected(item,key){
          //状态标签清零
          var arr=this.allData.filter[key];
          for(var i=0;i<arr.length;i++){
              if(arr[i].active){
                  arr[i].active=0;
              }
          }
          //标记高亮
          item.active=1;
          if(key=='course_path'){
              this.technology=0;
          }
          this[key]=item.id;
          this.getData(this.addtionalString())
      },
      getData(myurl){
          if(!myurl){
              myurl=this.url
          }
          this.$ajax.get(myurl).then(res=>{
          this.$fn.addString(this.$myConst.httpUrl,res.data.data,['course_img','avatar'])
          var filter=res.data.data.filter;
          for(var k in filter){
              for(var i=0;i<filter[k].length;i++){
                  if(!filter[k][i]['active']){
                      filter[k][i]['active']=1;
                  }
              }
          }
          this.allData=res.data;
          console.log(res)
      })
      }
  },
  created(){
      this.getData()
  }
};
</script>
<style scoped lang="scss">
.courseSelect {
  padding-top: 60px;
  padding-bottom: 40px;
//   background: pink;
}
.cst-tagcontainer{
    margin-left:64px;
}
.cstt-tags li{
    display:inline-block;
    margin-bottom:16px;
    span{
        padding:4px 16px;
    }
}
.cstt-selected{
    background: #23B8FF;
    color:white;
}
</style>



