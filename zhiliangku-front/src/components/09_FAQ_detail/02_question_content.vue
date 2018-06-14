<template>
  <div >
    <div class="mw aq-width incenter r">
      <!--<el-button @click="foucus" class="foucusButton">{{foucused}}</el-button> -->
      <!--<el-button @click="dialogVisible=true" class="quizButton">我要提问</el-button> -->
      <fixedButton class="fixedButton" @click.native="dialogVisible=true" text="我要回答">
        <!-- <img src="" alt="" style="background-color:red"> -->
        <span class="dib ftc a_icon">A</span>
      </fixedButton>
      <div>
        <div class="info r clearfix">
          <div class="info_left fl ftc">
            <img class="question-icon" v-if="mainData.custom_user_avatar"
                 :src="$myConst.httpUrl+mainData.custom_user_avatar" alt="">
          </div>
          <div class="info_right">
            <span class="qestion-owner-name font1_16_9">{{mainData.custom_user_nickname}}</span>
            <span class="font1_16_9 createTime">{{mainData.create_time}} 提问</span>
            <div class="clearfix">
              <div class="question-title font1_18_6 fl">{{mainData.title}}</div>
              <div class="fr">
                <span class="info_right_one scan fr font1_14_6">{{mainData.browse_amount}}次浏览</span>
                <span class="info_right_two scan fr font1_14_6">{{dataLength()}}次回答</span>
              </div>
            </div>
            <div class="info_status">
              <div class="font1_14_b4 dib">{{mainData.status_name|| "未解决"}}</div>
              <!--关注-->
              <div class="dib heart">❤</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <el-dialog :visible.sync="dialogVisible"
               width="850px">
      <span class="dib font1_18_6 dialog_title" slot="title">我来回答</span>
      <!--<submitQuestion id="question_container" :where="'community'" @submitover="over"></submitQuestion>-->
      <richtext class="richtext hc"></richtext>
    </el-dialog>
  </div>
</template>
<style >
  .dialog_title{
    margin: 20px 0 0 20px;
  }
</style>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
  import Bus from '../../assets/js/02_bus'
  import {Button} from 'element-ui'
  import Vue from 'vue'
  import submitQuestion from '../07_video_detail/07_submit_question'
  import fixedButton from '../08_community/05_fixed_button.vue'
  import richtext from './05_vue_qill_editor'

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
      dataLength() {
        if (!this.mainData || !this.mainData.faq_answer_list) {
          return 0
        }
        return this.mainData.faq_answer_list.length;
      },
      over() {
        this.dialogVisible = false;
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
      Bus.$on('replyover', () => {
        this.dialogVisible = false;
      })
    },
    components: {
      submitQuestion: submitQuestion,
      fixedButton: fixedButton,
      richtext: richtext
    }
  }

</script>

<style scoped>
  .a_icon{
    background: white;
    height: 32px;
    width: 32px;
    line-height: 32px;
    font-size: 20px;
    color: #8c97cb;
    border-radius: 100px;
  }
  #question_container {
    height: inherit;
    padding-top: 0px;
  }

  .incenter {
    margin-left: auto;
    margin-right: auto;
  }

  .aq-width {
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

  .info {
    color: #7c7e8c;
  }

  .info_left {
    width: 120px;
    height: 80px;
    padding-top: 22px;
  }

  .info_right {
    margin-left: 120px;
  }

  .info_right_one {
    padding-right: 40px;
  }

  .info_right_two {
    padding-right: 15px;
  }

  .createTime {
    padding-left: 20px;
  }

  .aq_container {
    background: #fafafa;
  }

  .quizButton {
    position: absolute;
    right: -123px;
  }

  .question-icon {
    border-radius: 50%;
    height: 80px;
    width: 80px;
  }

  .fixedButton {
    position: fixed;
    top: 90px;
    left: 50%;
    margin-left: 600px;
  }

  .info_status {
    margin-top: -17px;
  }

  .heart {
    width: 32px;
    height: 24px;
    padding-left: 20px;
    font-size: 24px;
    color: coral;
  }
</style>
