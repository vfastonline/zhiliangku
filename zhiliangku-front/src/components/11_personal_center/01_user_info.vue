<template>
  <div class="personal-info-outer zindex1" :style="{'background-image':'url(' +imgData.pathwel +')'}">
    <div class="pio-detail  mw ">
      <div class="pio-user-left r">
        <el-upload class="avatar-uploader" :action="ognizeUrl()" :show-file-list="false"
                   :on-success="handleAvatarSuccess"
                   :before-upload="beforeAvatarUpload">
          <img class="pio-user-img" v-if="imgsrc" :src=" imgsrc" alt=""/>
          <div class="camera ftc a cp">
            <img class="camera_icon" src="./img/01_camera_icon.png" alt="">
          </div>
        </el-upload>
      </div>
      <div class="pio-user-right">
        <div class="pio-username font1_20_f">{{nickname}}</div>
        <div class="pio-words font1_20_f">{{mainData.signature}}</div>
      </div>
    </div>
  </div>
</template>
<script>
  import Vue from 'vue'
  import {Upload} from 'element-ui'
  import Bus from '../../assets/js/02_bus'

  Vue.use(Upload)
  export default {
    name: 'HelloWorld',
    data() {
      return {
        imgsrc: '',
        nickname: '',
        mainData: {},
        imgData: {
          pathwel: ''
        },
        actionUrl: ''
      }
    },
    methods: {
      handleAvatarSuccess(res, file) {
        localStorage.avatar = res.avatar;
        Bus.$emit('refreshAvatar')
        this.imgsrc = URL.createObjectURL(file.raw);
      },
      beforeAvatarUpload(file) {
        const isJPG = file.type === 'image/jpeg';
        const isLt2M = file.size / 1024 / 1024 < 2;
        if (!isJPG) {
          this.$message.error('上传头像图片只能是 JPG 格式!');
        }
        if (!isLt2M) {
          this.$message.error('上传头像图片大小不能超过 2MB!');
        }
        return isJPG && isLt2M;
      },
      ognizeUrl() {
        var str = this.$myConst.httpUrl + '/customuser/change/avatar?custom_user_id=' + localStorage.uid + '&avatar_type=custom_user_avatar';
        return str
      },
      getData() {
        this.$get('/personal_center/basic/info' ).then(res => {
          this.mainData = res.data.data;
          for (var k in res.data.data) {
            localStorage[k] = res.data.data[k]
          }
          this.initTags()
          Bus.$emit('havePersonalData', res.data.data)
        })
      },
      getimage() {
        this.$get('/slides/list?category=3').then(res => {
          this.$fn.addString(this.$myConst.httpUrl, res.data.data, 'pathwel')
          this.imgData.pathwel = res.data.data[0].pathwel;
        })
      },
      initTags() {
        this.nickname = localStorage.nickname;
        this.imgsrc = this.$myConst.httpUrl + localStorage.avatar;
      }
    },
    created() {
      this.getData();
      this.getimage();
      Bus.$on('refreshPersonalData', () => {
        this.getData()
      })
      Bus.$on('requirePersonalData', () => {
        Bus.$emit('havePersonalData', this.mainData)
      })
    }
  }
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang='scss'>
  .pio-user-left {
    border-radius: 100px;
    overflow: hidden;
  }

</style>

<style scoped>
  .camera{
    height: 0px;
    transition: height 0.6s;
    background-color: rgba(0,0,0,.5);
    bottom: 0px;
    width: 120px;
  }
  .camera_icon{
    margin-top:7px;
  }
  .pio-user-left:hover .camera{
    height: 37px;
  }
  .personal-info-outer {
    width: 100%;
    height: 300px;
    background: rgba(35, 184, 255, 0.60);
    box-sizing: border-box;
    background-repeat: no-repeat;
    background-size: cover;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .pio-detail {
    display: flex;
    justify-content: left;
    align-items: center;
    height: 100%;
  }

  .pio-detail .pio-user-left {
    width: 120px;
    height: 120px;
    margin-left: 12px;
    float: left;
  }

  .pio-detail .pio-user-left .pio-user-img {
    border-radius: 50%;
    width: 120px;
    height: 120px;
  }

  .pio-detail .pio-user-right {
    margin-left: 20px;
    box-sizing: border-box;
    max-width: 400px;
    position: relative;
  }

  .pio-user-right {
    padding-top: 50px;
  }

  .pio-detail .pio-user-right .pio-username {
    height: 28px;
    line-height: 28px;
  }

  .pio-detail .pio-user-right .pio-studytime {
    height: 20px;
    line-height: 20px;
    margin-top: 20px;
    opacity: 0.5;
  }

  .pio-detail .pio-user-right .pio-words {
    height: 20px;
    line-height: 20px;
    margin-top: 23px;
    opacity: 0.5;
  }

  .pio-words {
    width: 600px;
  }

  .pio-detail .pio-user-right .pio-exit {
    position: absolute;
    left: 523px;
    top: 136px;
    opacity: 0.5;
  }

</style>
