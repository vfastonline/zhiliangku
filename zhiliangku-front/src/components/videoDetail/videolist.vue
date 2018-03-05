<template>
  <div class="videolist">
    <el-dialog :visible.sync="showDialog" 
    @open="changeIndex()"    
    :top="getHeight()">
      <div class="videolist-container  " >
        <el-scrollbar class="vdc-el-scrollbar" :style="{'height':maxheight+'px'}">
          <div class="videolist-wrap">
            <div class=" textellipsis thispadding0">
              <span class="font20plffffff pointer  " :title="mainData.name" @click="goToCourse(mainData.id)">{{mainData.name}}</span>
            </div>
            <ul v-for="(item,index) in mainData.sections" :key="index" class="marginbottom32">
              <li class="font14plffffff  videolist-section thispadding0" :title="item.title">{{item.title}}</li>
              <li class="font20plffffff  thispadding0" :title="item.desc">{{item.desc}}</li>
              <li v-for="(li,liIndex) in item.videos" :key="liIndex" 
              class="font14plffffff  pointer section-li thispadding1"
              @click="goPages(li)"
              >
                <span class="vlw-video-name textellipsis" :title="li.name" @click="goInformation(li.id,li.type)">{{li.name}}</span>
                <img v-if="statusShow(li,1)" src="../../assets/img/icons/path+路线+课程_图标/课程详情_已完成对勾.svg" alt="">
                <span v-if="statusShow(li,2)">{{li.live_start_time}}</span>
              </li>
            </ul>
          </div>
        </el-scrollbar>
      </div>
    </el-dialog>
  </div>
</template>
<style lang='scss'>
.videolist .el-dialog{
    width: 400px;
    // overflow: hidden;
    position: absolute;
    margin-top: 0%;
    left:0px;
    background: #535762;
}
  .videolist-container {
    width: 400px;
    overflow: hidden;
    max-height: 800px;
    position: absolute;
    background: #535762;
    z-index: 10002;
    top: 0%;
    left: 0%;
  }
  .thispadding0{
    padding: 8px 30px 8px 40px;
  }
  .thispadding1{
    padding: 8px 30px 8px 50px;
  }
  .vdc-el-scrollbar {
    .el-scrollbar__wrap {
      overflow-y:scroll;
      overflow-x: hidden;
    }
  }

  .videolist-section {
    opacity: 0.5;
  }
  .section-li{
    display: flex;
    justify-content: space-between;
  }
  .section-li:hover{
    background: #22252B;
  }
  .videolist-wrap {
    // margin-right: 35px;
    background-attachment: #535762;
  }

  .videolist-close {
    height: 14px;
    width: 14px;
    margin-right: 16px;
    vertical-align: middle;
  }

  .vlw-video-name {
    display: inline-block;
    max-width: 260px;
  }
</style>

<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        mainData: {},
        showDialog: false,
        maxheight:''
      }
    },
    methods: {
      getHeight(){
        var sy=window.scrollY;
        if(sy<70){
          return 70-sy+'px'
        }
        else{
         return 0+'px' 
        }
      },
      statusShow(li,type){
        var t1=function(li){
          if(li.is_complete){
            return true
          }
          else{
            return false
          }
        };
        var t2=function(li){
          if(li.is_complete){
            return false
          }
          else{
            return true
          }
        }
        switch(type){
          case 1: return t1(li) ;break;
          case 2:return t2(li) ; break;
          default: break;
        }
      },
      showVideoList() {
        this.$parent.$emit('showVideoList')
      },
      goInformation(id, type) {
          
      },
      goToCourse(id){
        window.location.href='/tracks/course/detail/?course_id='+id+'&custom_user_id='+localStorage.uid;
      },
      goPages(obj){
        switch(obj.type*1){
          case 1:
          case 2 : window.location.href='/tracks/video/detail/?course_id='+this.$fn.funcUrl('course_id')+'&video_id='+obj.id+'#/note'; break;
          case 3: window.location.href='/tracks/live/detail/?course_id='+this.$fn.funcUrl('course_id')+'&video_id='+obj.id; break;
          case 4: window.location.href='/exercise/list/?course_id='+this.$fn.funcUrl('course_id')+'&video_id='+obj.id; break;
          default: break;
        }
      },
      changeIndex(){
      }
    },
    created() {
      // console.log(window.innerHeight)
      if(window.innerHeight){
        this.maxheight=window.innerHeight-70;
      }
      //如果别的页面依然需要这个函数，那么我会把这些东西抽离出来
      this.$on('openDialog', function () {
        this.showDialog = !this.showDialog;
      })
      var course_id = this.$fn.getSearchKey('course_id');
      var include_video = 1;
      this.$get('/tracks/course/detail/info?course_id=' + course_id + '&include_video=1').then(res => {
        console.log(res)
        this.mainData = res.data.data;
      })
    },
    mounted(){
    }
  }

</script>
