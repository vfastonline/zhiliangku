<template>
  <div class="mw hc test rose">
    <div class="text_name font1_28_f"></div>
    <div class="test_container hc">
      <div class="list" v-html="content.topic">
      </div>
      <div>
        <iframe :src="src" onload="" frameborder="0" width="1000px" height="400" scrolling='no'
                hspace="0"
                vspace="0"></iframe>
      </div>
      <div class="submit_container">
        <el-button class="submit_buttton" type="primary" @click="submit()" size="medium">提交答案</el-button>
      </div>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
  .list {
    p {
      line-height: 30px;
      height: 30px;
      font-size: 20px;
    }
    margin-bottom: 32px;
  }
</style>
<style scoped lang='scss'>
  .text_name {
    height: 60px;
    line-height: 60px;
    padding-left: 80px;
    overflow: hidden;
    border-radius: 10px 10px 0 0;
    background-color: #324e5c;
    margin-bottom: 60px;
  }

  .test {
    margin-top: 98px;
    border-radius: 10px 10px 0 0;
  }

  .submit_container {
    text-align: right;
  }

  .submit_buttton {
    margin:25px 100px 80px 0; 
  }

  .test_container {
    padding-left:100px;
    line-height:30px;
    font-size:20px;
    color:#666;
  }


</style>
<script>
  import Vue from 'vue'
  import {Button} from 'element-ui'

  Vue.use(Button)
  export default {
    name: 'HelloWorld',
    data() {
      return {
        src: '',
        content: {
          topic: ''
        },
        vid: ''
      }
    },
    props: {},
    methods: {
      get_data() {
        this.vid = this.$fn.funcUrl('video_id')
        if (!this.vid) {
          this.$fn.showNotice(this, '地址栏video_id错误')
          return
        }
        this.$get('/assess/construct?video_id=' + this.vid).then(res => {
          let data = res.data.data
          this.content = data
          this.src = 'http://' + data.docker
        })
      },
      submit() {
        window.open("/assess/result/info/?video_id=" + this.vid)
      }
    },
    created() {
      this.get_data()
    }
  }

</script>
