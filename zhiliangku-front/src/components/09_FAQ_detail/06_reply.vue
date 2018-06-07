<template>
  <div class="reply_container">
    <div class="user_info">
      <div class="fl ftc img_box">
        <img class="question-user-icon" :src="$myConst.httpUrl+mainData.custom_user_avatar" alt="">
      </div>
      <div class="info_right">
        <span class="font1_16_9">{{mainData.custom_user_nickname}}</span>
        <!--<span class="user_status font1_16_9">{{mainData.role}}</span>-->
        <span class="font1_16_9 scan fr">{{mainData.create_time}}</span>
      </div>
    </div>
    <div class="msg-container font1_18_6">
      {{mainData.reply}}
    </div>
    <div class="toolbar">
      <div>
        <div class="fl praise">
          <i @click="support ('approve')"  class="iconfont  icon-zan  cp beforeApprove"></i>
          <i @click="notice" v-if="mainData.feedback=='approve'" class="iconfont  icon-zan1  cp "
             :class="{'afterApprove':mainData.feedback=='approve'}"></i>
          <span class="question-yes  "
                :class="{'font16fbc02d':mainData.feedback=='approve'}">假1{{mainData.approve}}</span>
        </div>
        <div class="fl praise">
          <i @click="support ('oppose')"  class="iconfont  icon-cai  cp beforeOppose"></i>
          <i @click="notice" v-if="mainData.feedback=='oppose'" class="iconfont  icon-buzan  cp "
             :class="{'afterOppose':mainData.feedback=='oppose'}"></i>
          <span class="question-yes" :class="{'font16fbc02d':mainData.feedback=='oppose'}">假0{{mainData.oppose}}</span>
        </div>
      </div>
      <div v-if="replyEdit">
      <span @click="showTextarea=!showTextarea" class="cp reply font1_18_6 replayButton">编辑</span>
      <span @click="deleteReply" class="cp reply font1_18_6 replayButton">删除</span>
      </div>
      <!--<div >-->
        <!--<span @click="showTextarea=!showTextarea" class="cp reply font1_18_6 replayButton">回复</span>-->
      <!--</div>-->

    </div>
    <replyMsg v-show="showTextarea"  :mainData="mainData"></replyMsg>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .user_info {
    padding-top: 5px;
  }

  .msg-container {
    margin-bottom: 10px;
    box-sizing: border-box;
    /* padding-left: 39px; */
    /*background: #eee;*/
    margin-left: 53px;
    padding: 8px;
  }

  .reply_container {
    padding: 8px 0 10px 0;
    /*border-bottom:1px solid rgba(0,0,0,0.09);*/
    margin: 20px 100px;
    background-color: #fff;
    border-radius: 10px;
  }

  .question-user-icon {
    width: 40px;
    height: 40px;
    margin-left: 16px;
    margin-right: 16px;
    border-radius: 50%;
  }

  .user_info {
    margin-bottom: 10px;
  }

  .toolbar {
    display: flex;
    justify-content: space-between;
    /*border-bottom: 1px solid rgba(0, 0, 0, 0.09);*/
    padding: 8px 16px 8px 120px;
    padding-top: 0px;
  }

  .praise {
    width: 120px;
    height: 40px;
    line-height: 40px;
    text-align: right;
    border-radius: 8px;
  }

  .praise:hover {
    background-color: #00bcd5;
  }

  .praise:hover span {
    color: #fff;
  }
  .question-yes {
    margin-right: 36px;
  }
  .adopt {
    margin-right: 24px;
  }

  .reply {
    margin-right: 24px;
  }
  .img_box {
    padding-top:25px;
    width:120px;
    height:50px;
  }
  .info_right {
    margin-left:90px;
    margin-top:20px;
  }
  .scan {
  padding-right:100px;
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
<script>
  import Bus from '../../assets/js/02_bus'
  import replyMsg from './07_reply_msg'
  export default {
    name: 'reply',
    data() {
      return {
        showTextarea:false,
        replyEdit: false
      }
    },
    props: {
      mainData: Object,
    },
    methods: {
      //评论删除功能 接口未写正确。
      deleteReply(){
        var obj={};
        obj.faq_answer_id=this.mainData.id;
        obj.custom_user_id=localStorage.uid;

        //提问ID  回答ID 回复ID
        // custom_user_id
        obj.reply=this.content;
        this.$post(' ',obj).then(res=>{
          if(!res.data.err){
            Bus.$emit('replyover');
          }
        })
      }
    },
    created() {
        if (this.mainData.custom_user_id == localStorage.uid) {
          this.replyEdit=true;
        }
      },
    components: {
      replyMsg: replyMsg
    }
  }

</script>
