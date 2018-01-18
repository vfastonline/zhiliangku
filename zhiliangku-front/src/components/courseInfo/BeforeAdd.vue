<template>
  <div class="beforeAdd">
    <div class="ba-header flexstartcenter" :style="{'background-image':'url(' +allData.course_img +')'}">
      <div class="font36plffffff">{{allData.name}}
        <img @click="collect()" v-if="!allData.is_collect" class="bah-star pointer" src="../../assets/img/icons/path+路线+课程_图标/课程详情_收藏_空心.svg" alt="">
        <img @click="collect()" v-if="allData.is_collect" class="bah-star pointer" src="../../assets/img/icons/path+路线+课程_图标/课程详情_收藏_实心.svg" alt="">
      </div>
      <div class="fontcenter">
        <div class="font14plffffff bah-tag1">课程时长</div>
        <div class="font14plffffff bah-tag2">
          <span class="font16plffffff">{{Math.floor( allData.remaining_time/60)}} </span>小时
          <span class="font16plffffff">{{allData.remaining_time%60}} </span>分</div>
      </div>
      <div>
        <el-button class="font20plffffff" :style="buttonStyle" @click="learn(allData.is_study_record)" >{{allData.is_study_record?'继续学习':'开始学习'}}</el-button>
      </div>
    </div>
    <div v-if="allData.participate" class="ba-progressbar">
      <div :style="{'width':allData.schedule*100+'%'}" class="ba-progressbar-inner"></div>
      <div class="ba-progress-tip  font12plffffff"
      :class="{'ba-progress-tip-left':allData.schedule*100<2,'ba-progress-tip-right':allData.schedule*100>98}"
      :style="{'left':allData.schedule*100+'%'}" >{{allData.schedule*100+'%'}}
        <div class="bapt-squer " :class="{'bapt-squer-left':allData.schedule*100<2,'bapt-squer-right':allData.schedule*100>98}"></div>
      </div>
    </div>
    <div class="ba-main mainwidth incenter clearfix">
      <div class="ba-teacherInfo rise floatl">
        <ul class="ba-teacherInfo-ul">
          <li>
            <img class="floatl bam-teachericon" :src="allData.avatar" alt="">
            <ul class="bam-teacherInfo">
              <li class="font14pl3a3c50 name">{{allData.lecturer}}</li>
              <li class="font14pl5A646E job">{{allData.position}}</li>
            </ul>
          </li>
          <li>
            <ul class="bamt-uls">
              <li class="bamt-uls-title font16pl3a3c50">先修要求</li>
              <li class="font14pl3a3c50" v-html="allData.prerequisites"></li>
            </ul>
          </li>
          <li>
            <ul class="bamt-uls">
              <li class="bamt-uls-title font16pl3a3c50">你将学到什么</li>
              <li v-html="allData.learn">
              </li>
            </ul>
          </li>
        </ul>
      </div>
      <div class="floatr ba-progress">
        <p class="bap-p">{{allData.learn}}</p>
        <div class="bap-all">
          <el-collapse accordion @change="jj" v-model="activeName" >
            <el-collapse-item 
            v-for="(item,index) in allData.sections" :key="index"
            :name="index+1"
            >
              <template slot="title">
                <img class="beforeadd-img-icons" v-if="activeName==index+1" src="../../assets/img/icons/path+路线+课程_图标/课程详情_收起.svg" alt="">
                <img class="beforeadd-img-icons" v-else src="../../assets/img/icons/path+路线+课程_图标/课程详情_展开.svg" alt="">
                <span class="title-tag font14pl5A646E">{{item.title}}</span>
                <span class="title-tag font20pl3a3c50 " >{{item.desc}}</span>
              </template>
              <div  class="bap-container clearfix">
                <ul  class="incenter floatr bapc-videos">
                  <li v-if="allData.container[index].data" 
                  v-for="(thisli,liindex) in allData.container[index].data"  
                  :key="liindex"
                  @click="goPages(thisli)"  
                  class="bacp-v-li rise clearfix pointer">
                    <div class="main">
                      <div class="video-title inner">{{thisli.name}}</div>
                    </div>
                    <div class="left">
                      <img v-if="thisli.type==1" src="../../assets/img/icons/path+路线+课程_图标/课程详情_录播.svg" alt="">
                      <img v-if="thisli.type==2" src="../../assets/img/icons/path+路线+课程_图标/课程详情_回放.svg" alt="">
                      <img v-if="thisli.type==3" src="../../assets/img/icons/path+路线+课程_图标/课程详情_直播.svg" alt="">
                      <img v-if="thisli.type==4" src="../../assets/img/icons/path+路线+课程_图标/pencil-2.svg" alt="">
                    </div>
                    <div class="right">
                      <img v-if="thisli.is_learned" src="../../assets/img/icons/Path.svg" >
                      <span v-if="!thisli.is_learned">{{thisli.duration}}分钟</span>
                      <span v-if="thisli.live_status=='live'" class="font14pr23b8ff" >正在直播</span>
                    </div>
                  </li>
                </ul>
              </div>
            </el-collapse-item>
          </el-collapse>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        activeName:1,
        buttonStyle: {
          background: '#23B8FF',
          padding: '9px 32px',
          'border-radius': '22px',
          background: '#23B8FF'
        },
        allData:{},
        liData:{},
        activeId:-1
      }
    },
    methods: {
   
      collect(){
        this.$post('/tracks/collect/course',{
          course_id:this.$fn.funcUrl('course_id'),
        'custom_user_id':localStorage.uid,
        'is_collect':this.allData.is_collect==0?1:0
        }).then(res=>{
          if(!res.err){
            console.log(this.allData.is_collect)
          this.allData.is_collect=!this.allData.is_collect;
          }
        })
      },
      jj(id) {
        if(!id){return};
        this.activeId=id;
        // if(this.allData.container[id-1].data){return}
        this.$get('/tracks/video/list/info?'+this.orgnizeData(id)).then(res=>{
          this.allData.container[id-1].data=res.data.data;
          console.log(this.allData)
        })
      },
      orgnizeData(id){
        var str='section_id='+this.allData.sections[id-1].id;
        if(localStorage.uid){
          str=str+'&custom_user_id='+localStorage.uid
        }
        return str
      },
      learn(bool){
        debugger
       if(bool){
         var obj={};
         obj.id=this.allData.last_time_learn_id;
         obj.type=this.allData.last_time_learn_type;
         this.goPages(obj)
       } 
       else{
         var obj=this.allData.container[0].data;
         this.goPages(obj)
       }

      },
      goPages(obj){
        switch(obj.type*1){
          case 1:
          case 2: window.location.href='/tracks/video/detail/?course_id='+this.allData.id+'&video_id='+obj.id+'#/note'; break;
          case 3: window.location.href='/tracks/video/detail/?course_id='+this.allData.id+'&video_id='+obj.id+'&type=3'; break;
          case 4: window.location.href='/exercise/list/?course_id='+this.allData.id+'&video_id='+obj.id; break;
          default: break;
        }
      }
    },
    created() {
      console.log(this)
      this.$get('/tracks/course/detail/info?course_id='+this.$fn.getSearchKey('course_id')+'&custom_user_id='+localStorage.uid).then(res => {
        this.hotCourseData=this.$fn.addObjString(this.$myConst.httpUrl,res.data.data,'avatar')
        this.hotCourseData=this.$fn.addObjString(this.$myConst.httpUrl,res.data.data,'course_img')
        //创建容器，容器有状态，通过容器是否为空，发起请求。
        res.data.data.container={};
        for(var i=0;i<res.data.data.sections.length;i++){
          res.data.data.container[i]={data:''}
        }
        this.allData=res.data.data;
        this.jj(1);
        console.log(res)
      })
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
.beforeadd-img-icons{
  margin-right:18px;
  vertical-align: middle;
}
  .ba-header {
    width: 100%;
    height: 216px;
    background: #cccccc;
    background-repeat:no-repeat;
    background-size: cover;

    /* padding-bottom:24px; */
  }

  .ba-header>div {
    margin: 24px;
    margin-bottom: 0px;
  }

  .ba-progressbar:hover {
    .ba-progress-tip {
      top: -27px;
    }
  }

  .ba-progressbar {
    height: 8px;
    width: 100%;
    position: relative;
    .ba-progressbar-inner {
      height: 8px;
      background: #23B8FF;
    }
    .ba-progress-tip {
      position: absolute;
      top: -24px;
      width: 40px;
      height: 20px;
      line-height: 20px;
      margin-left: -20px;
      text-align: center;
      background: #23B8FF;
      box-shadow: 0 0 10px 5px rgba(99, 117, 138, 0.10);
      transition: top ease-out 0.1s;
    }
    .ba-progress-tip-right {
      margin-left: -36px;
    }
    .ba-progress-tip-left {
      margin-left: -4px;
    }
    .bapt-squer {
      width: 0px;
      height: 0px;
      border: 4px solid transparent;
      border-top: 4px solid #23B8FF;
      position: absolute;
      bottom: -8px;
      left: 50%;
      margin-left: -4px;
    }
    .bapt-squer-right {
      left: inherit;
      right: 0%;
      margin-left: -8px;
    }
    .bapt-squer-left {
      left: 0px;
      margin-left: 0px;
    }
  }

  .bah-star {
    vertical-align: middle;
    margin-left: 24px;
    margin-right: -43px;
  }

  .ba-main {
    padding-top: 60px;
  }

  .bam-teachericon {
    height: 64px;
    width: 64px;
    border-radius: 32px;
  }

  .ba-teacherInfo:hover {
    border-right: 1px solid rgba(255, 255, 255, 0);
  }

  .ba-teacherInfo {
    transition: border 0.15s ease;
    width: 320px;
    box-sizing: border-box;
    padding: 24px 35px 32px 24px;
    border-right: 1px solid #E0E0E0;
  }

  .ba-teacherInfo-ul {
    >li {
      margin-bottom: 24px;
    }
    .bamt-uls-title {
      margin-bottom: 8px;
    }
    .content {
      margin-left: 14px;
    }
  }

  .bam-teacherInfo {
    margin-left: 104px;
    height: 64px;
  }

  .ba-progress {
    width: 752px;
  }

  .bap-p {
    margin-bottom: 40px;
  }

  .bap-all {
    .expendedicon,
    .title-tag {
      margin-right: 18px;
    }
  }

  .bapc-videos {
    width: 726px;
    position: relative;
    box-sizing: border-box;
    .bacp-v-li {
      box-sizing: border-box;
      padding: 8px 24px;
      .left,
      .main,
      .right {
        float: left;
      }
      .main {
        width: 100%; // background:red;
      }
      .inner {
        margin-left: 48px; // margin-right:150px;
      }
      .left {
        width: 48px;
        margin-left: -100%; // background:blue;
        img {
        width: 22px;
        height: 18px;
        vertical-align: middle;
      }
      }
      .right {
        width: 150px;
        margin-left: -150px;
        text-align: right; // background:black;
        img {
        width: 10px;
        height: 8px;
        vertical-align: middle;
      }
      }
      
    }
  }
  /* .bapc-videos li{
    margin:5px 24px;
  } */

</style>
