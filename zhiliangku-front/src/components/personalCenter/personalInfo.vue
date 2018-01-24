<template>
  <div class="personal-info-outer zindex1" :style="{'background-image':'url(' +imgData.pathwel +')'}">
    <div class="mainwidth incenter">
      <div class="pio-detail">
        <div class="pio-user-left">
          <el-upload class="avatar-uploader" action="https://jsonplaceholder.typicode.com/posts/" :show-file-list="false" :on-success="handleAvatarSuccess"
            :before-upload="beforeAvatarUpload">
            <img class="pio-user-img" v-if="imgsrc" :src="imgsrc" alt="" />
          </el-upload>
        </div>
        <div class="pio-user-right">
          <div class="pio-username font20plffffff">{{nickname}}</div>
          <div class="pio-studytime font14prffffff">
            学习时长：{{Math.floor( mainData.learn_time/60)}}小时{{mainData.learn_time%60}}分钟 | 积分：{{mainData.integral}}分</div>
          <div class="pio-words font14prffffff">{{mainData.signature}}</div>
        </div>
      </div>
    </div>

  </div>
</template>
<script>
  import Bus from '../../assets/js/bus'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        imgsrc: '',
        nickname: '',
        mainData: {},
        imgData: {
          pathwel: ''
        }
      }
    },
    methods: {
      handleAvatarSuccess(res, file) {
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
      getData() {
        this.$get('/personal_center/basic/info?custom_user_id=' + localStorage.uid).then(res => {
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
    .el-upload {
      border-radius: 100px;
    }
  }

</style>

<style scoped>
  .personal-info-outer {
    width: 100%;
    height: 400px;
    background: rgba(35, 184, 255, 0.60);
    box-sizing: border-box;
    padding-top: 143px;
    background-repeat: no-repeat;
    background-size: cover;
  }

  .pio-detail {
    width: 100%;
    height: 196px;
  }

  .pio-detail .pio-user-left {
    width: 196px;
    height: 196px;
    margin-left: 12px;
    float: left;
  }

  .pio-detail .pio-user-left .pio-user-img {
    border-radius: 50%;
    width: 196px;
    height: 196px;
  }

  .pio-detail .pio-user-right {
    margin-left: 276px;
    box-sizing: border-box;
    padding-top: 25px;
    position: relative;
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
    margin-top: 51px;
    opacity: 0.5;
  }

  .pio-detail .pio-user-right .pio-exit {
    position: absolute;
    left: 523px;
    top: 136px;
    opacity: 0.5;
  }

</style>
