<template>
  <div class="anwser-container hc r">
    <div class="anwser_content mw">
      <div class="anwser_info_left fl ftc">
        <img class="question-user-icon imgmiddle" :src="$myConst.httpUrl+mainData.custom_user_avatar" alt="">
        <div class="adopt r ftc">
          <img class="a state_icon" v-if="showAreadyAdopt" src="./img/01_adopt.png" alt="">
          <img class="a state_icon" v-if="showAdopt" src="./img/02_default.png" alt="">
          <span class="state r font1_16_f" v-if="mainData.optimal">已采纳</span>
          <span class="state r font1_16_f" v-else>采纳</span>
        </div>
      </div>
      <div class="anwser_info_right">
        <div class="r userinfo">
          <span class="font1_16_9">{{mainData.custom_user_nickname}}</span>
          <span class="font1_16_9 createTime fr">{{mainData.create_time}}</span>
        </div>
        <div class="answerType font1_16_b4" v-if="mainData.is_self">答主</div>
        <div class="answerContent font1_18_9" v-html="mainData.answer">
        </div>
        <div class="toolbar">
          <div>
            <div class="fl praise ftc cp " :class="{'yes':mainData.feedback==='approve',empty:!mainData.feedback}">
              <i @click="support ('approve')"  class="iconfont  icon-zan   praise_block_icon"></i>
              <span class="question-yes dib vm">{{mainData.approve}}</span>
            </div>
            <div class="fl praise ftc cp" :class="{'no':mainData.feedback==='oppose',empty:!mainData.feedback}">
              <i @click="support ('oppose')"  class="iconfont  icon-cai  cp praise_block_icon"></i>
              <span class="question-yes dib vm">{{mainData.oppose}}</span>
            </div>
          </div>
          <div>
            <!--<tag_0 v-if="answer_edit" @click="showTextarea=!showTextarea"><span>编辑</span></tag_0>-->
            <!--<tag_0 v-if="answer_edit" @click="showTextarea=!showTextarea"><span>删除</span></tag_0>-->
            <span class="cp replayButton" @click="showReply()">
              <span class="font1_18_f">评论 {{mainData.answer_reply_list.length||0}}</span>
              <i class="iconfont icon-zhankai" :class="{'spread':showr}"></i>
            </span>
          </div>
        </div>
      </div>
    </div>
    <transition
      enter-active-class="animated fadeInUp"
      leave-active-class="animated fadeOutDown">
      <div ref="reply" v-show="showr" class="reply_box">
        <reply class="animated fadeIn"
               v-for="(item,index) in mainData.answer_reply_list" :key="index"
               :mainData="item"></reply>
        <replyMsg :mainData="mainData"></replyMsg>
      </div>
    </transition>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .adopt{
    height: 53px;
    width: 50px;
    margin:5px;
    line-height: 32px;
  }
  .state_icon{
    top: 0;
    left: 0;
    z-index: 1;
  }
  .state{
    z-index: 10;
  }
</style>
<script>
  import Bus from '../../assets/js/02_bus'
  import reply from './06_reply'
  import replyMsg from './07_reply_msg'
  import tag_0 from '../11_personal_center/08_tag_0'
  // import fixedButton from '../08_community/05_fixed_button.vue'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        showr: false,
        showTextarea: false,
        showAreadyAdopt: false,
        showAdopt: false,
        answer_edit: false
      }
    },
    props: {
      mainData: Object,
      questionId: Number
    },
    computed: {
      state: function () {
        if (this.mainData.feedback == '' || this.mainData.feedback == 'oppose') {
          return true
        } else return false
      },
      state1: function () {
        if (this.mainData.feedback == '' || this.mainData.feedback == 'approve') {
          return true
        } else return false
      },
    },
    methods: {
      notice() {
        this.$fn.showNotice(this, '禁止重复操作哟~')
      },
      adoptAnwser() {
        var obj = {
          faq_id: this.questionId,
          custom_user_id: localStorage.uid,
          faq_answer_id: this.mainData.id
        };
        this.$post('/community/accept/faqanswer', obj).then(res => {
          if (!res.data.err) {
            this.showAreadyAdopt = true
            this.$fn.showNotice(this, res.data.msg, 'success')
            Bus.$emit('replyover')
          }
        })
      },
      support(str) {
        if (this.mainData.feedback) {
          this.notice()
          return
        }
        var obj = {}
        obj.faq_answer_id = this.mainData.id
        obj.appraisal = str
        obj.custom_user_id = localStorage.uid
        this.$post('/community/appraisal/faqanswer', obj).then(res => {
          // console.log(res)
          if (!res.data.err) {
            this.mainData.feedback = str
            if (str == 'approve') {
              this.mainData.approve++
            }
            if (str == 'oppose') {
              this.mainData.oppose++
            }
          }
        })
      },
      showReply() {
        this.showr = !this.showr
        this.showTextarea = !this.showTextarea
      },
    },
    created() {
      console.log(this.mainData)
      if (this.mainData.custom_user_id == localStorage.uid) {
        this.answer_edit = true
        if (this.mainData.optimal == true) {
          this.showAreadyAdopt = true
        }
        else {
          this.showAdopt = true
        }
      }
    },
    components: {
      reply: reply,
      replyMsg: replyMsg,
      tag_0: tag_0
      // fixedButton: fixedButton
    }
  }

</script>
<style scoped lang="scss">
  .praise_block_icon{
    color: #666;
    font-size: 30px;
  }
  .anwser_content {
    background-color: #fff;
    padding: 30px 120px 30px 20px;
  }
  .praise_block_icon{

  }
  .answerContent {
    padding: 8px;
    min-height: 50px;
  }

  .userinfo {
    margin-bottom: 10px;
  }

  .createTime {
    padding-right: 30px;
  }

  .icon-zhankai {
    display: inline-block;
    transition: all ease 0.5s;
  }

  .toolbar {
    display: flex;
    justify-content: space-between;
    /*border-bottom: 1px solid rgba(0, 0, 0, 0.09);*/
  }

  .praise {
    width: 120px;
    height: 40px;
    border-radius: 8px;
    line-height: 40px;
  }

  .empty:hover {
    background-color: #00bcd5;
    span{
      color: white;
    }
    .iconfont{
      color: white;
    }
  }
  .yes,.no{
    background-color: #00bcd5;
    span{
      color: white;
    }
    .iconfont{
      color: white;
    }
  }

  .anwser-container {
    margin: 32PX 0;
    border-radius: 10px;
    transition: all ease 0.2s;
  }

  .anwser_info_left {
  }

  .anwser_info_right {
    margin-left: 76px;
    padding: 27px 32px 32px 0;
  }

  .question-user-icon {
    width: 60px;
    height: 60px;
    border-radius: 50%;
  }

  .question-yes {
    margin-left: 14px;
    font-size: 18px;
    font-family: "MicroSoft YaHei", "PingFangSC-Light";
  }

  .reply_box {
    padding-top: 20px;
    background-color: #fafafa;
  }

  .replayButton {
    display: inline-block;
    width: 120px;
    height: 40px;
    line-height: 40px;
    background-color: #00bcd5;
    text-align: center;
    color: #fff;
    border-radius: 8px;
  }

  .adopt_view {
    width: 50px;
    height: 50px;
    background-color: red;
    margin-top: 5px;
    margin: 5px auto 0px;
  }

  .adopt_view2 {
    width: 50px;
    height: 50px;
    background-color: #ccc;
    margin-top: 5px;
    margin: 5px auto 0px;
  }

</style>
