<template>
  <div class="lvs-container">
    <!-- <div class="mainwidth incenter block logo">
      <img class="block incenter" src="../../assets/img/icons/Logo.png" alt="">
    </div> -->
    <div class="lvs-content clearfix incenter mainwidth">
      <div :style="{'background-image':'url('+imgUrl+')'}" class="lvsc-video relative floatl">
        <!-- <img :src="" alt=""> -->
        <el-button v-if="showButton" class="lvsc-enterButton" :style="myButtonStyle" @click="go()">进入直播间</el-button>
      </div>
      <div class="lvsc-list floatl">
        <el-scrollbar class="lvsc-list-container">
          <ul>
            <li v-for="item in liveData" @click="changeImg(item)" :key="item.id" class="lvsc-info textellipsis">
              <span v-if="item.status=='end'" class="lvsc-tag font16pmCCCCCC">{{item['start_time']}}</span>
              <span v-if="item.status=='live'" class="lvsc-tag lvsc-live">直播中</span>
              <span class="lvsc-content font16pr07111B pointer">{{item.name}}</span>
            </li>
          </ul>
        </el-scrollbar>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "HelloWorld",
    data() {
      return {
        showButton: '',
        liveData: [],
        imgUrl: '',
        myButtonStyle: {
          'color': "#ffffff",
          'height': '44px',
          'width': '164px',
          'border-radius': '22px',
          'background-color': '#23B8FF'
        },
        video_id: '',
        course_id: ''
      };
    },
    methods: {
      changeImg(item) {
        if (item.status == 'live') {
          this.showButton = true;
        } else {
          this.showButton = false;
        }
        this.imgUrl = item.pathwel
        this.video_id = item['video_id'];
        this.course_id = item['course_id'];
      },
      go() {
        window.location.href = '/tracks/live/detail/?course_id=' + this.course_id + '&video_id=' + this.video_id
      },
      getData() {
        this.$get('/lives/index/list').then(res => {
          this.liveData = this.$fn.addString(this.$myConst.httpUrl, res.data.data, 'pathwel')
          this.initi()
        })
      },
      initi() {
        this.imgUrl = this.liveData[0]['pathwel'];
        this.video_id = this.liveData[0]['video_id'];
        this.course_id = this.liveData[0]['course_id'];
        this.showButton = false || (this.liveData[0].status == 'live')
      }
    },
    created() {
      this.getData()
    },
    mounted() {}
  }

  ;

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
  .logo {
    height: 88px;
    margin-top: 60px;
    margin-bottom: 60px;
  }

  .lvs-container {
    height: 440px;
    width: 100%;
    position: relative;
    padding-bottom: 32px;
  }

  .lvsc-info:hover {
    .lvsc-tag,
    .lvsc-content {
      color: #23B8FF
    }
    background:#F5F6F7;
  }

  .lvsc-info {
    height: 56px;
    line-height: 56px;
    padding-left: 32px;
    font-size: 16px;
    .lvsc-tag {
      display: inline-block;
      width: 48px;
      padding-right: 17px;
    }
    .lvsc-live {
      color: #23B8FF
    }
    .lvsc-content {
      width: 310px;
    }
  }

  .lvsc-list-container {
    width: 440px;
    height: 440px;
    .el-scrollbar__wrap {
      overflow-y: scroll;
      overflow-x: hidden;
    }
  }

  .lvsc-video {
    background: no-repeat;
    background-size: cover;
    background-position: center;
    height: 440px;
    width: 712px;
    img {
      height: 440px;
      width: 712px;
    } // background: skyblue;
    box-sizing: border-box;
  }

  .lvsc-enterButton {
    position: absolute;
    bottom: 62px;
    left: 273px;
  }

  .lvsc-list {
    width: 440px;
    height: 440px;
    box-sizing: border-box; // background: pink;
  }

</style>
