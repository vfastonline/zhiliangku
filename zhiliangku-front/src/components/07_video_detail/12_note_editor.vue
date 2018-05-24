<template>
    <div class="submit-question  mw hc rose">
      <div class="font1_20_3 mb16 sqc-title ftj">
        <span class="dib">学习笔记</span>
        <span class="dib cp" @click="close()">关闭</span>
        <span class="line2"></span>
      </div>
      <div class=" submit-li">
        <div class="floatl submit-label">标题：</div>
        <div class="mb32 ml">
          <el-form>
            <el-form-item>
              <el-input v-model="title" placeholder="笔记标题"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </div>
      <div class="mb16 clearfix submit-li">
        <div class="fl submit-label">问题描述：</div>
        <div class="ml">
          <!-- 注意此处是富文本编辑器 -->
          <quill-editor v-model="content" :options="options" ref="myQuillEditor">
          </quill-editor>
        </div>
      </div>
      <div class="sq-submit">
        <el-button @click="submit_note()">提交</el-button>
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
  import {Form, FormItem, Select, Option, Button} from 'element-ui'

  Vue.use(Form)
  Vue.use(FormItem)
  Vue.use(Select)
  Vue.use(Option)
  Vue.use(window.VueQuillEditor)
  Vue.use(Button)
  export default {
    name: 'note_editor',
    data() {
      return {
        // 这个参数是为了防止用户点击过快，造成问题的多次提交。
        disable: false,
        activeButtonIndex: -1,
        title: '',
        content: '',
        direction: '',
        reward: 0,
        tags: [],
        options: {
          modules: {}
        },
      }
    },
    props: {
    },
    methods: {
      close(){
        this.$emit('close')
      },
      submit_note() {
        if (this.disable) {
          this.$fn.showNotice(this, '数据正在传输……请稍后哦')
          return
        }
        this.disable = true;
        var obj = {
          title: this.title,
          notes: this.content,
        };
        if (this.$fn.funcUrl('video_id')) {
          obj.video_id = this.$fn.funcUrl('video_id')
        } else {
          this.$fn.showNotice(this, 'url错误', 'error')
        }
        this.$post('/tracks/student/add/notes/info', obj).then(res => {
          if (!res.data.err) {
            this.$fn.showNotice(this, res.data.msg, 'success');
            this.close();
            this.$emit('up_data')
          }
          this.disable = false;
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
  .submit-question-container {
    background: #fafafa;
    padding-top: 40px;
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

  .ml {
    margin-left: 94px;
  }

  .submit-question {
    background: white;
    width: 649px;
    box-sizing: border-box;
    padding: 16px 40px 24px 40px;
    border:1px solid #ccc;
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
