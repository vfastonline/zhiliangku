<template>
  <div class="anwser-container incenter r">
    <!--<div v-if="mainData.optimal" class="bestAnwser fontcenter">
      <span class="bestAnwserContent font1_16_fff ftc">最佳答案</span>
    </div>-->
    <div class="anwser_info_left fl ftc">
       <img class="question-user-icon imgmiddle" :src="$myConst.httpUrl+mainData.custom_user_avatar" alt="">
    </div>
    <div class="anwser_info_right">
        <div class="r userinfo">
          <span class="font1_16_9">{{mainData.custom_user_nickname}}</span>
          <span class="font1_16_9 createTime fr">{{mainData.create_time}}</span>
        </div>
        <div class="answerType font1_18_b4">答主</div>
        <div class="answerContent font1_18_9" v-html="mainData.answer">
        </div>
        <div class="toolbar">
          <div>
            <div class="fl praise">
              <i @click="support ('approve')" v-if="state" class="iconfont  icon-zan  cp beforeApprove"></i>
              <i @click="notice" v-if="mainData.feedback=='approve'" class="iconfont  icon-zan1  cp " :class="{'afterApprove':mainData.feedback=='approve'}"></i>
              <span class="question-yes  " :class="{'font16fbc02d':mainData.feedback=='approve'}">{{mainData.approve}}</span>
            </div>
            <div class="fl praise">
              <i @click="support ('oppose')" v-if="state1" class="iconfont  icon-cai  cp beforeOppose"></i>
              <i @click="notice" v-if="mainData.feedback=='oppose'" class="iconfont  icon-buzan  cp " :class="{'afterOppose':mainData.feedback=='oppose'}"></i>
              <span class="question-yes" :class="{'font16fbc02d':mainData.feedback=='oppose'}">{{mainData.oppose}}</span>
            </div>
            <!--红心-->
            <div class="fl">
              <i @click="support ('oppose')" v-if="state1" class="iconfont  icon-cai  cp beforeOppose"></i>
              <i @click="notice" v-if="mainData.feedback=='oppose'" class="iconfont  icon-buzan  cp " :class="{'afterOppose':mainData.feedback=='oppose'}"></i>
            </div>
          </div>
          <div>
            <span @click="adoptAnwser" v-if="showAdopt" class="adopt cp">采纳该答案</span>
            <span  v-if="showAreadyAdopt" class="adopt">您已采纳该答案</span>
            <span @click="showTextarea=!showTextarea"  class="cp reply replayButton">回复</span>
            <span class="cp replayButton" @click="showReply()">
              <span>展开回复</span>
              <i class="iconfont icon-zhankai" :class="{'spread':showr}"></i>
            </span>
          </div>

        </div>
    </div>
    <div class="reply_box">
      <reply v-show="showr" v-for="(item,index) in mainData.answer_reply_list" :key="index" :mainData="item" ></reply>
      <replyMsg v-show="showTextarea"  :mainData="mainData"></replyMsg>
    </div>
    <!--<fixedButton class="fixedButton" @click.native="showTextarea=!showTextarea" text="我要评论">-->
        <!--&lt;!&ndash; <img src="" alt="" style="background-color:red"> &ndash;&gt;-->
        <!--<span>？</span>-->
    <!--</fixedButton>-->
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
  import Bus from '../../assets/js/02_bus'
  import reply from './06_reply'
  import replyMsg from './07_reply_msg'
  // import fixedButton from '../08_community/05_fixed_button.vue'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        showr: false,
        showTextarea:false,
        showAreadyAdopt:false,
        showAdopt:false
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
        obj.custom_user_id=localStorage.uid;
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
      console.log(this.mainData)
      if (this.mainData.custom_user_id == localStorage.uid) {
        if(this.mainData.optimal==true){
          this.showAreadyAdopt=true
        }
        else{
          this.showAdopt = true;
        }
      }
    },
    components: {
      reply: reply,
      replyMsg: replyMsg,
      // fixedButton: fixedButton
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
  .createTime {
    padding-right:30px;
  }

  .icon-zhankai {
    display: inline-block;
    transition: all ease 0.5s;
  }

  .toolbar {
    display: flex;
    justify-content: space-between;
    /*border-bottom: 1px solid rgba(0, 0, 0, 0.09);*/
    padding: 8px;
    padding-top: 0px;
  }
  .praise {
    width: 120px;
    height: 40px;
    text-align: right;
    border-radius: 8px;
  }
  .praise:hover {
    background-color: #00bcd5;
  }
  .praise:hover span{
    color:#fff;
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
    margin: 32PX 0;
    background: white;
    border-radius:10px;
  }
  .anwser_info_left {
    padding-top:43px;
    width:120px;
    height:35px;
  }

  .anwser_info_right {
    margin-left:120px;
    padding:40px 32px 32px 0;
  }

  .question-user-icon {
    width: 60px;
    height: 60px;
    border-radius: 50%;
  }

  .question-yes {
    margin-right: 36px;
    font-size: 16px;
    font-family: "MicroSoft YaHei", "PingFangSC-Light";
  }
  .reply_box {
    padding-top:20px;
    background-color: #fafafa;
  }
  .replayButton {
    display: inline-block;
    width: 120px;
    height: 40px;
    line-height: 40px;
    background-color: #00bcd5;
    text-align: center;
    color:#fff;
    border-radius: 8px;
  }

</style>
