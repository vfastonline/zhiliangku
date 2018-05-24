<template>
  <div class="mainwidth  aq_container">
    <div class="aq-width incenter r">
      <el-button @click="foucus" class="foucusButton">{{foucused}}</el-button>
      <el-button @click="dialogVisible=true" class="quizButton">我要提问</el-button>
      <div class="question-title font1_20_3 3a3c50">{{mainData.title}}</div>
      <div>
        <div class="info r">
          <img class="question-icon  imgmiddle" :src="$myConst.httpUrl+mainData.custom_user_avatar" alt="">
          <span class="qestion-owner-name font1_14_9">{{mainData.custom_user_nickname}}</span>
          <span class="font1_16_9 createTime">{{mainData.create_time}}</span>
          <span class="scan fr font1_14_9">{{mainData.browse_amount}}次浏览</span>
        </div>
        <div v-html="mainData.description"></div>
      </div>
    </div>
    <el-dialog :visible.sync="dialogVisible">
      <submitQuestion id="question_container" :where="'community'" @submitover="over"></submitQuestion>
    </el-dialog>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
  import { Button } from 'element-ui'
  import Vue from 'vue'
  import submitQuestion from '../07_video_detail/07_submit_question'
  Vue.use(Button)
  export default {
    name: 'question_content',
    data() {
      return {
        havefoucesed: false,
        dialogVisible: false,
        where: ''
      }
    },
    props: {
      mainData: Object
    },
    watch: {
      mainData: {
        handler() {
          if (this.mainData.is_follow_user) {
            this.havefoucesed = true;
          }
        },
        deep: true
      }
    },
    computed: {
      foucused: function () {
        return this.havefoucesed ? '已关注该问题' : '关注这个问题'
      }
    },
    methods: {
      over() {
        this.dialogVisible = false;
        window.location.href = '/community/faq/list/'
      },
      foucus() {
        if (this.havefoucesed) {
          this.$fn.showNotice(this, '您已关注该问题')
          return
        }
        var obj = {};
        obj.faq_id = this.$fn.funcUrl('id');
        obj.custom_user_id = localStorage.uid;
        this.$post('/community/follow/faq', obj).then(res => {
          if (!res.data.err) {
            this.$fn.showNotice(this, '您已成功关注该问题', 'success')
            this.havefoucesed = true;
          }

        })
      }
    },
    created() {

    },
    components: {
      submitQuestion: submitQuestion,
    }
  }

</script>

<style>
  #question_container {
    height: inherit;
    padding-top: 0px;
  }

  .incenter {
    margin-left: auto;
    margin-right: auto;
  }
  .aq-width {
    width: 780px;
    position: relative;
    line-height: 42px;
  }

  .el-dialog__body {
    padding-top: 0px;
    padding-bottom: 0px;
  }

  .foucusButton {
    position: absolute;
    left: -150px;
  }

  .foucusButton {
    position: absolute;
    left: -150px;
  }

  .createTime {
    padding-left:20px;
  }

  .qestion-owner-name {
    padding-left:30px;
  }
  .info {
   color: #7c7e8c;
  }

  .aq-width {
    width: 780px;
  }

  .aq_container {
    background: white;
  }

  .quizButton {
    position: absolute;
    right: -123px;
  }

  .question-icon {
    border-radius: 50%;
    height: 60px;
    width: 60px;
  }

</style>
