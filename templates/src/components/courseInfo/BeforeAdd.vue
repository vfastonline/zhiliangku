<template>
  <div class="beforeAdd">
    <div class="ba-header flexstartcenter">
      <div class="font36plffffff">{{allData.name}}
        <img @click="jj()" class="bah-star" src="../../assets/img/icons/Search-magnifier.svg" alt="">
      </div>
      <div class="fontcenter">
        <div class="font14plffffff bah-tag1">课程时长</div>
        <div class="font14plffffff bah-tag2">
          <span class="font16plffffff">{{allData.remaining_time_hour}} </span>小时
          <span class="font16plffffff">{{allData.remaining_time_minute}} </span>分</div>
      </div>
      <div>
        <el-button class="font20plffffff" :style="buttonStyle">开始学习</el-button>
      </div>
    </div>
    <div class="ba-progressbar">
      <div :style="{'width':'80%'}" class="ba-progressbar-inner"></div>
      <div class="ba-progress-tip  font12plffffff">80%
        <div class="bapt-squer "></div>
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
              <li class="font14pl3a3c50">{{allData.prerequisites}}</li>
            </ul>
          </li>
          <li>
            <ul class="bamt-uls">
              <li class="bamt-uls-title font16pl3a3c50">你将学到什么</li>
              <li>
                <ul>
                  <li v-for="(item,index) in allData.tech" :key="index" class="font14pl3a3c50">
                    <span class="floatl">{{index+1}}、</span>
                    <div class="content">{{item}}</div>
                  </li>
                </ul>
              </li>
            </ul>
          </li>
        </ul>
      </div>
      <div class="floatr ba-progress">
        <p class="bap-p">{{allData.learn}}</p>
        <div class="bap-all">
          <el-collapse accordion>
            <el-collapse-item v-for="(item,index) in allData.sections" :key="index">
              <template slot="title">
                <i @click="jj()" class="header-icon el-icon-info expendedicon"></i>
                <span class="title-tag font14pl5A646E">{{item.desc}}</span>
                <span class="title-tag font20pl3a3c50">{{item.title}}</span>
              </template>
              <div class="bap-container clearfix">
                <ul class="incenter floatr bapc-videos">
                  <li class="bacp-v-li rise clearfix">
                    <div class="main">
                      <div class="video-title inner">课程简介及Linix进程管理作用</div>
                    </div>
                    <div class="left">
                      <img src="../../assets/img/user-icon.jpg" alt="">
                    </div>
                    <div class="right">123</div>
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
        buttonStyle: {
          background: '#23B8FF',
          padding: '9px 32px',
          'border-radius': '22px',
          background: '#23B8FF'
        },
        allData:{}
      }
    },
    methods: {
      jj() {
        console.log(1)
      }
    },
    created() {
      console.log(this)
      this.$ajax.post('/tracks/course/detail', {'course_id': 1}).then(res => {
        this.hotCourseData=this.$fn.addObjString(this.$myConst.httpUrl,res.data.data,'avatar')
        this.allData=res.data.data;
        console.log(res)
      })
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .ba-header {
    width: 100%;
    height: 216px;
    background: #cccccc;
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
      left: 80%;
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
      right: 0px;
      margin-left: 0px;
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
      }
      .right {
        width: 150px;
        margin-left: -150px;
        text-align: right; // background:black;
      }
      img {
        width: 22px;
        height: 18px;
        background: blue;
        vertical-align: middle;
      }
    }
  }
  /* .bapc-videos li{
    margin:5px 24px;
  } */

</style>
