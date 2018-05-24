<template>
  <div>
    <div  class="submit-question  mw hc">
      <div class="font1_20_6 mb16 sqc-title ftj">
        <span class="dib">提问</span>
        <span class="dib cp" @click="$emit('close')">关闭</span>
        <span class="line2"></span>
      </div>
      <div class=" submit-li">
        <div class="floatl submit-label">标题：</div>
        <div class="mb32 ml">
          <el-form>
            <el-form-item>
              <el-input v-model="title" placeholder="请一句话简介明了的说明你的问题"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </div>
      <div class="sqc-tip-container ml submit-li">
        <div class="sqct-usericon floatl">
          <!--<img class="sqct-icon" src="../../assets/img/icons/Search-magnifier.svg" alt="">-->
        </div>
        <div class="sqct-content font14pr424242">
          在你提问之前，不妨先搜索一下你的问题，其他同学可能问到过同样的问题，应该尽量确保你的问题是独一无二的。
        </div>
      </div>
      <div class="mb16 clearfix submit-li">
        <div class="floatl submit-label">问题描述：</div>
        <div class="ml">
          <!-- 注意此处是富文本编辑器 -->
          <quill-editor v-model="content" :options="options" ref="myQuillEditor">
          </quill-editor>
        </div>
      </div>
      <div class="sq-submit">
        <el-button @click="submitQuestion()">提交</el-button>
      </div>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang='scss'>
  .sq-button-container {
    .el-button {
      padding: 4px 8px;
      border-radius: 100px;
      background: #6A747F;
      color: #ffffff;
    }

    .el-button + .el-button {
      margin-left: 10px
    }

    .el-button:focus,
    .el-button:hover {
      color: #fafafa;
      border-color: #c6e2ff;
      background-color: #6A747F;
      opacity: 0.8;
    }
    .active-el-button {
      background: #23B8FF;
      color: #ffffff;
    }
  }

  .submit-li {
    .sq-button-container {
      .active-el-button {
        background: #23B8FF;
        color: #ffffff;
      }
    }
  }

  .el-select {
    width: 100%
  }

  .sq-submit {
    .el-button {
      border-radius: 100px;
    }
  }
</style>

<script>
  import Vue from 'vue'
  import VueQuillEditor from 'vue-quill-editor'
  import 'quill/dist/quill.core.css'
  import 'quill/dist/quill.snow.css'
  import 'quill/dist/quill.bubble.css'
  import {Form, FormItem, Select, Option, Button} from 'element-ui'

  Vue.use(Form)
  Vue.use(FormItem)
  Vue.use(Select)
  Vue.use(Option)
  Vue.use(VueQuillEditor)
  Vue.use(Button)
  export default {
    name: 'HelloWorld',
    data() {
      return {
        // 这个参数是为了防止用户点击过快，造成问题的多次提交。
        switch: true,
        activeButtonIndex: -1,
        title: '',
        content: '',
        reward: 0,
        tags: [],
        options: {
          modules: {}
        },
      }
    },
    props: {
      // where:String
    },
    methods: {
      jj() {
        console.log(11111)
      },
      submitQuestion() {
        if (!this.switch) {
          this.$fn.showNotice(this,'数据正在传输……请稍后哦')
          return
        }
        var obj = {
          title: this.title,
          description: this.content,
          video_id:this.$fn.funcUrl('video_id')
        }
        this.$post('/community/add/faq', obj).then(res => {
          if (!res.data.err) {
            this.$fn.showNotice(this, res.data.msg, 'success');
            this.$emit('submit_success');
          }
          this.switch = false;
        })
      },
      selectDirection(item, index) {
        this.direction = item.id;
        this.activeButtonIndex = index;
      }
    },
    created() {
    },
    mounted() {
    }
  }

</script>

<style scoped>
  .relative {
    position: relative;
  }

  .sqc-title {
    margin-bottom: 34px;
  }

  .submit-li {
    position: relative
  }

  .submit-label {
    white-space: nowrap;
    width: 80px;
    position: absolute;
    top: 50%;
    transform: translate(0, -50%);
    text-align: right;
  }

  .sqc-tip-container {
    margin-bottom: 34px;
    position: relative;
  }

  .sqct-usericon {
    position: absolute;
    top: 50%;
    margin-top: -12px;
  }

  .sqct-icon {
    height: 24px;
    width: 24px;
    vertical-align: middle;
  }

  .ml {
    margin-left: 94px;
  }

  .sq-button-container {
    margin-left: 85px;
  }

  .first-button {
    margin-left: 10px;
  }

  .sqct-content {
    opacity: 0.5;
    margin-left: 30px;
  }

  .submit-question {
    background: white;
    width: 649px;
    box-sizing: border-box;
    padding: 16px 40px 24px 40px;
  }

  .sq-submit {
    text-align: right;
  }

  .mb32 {
    margin-bottom: 32px;
  }

  .mb16 {
    margin-bottom: 16px;
  }

</style>
