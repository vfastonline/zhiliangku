<template>
  <div class="submit-question-container">
    <div class="submit-question incenter">
      <div class="font20pl3a3c50 mb16 sqc-title">提问</div>
      <div class=" submit-li">
        <div class="floatl submit-label">标题：</div>
        <div class="mb32 ml">
          <el-form :model="title">
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
          <quill-editor  v-model="content" :options="options" ref="myQuillEditor">
          </quill-editor>
        </div>
      </div>
      <div class="relative mb16 submit-li">
        <div class="floatl submit-label">问题方向：</div>
        <div class="sq-button-container">
          <el-button v-for="(item,index) in tags" :key="index" :class="{'first-button':index==0,'active-el-button':activeButtonIndex==index}" @click="selectDirection(item,index)">{{item.name}}</el-button>
        </div>
      </div>
      <div class=" submit-li">
        <div class="floatl submit-label">悬赏：</div>
        <div class="mb32 ml">
          <el-select v-model="reward" placeholder="活动区域">
            <el-option v-for="(item,index) in arr" :key="index" :label="item.label" :value="item.value"></el-option>
          </el-select>
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
      padding:4px 8px;
      border-radius: 100px;
      background: #6A747F;
      color: #ffffff;
    }

    .el-button+.el-button {
      margin-left: 10px
    }

    .el-button:focus,
    .el-button:hover {
      color: #fafafa;
      border-color: #c6e2ff;
      background-color: #6A747F ;
      opacity: 0.8;
    }
    .active-el-button{
      background: #23B8FF ;
      color: #ffffff;
    }
  }
  .submit-li{
    .sq-button-container{
      .active-el-button{
        background: #23B8FF ;
        color: #ffffff;
      }
    }
  }
  .el-select{
    width:100%
  }
  .sq-submit{
    .el-button{
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
  import {Form,FormItem} from 'element-ui'
  Vue.use(Form)
  Vue.use(FormItem)
  Vue.use(VueQuillEditor)
  export default {
    name: 'HelloWorld',
    data() {
      return {
        // 这个参数是为了防止用户点击过快，造成问题的多次提交。
        disable:false,
        activeButtonIndex:-1,
        title: '',
        content: '',
        direction: '',
        reward: 0,
        tags: [],
        arr: [{
          label: '不悬赏',
          value: 0
        }, {
          label: '1积分',
          value: 1
        }, {
          label: '2积分',
          value: 2
        }, {
          label: '3积分',
          value: 3
        }, {
          label: '4积分',
          value: 4
        }, {
          label: '5积分',
          value: 5
        }],
        options: {
          modules: {
            toolbar: ['bold', 'italic', 'underline',
              // 'image',
              'link', {
                'list': 'bullet'
              }, {
                'list': 'ordered'
              }, 'blockquote'
            ]
          }
        },
      }
    },
    props:{
      where:String
    },
    methods: {
      jj(){
        console.log(11111)
      },
      submitQuestion() {
        if(this.disable){
          // this.$fn.showNotice(this,'数据正在传输……请稍后哦')
          return
        }
        this.disable=true;
        var obj={
          custom_user_id: localStorage.uid,
          title: this.title,
          description: this.content,
          path: this.direction,
          reward: this.reward
        };
        if(this.$fn.funcUrl('video_id')){
          obj.video_id=this.$fn.funcUrl('video_id')
        }
        this.$post('/community/add/faq',obj ).then(res => {
          if (!res.data.err) {
            this.$fn.showNotice(this,res.data.msg,'success');
            if(this.where=='community'){
              this.$emit('submitover');
              return
            }
            this.$router.push({
              path: '/question'
            })
            return
          }
          this.disable=false;
        })
      },
      selectDirection(item,index) {
        this.direction = item.id;
        this.activeButtonIndex=index;
      }
    },
    created() {
      this.$get('/tracks/question/path/info').then(res => {
        this.tags = res.data.data
      })
    },
    mounted() {}
  }

</script>

<style scoped>
  .relative {
    position: relative;
  }

  .submit-question-container {
    background: #fafafa;
    padding-top: 40px;
    height: 700px;
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
