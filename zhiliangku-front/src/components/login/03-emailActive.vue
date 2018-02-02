<template>
  <div class="email-active relative" :style="{'height':height+'px'}">
    <div class="inmiddle msg-container">
      <div v-if="show" class="fontcenter active-msg">
        <img class="imgmiddle active-right" src="../../assets/img/icons/login/大对勾.svg" alt="">
        <span class="font20pr23b8ff">恭喜，邮箱已激活成功！</span>
      </div>
      <div v-if="show" class="fontcenter gohome-button">
        <el-button @click="gohome">
          返回首页（{{time}}s）
        </el-button>
      </div>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang='scss'>
  .gohome-button {
    .el-button {
      background: #23b8ff;
      color: #ffffff;
      padding: 16px 32px;
      font-size: 20px;
      border-radius: 100px;
      span {
        font-family: 'PingFangSC-Light', 'Microsoft YaHei';
      }
    }

    .el-button+.el-button {
      margin-left: 10px
    }

    .el-button:focus,
    .el-button:hover {
      color: #409EFF;
      background: #ffffff;
    }

    .el-button:active {
      color: #3a8ee6;
      border-color: #3a8ee6;
      outline: 0
    }
  }

</style>

<style scoped>
  .email-active {
    height: 100%
  }

  .active-msg {
    margin-bottom: 60px;
  }

  .msg-container {
    width: 100%;
    height: 200px;
  }

  .active-right {
    margin-right: 48px;
  }

</style>
<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        height: '',
        time: 5,
        timer: '',
        show: false,
        hash:''
      }
    },
    watch: {
      show(newvalue, oldvalue) {
        if (newvalue) {
          this.timer = setInterval(this.countTime, 1000)
        }
      }
    },
    props: {

    },
    methods: {
      gohome() {
        window.location.href = '/'
      },
      countTime() {
        this.time = this.time - 1;
        if (this.time == 0) {
          this.gohome()
        }
      }
    },
    created() {
      this.height = window.innerHeight - 70;
      this.hash=this.$fn.funcUrl('hash');
      if(this.hash){
        this.$get('/customuser/activation?hash='+this.hash).then(res=>{
          if(!res.data.err){
            this.show=true;
          }
        })
        }
    },
    components: {

    }
  }

</script>
