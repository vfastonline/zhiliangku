<template>
  <div class="mw hc test rose">
    <div class="text_name font1_28_f"></div>
    <div class="test_container hc">
      <div class="list" v-html="content.topic">
      </div>
      <div>
        <iframe :src="src" onload="" frameborder="0" width="1088px" height="400" scrolling='no'
                hspace="0"
                vspace="0"></iframe>
      </div>
      <div class="submit_container">
        <el-button type="primary" @click="submit()" size="medium">提交答案</el-button>
      </div>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
  .list {
    p {
      line-height: 48px;
      height: 48px;
      font-size: 32px;
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

  .test_container {
    margin-top: 32px;
    border-radius: 10px;
    padding: 24px
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
        }
      }
    },
    props: {},
    methods: {
      get_data() {
        let vid = this.$fn.funcUrl('video_id')
        if (!vid) {
          this.$fn.showNotice(this, '地址栏video_id错误')
          return
        }
        this.$get('/assess/construct?video_id=' + vid).then(res => {
          let data = res.data.data
          this.content = data
          this.src = 'http://' + data.docker
        })
      }
    },
    created() {
      this.get_data()
    }
  }

</script>
