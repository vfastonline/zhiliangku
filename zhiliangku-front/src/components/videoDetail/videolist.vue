<template>
  <div class="videolist">
    <el-dialog :visible.sync="showDialog" 
    @open="changeIndex()"    
    :top="'70px'">
      <div class="videolist-container " >
        <el-scrollbar class="vdc-el-scrollbar" :style="{'height':maxheight+'px'}">
          <div class="videolist-wrap">
            <div class="marginbottom24 textellipsis">
              <span class="font20pl3a3c50" :title="mainData.name">{{mainData.name}}</span>
            </div>
            <ul v-for="(item,index) in mainData.sections" :key="index" class="marginbottom32">
              <li class="font14pl5A646E marginbottom8 videolist-section" :title="item.title">{{item.title}}</li>
              <li class="font20pl3a3c50 marginbottom16" :title="item.desc">{{item.desc}}</li>
              <li v-for="(li,liIndex) in item.videos" :key="liIndex" 
              class="font14pl5A646E marginbottom16 pointer "
              @click="goPages(li)"
              >
                <span class="vlw-video-name textellipsis" :title="li.name" @click="goInformation(li.id,li.type)">{{li.name}}</span>
              </li>
            </ul>
          </div>
        </el-scrollbar>
      </div>
    </el-dialog>
  </div>
</template>
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
      showVideoList() {
        this.$parent.$emit('showVideoList')
      },
      goInformation(id, type) {
          
      },
      goPages(obj){
        switch(obj.type*1){
          case 1:
          case 2 : window.location.href='/tracks/video/detail/?course_id='+this.$fn.funcUrl('course_id')+'&video_id='+obj.id+'#/note'; break;
          case 3: window.location.href='/tracks/video/detail/?course_id='+this.$fn.funcUrl('course_id')+'&video_id='+obj.id+'&type=3'; break;
          case 4: window.location.href='/exercise/list/?course_id='+this.$fn.funcUrl('course_id')+'&video_id='+obj.id; break;
          default: break;
        }
      },
      changeIndex(){
      }
    },
    created() {
      console.log(window.innerHeight)
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
    }
  }

</script>
<style lang='scss'>
.videolist .el-dialog{
    position: absolute;
    margin-top: 0%;
    left:0px;
}
  .videolist-container {
    width: 400px;
    max-height: 800px;
    padding: 21px 0px 0px 41px;
    position: absolute;
    background: white;
    z-index: 10002;
    top: 0%;
    left: 0%;
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

  .videolist-wrap {
    margin-right: 35px;
    background-attachment: white;
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
