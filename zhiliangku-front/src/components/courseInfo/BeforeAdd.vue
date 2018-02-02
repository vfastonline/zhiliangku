<template>
  <div class="beforeAdd">
    <div class="blur-background index1" :style="{'background-image':'url(' +allData.course_img +')'}"></div>
    <div class="ba-header index10 relative flexstartcenter">

      <div class="font36plffffff course_title">{{allData.name}}
        <img @click="collect()" v-if="!allData.is_collect" class="bah-star pointer" src="../../assets/img/icons/path+路线+课程_图标/课程详情_收藏_空心.svg"
          alt="">
        <img @click="collect()" v-if="allData.is_collect" class="bah-star pointer" src="../../assets/img/icons/path+路线+课程_图标/课程详情_收藏_实心.svg"
          alt="">
      </div>
      <div class="fontcenter  course_sub_title">
        <div class="font14plffffff bah-tag1">{{allData.is_study_record?'剩余时长':'课程时长'}}</div>
        <div v-if="allData.is_study_record" class="font14plffffff bah-tag2 marginbottom24">
          <span class="font20plffffff ">{{allData.remaining_time}} </span>
        </div>
        <div v-if="!allData.is_study_record" class="font14plffffff bah-tag2 marginbottom24">
          <span class="font20plffffff ">{{allData.total_time}} </span>
        </div>
        <div class="course_continue_learn">
          <el-button class="font20plffffff " :style="buttonStyle" @click="learn(allData.is_study_record)">{{allData.is_study_record?'继续学习':'开始学习'}}</el-button>
        </div>
      </div>
    </div>
    <div v-if="allData.is_study_record" class="ba-progressbar ">
      <div :style="{'width':allData.schedule*100+'%'}" class="ba-progressbar-inner"></div>
      <div class="ba-progress-tip  font12plffffff" :class="{'ba-progress-tip-left':allData.schedule*100<2,'ba-progress-tip-right':allData.schedule*100>98}"
        :style="{'left':allData.schedule*100+'%'}">{{Math.round(allData.schedule*100,0)+'%'}}
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
        <div class="bap-p" v-html="allData.description"></div>
        <div class="bap-all">
          <!-- accordion -->
          <el-collapse @change="jj" v-model="activeName">
            <el-collapse-item v-for="(item,index) in allData.sections" :key="index" :name="index+1">
              <template slot="title">
                <img class="beforeadd-img-icons" v-if="activeName.indexOf( index+1)!=-1" src="../../assets/img/icons/path+路线+课程_图标/课程详情_收起.svg"
                  alt="">
                <img class="beforeadd-img-icons" v-else src="../../assets/img/icons/path+路线+课程_图标/课程详情_展开.svg" alt="">
                <span class="title-tag font14pl5A646E">{{item.title}}</span>
                <span class="title-tag font20pl3a3c50 ">{{item.desc}}</span>
              </template>
              <div class="bap-container clearfix">
                <ul class="incenter floatr bapc-videos">
                  <li v-if="allData.container[index].data" v-for="(thisli,liindex) in allData.container[index].data" :key="liindex" @click="goPages(thisli)"
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
                      <img v-if="thisli.is_learned==1" src="../../assets/img/icons/Path.svg">
                      <span v-if="thisli.is_learned==99">正在学习</span>
                      <span v-if="thisli.type!=3&&thisli.is_learned==0&&thisli.live_status!='live'">{{thisli.duration}}</span>
                      <span v-if="thisli.type==3" class="font14pr23b8ff">{{thisli.live_status_name}}</span>
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
  import func from '../../assets/js/commen/func'
  Vue.prototype.$func = func;
  export default {
    name: 'HelloWorld',
    data() {
      return {
        activeName: [1],
        buttonStyle: {
          background: '#23B8FF',
          padding: '9px 32px',
          'border-radius': '22px',
          background: '#23B8FF'
        },
        allData: {},
        liData: {},
        activeId: -1
      }
    },
    methods: {
      collect() {
        this.$post('/tracks/collect/course', {
          course_id: this.$fn.funcUrl('course_id'),
          'custom_user_id': localStorage.uid,
          'is_collect': this.allData.is_collect == 0 ? 1 : 0
        }).then(res => {
          if (!res.err) {
            console.log(this.allData.is_collect)
            this.allData.is_collect = !this.allData.is_collect;
            this.$notify({
              type: 'info',
              message: res.data.msg,
              offset: 100,
              duration: 2000,
              position: 'bottom-right'
            });
          }
        })
      },
      jj(id) {
        console.log(this.activeName)
        if (!id.length) return;
        var id = id[id.length - 1];
        if (!id) {
          return
        };
        // this.activeId = id;
        if (this.allData.container[id - 1].data) {
          return
        }
        this.$get('/tracks/video/list/info?' + this.orgnizeData(id)).then(res => {
          this.allData.container[id - 1].data = res.data.data;
          console.log(this.allData)
        })
      },
      orgnizeData(id) {
        var str = 'section_id=' + this.allData.sections[id - 1].id;
        if (localStorage.uid) {
          str = str + '&custom_user_id=' + localStorage.uid
        }
        return str
      },
      learn(bool) {
        if (bool) {
          var obj = {};
          obj.id = this.allData.last_time_learn_id;
          obj.type = this.allData.last_time_learn_type;
          obj.vid = this.allData.vid;
          this.goPages(obj)
        } else {
          if (!this.allData.container[0].data[0]) {
            return
          }
          var obj = this.allData.container[0].data[0];
          this.goPages(obj)
        }
      },
      goPages(obj) {
        if (['1','2'].indexOf( obj.type)!=-1) {
          if (!obj.vid) {
            this.showNotice('内容正在制作中，敬请期待')
            return
          }
        }
        if(obj.type==3){
          if(obj.live_status!='live'){
           this.$func.showNotice(this,'直播已经结束')
          }
        }
        this.$func.goCourse(obj.type, this.allData.id, obj.id)
      },
      intercept() {

      },
      showNotice(str) {
        this.$notify({
          type: 'info',
          message: str,
          offset: 100,
          duration: 3000,
          position: 'bottom-right'
        });
      }
    },
    created() {
      console.log(this)
      this.$get('/tracks/course/detail/info?course_id=' + this.$fn.getSearchKey('course_id') + '&custom_user_id=' +
        localStorage.uid).then(res => {
        this.hotCourseData = this.$fn.addObjString(this.$myConst.httpUrl, res.data.data, 'avatar')
        this.hotCourseData = this.$fn.addObjString(this.$myConst.httpUrl, res.data.data, 'course_img')
        //创建容器，容器有状态，通过容器是否为空，发起请求。
        res.data.data.container = {};
        for (var i = 0; i < res.data.data.sections.length; i++) {
          res.data.data.container[i] = {
            data: ''
          }
        }
        this.allData = res.data.data;
        this.allData.sections.forEach((element, ind) => {
          this.jj([ind + 1])
        });
        this.allData.schedule > 1 ? 1 : this.allData.schedule;
        console.log(res)
      })
    },
    mounted() {

    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang='scss'>
  .course_continue_learn {
    .el-button:focus,
    .el-button:hover {
      color: #ffffff;
      border-color: #c6e2ff;
      background-color: #ecf5ff;
    }
  }

  .bap-all {
    .el-collapse-item__header,
    .el-collapse-item__wrap {
      background: #fafafa
    }
    .bapc-videos {
      padding-top: 10px;
    }
  }

</style>

<style lang="scss" scoped>
  .beforeadd-img-icons {
    margin-right: 18px;
    vertical-align: middle;
  }

  .blur-background {
    position: absolute;
    width: 100%;
    height: 240px;
    background-repeat: no-repeat;
    background-size: cover;
    // background-position:center;
    -webkit-filter: blur(3px);
    /* Chrome, Opera */
    -moz-filter: blur(3px);
    -ms-filter: blur(3px);
    filter: blur(3px);
    overflow: hidden;
  }

  .ba-header {
    width: 100%;
    height: 240px;
    background: rgba(0, 0, 0, 0.3);
  }

  .course_sub_title {
    margin: 20px;
    margin-bottom: 0px;
  }

  .course_title {
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
      transition: top ease-out 0.3s;
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
      margin-right: 12px;
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
