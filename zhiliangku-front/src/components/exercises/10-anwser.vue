<template>
  <div class="anwser-container incenter relative">
    <div v-if="mainData.optimal" class="bestAnwser fontcenter">
      <span class="bestAnwserContent font16prffffff ">最佳答案</span>
    </div>
    <div class="relative userinfo">
      <img class="question-user-icon imgmiddle" :src="$myConst.httpUrl+mainData.custom_user_avatar" alt="">
      <span class="font14pl7c7e8c">{{mainData.custom_user_nickname}}</span>
      <span class="font14pl7c7e8c scan">{{mainData.create_time}}</span>
    </div>
    <div class="answerContent" v-html="mainData.answer">
    </div>
    <div class="toolbar">
      <div>
        <div class="floatl">
          <i @click="support ('approve')" v-if="state" class="iconfont  icon-zan  pointer beforeApprove"></i>
          <i @click="notice" v-if="mainData.feedback=='approve'" class="iconfont  icon-zan1  pointer " :class="{'afterApprove':mainData.feedback=='approve'}"></i>
          <span class="question-yes  " :class="{'font16fbc02d':mainData.feedback=='approve'}">{{mainData.approve}}</span>
        </div>
        <div class="floatl">
          <i @click="support ('oppose')" v-if="state1" class="iconfont  icon-cai  pointer beforeOppose"></i>
          <i @click="notice" v-if="mainData.feedback=='oppose'" class="iconfont  icon-buzan  pointer " :class="{'afterOppose':mainData.feedback=='oppose'}"></i>
          <span class="question-yes" :class="{'font16fbc02d':mainData.feedback=='oppose'}">{{mainData.oppose}}</span>
        </div>
      </div>
      <div>
        <span @click="adoptAnwser" v-if="showAdopt" class="adopt pointer">采纳该答案</span>
        <span  v-if="showAreadyAdopt" class="adopt">您已采纳该答案</span>
        <span @click="showTextarea=!showTextarea"  class="pointer reply">回复</span>
        <span class="pointer" @click="showReply()">
          <span>展开回复</span>
          <i class="iconfont icon-zhankai" :class="{'spread':showr}"></i>
        </span>
      </div>

    </div>
    <reply v-show="showr" v-for="(item,index) in mainData.answer_reply_list" :key="index" :mainData="item"></reply>
    <replyMsg v-show="showTextarea"  :mainData="mainData"></replyMsg>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
  import Bus from '../../assets/js/bus'
  import reply from './13-reply'
  import replyMsg from './14-reply-msg'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        showr: false,
        showTextarea:false,
        showAreadyAdopt:false,
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
        } else return false;
      },
      state1: function () {
        if (this.mainData.feedback == '' || this.mainData.feedback == 'approve') {
          return true
        } else return false;
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
            this.showAreadyAdopt=true;
            this.$fn.showNotice(this, res.data.msg, 'success');
            Bus.$emit('replyover');
          }
        })
      },
      support(str) {
        if (this.mainData.feedback) {
          this.notice();
          return
        }
        var obj = {};
        obj.faq_answer_id = this.mainData.id;
        obj.appraisal = str;
        this.$post('/community/appraisal/faqanswer', obj).then(res => {
          console.log(res)
          if (!res.data.err) {
            this.mainData.feedback = str;
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
        this.showr = !this.showr;
      }
    },
    created() {
      console.log(this.mainData.feedback)
      if (this.mainData.custom_user_id == localStorage.uid) {
        if(this.mainData.optimal=true){
          this.showAreadyAdopt=true
        }
        else{
          this.showAdopt = true;
        }
      }
    },
    components: {
      reply: reply,
      replyMsg: replyMsg
    }
  }

</script>

<style scoped>
  .bestAnwser {
    width: 88px;
    height: 128px;
    line-height: 128px;
    background: #66bb6a;
    position: absolute;
    left: -95px;
    top: 0px;
  }
  .answerContent{
    padding:8px;
  }
  .user_status {
    background: #FCF8E3;
    border-radius: 3px;
    padding: 2px;
    margin-left: 5px;
  }
  .spread{
    transform: rotate(-180deg);
  }
  .reply{
    margin-right: 24px;
  }
  .userinfo {
    margin-bottom: 10px;
  }

  .icon-zhankai {
    display: inline-block;
    transition: all ease 0.5s;
  }

  .toolbar {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid rgba(0, 0, 0, 0.09);
    padding: 8px;
    padding-top: 0px;
  }

  .disabled {
    cursor: disabled;
  }

  .adopt {
    margin-right: 24px;
  }

  .beforeApprove,
  .beforeOppose {
    font-size: 22px;
    color: #666;
  }

  .afterApprove,
  .afterOppose {
    font-size: 24px;
    color: #fbc02d;
  }

  .anwser-container {
    padding: 32px;
    margin: 32PX 0;
    background: white;
  }

  .question-user-icon {
    width: 48px;
    height: 48px;
    margin-right: 32px;
    border-radius: 50%;
  }

  .question-yes {
    margin-right: 54px;
    font-size: 16px;
    font-family: "MicroSoft YaHei", "PingFangSC-Light";
  }

  .msg-container {
    padding-left: 80px;
  }

  .msg-moudel {}

</style>
