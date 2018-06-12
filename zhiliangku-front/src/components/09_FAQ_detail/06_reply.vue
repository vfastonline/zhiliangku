<template>
  <div class="reply_container hc">
    <div class="user_info">
      <div class="ftc img_box">
        <img class="question-user-icon" :src="$myConst.httpUrl+mainData.custom_user_avatar" alt="">
      </div>
      <div class="content">
        <div class="replay_info_right">
          <span class="font1_16_9">{{mainData.custom_user_nickname}}</span>
          <span class="font1_16_9 scan fr">{{mainData.create_time}}</span>
        </div>
        <div class="msg-container font1_18_6">
          {{mainData.reply}}
        </div>
      </div>
    </div>
    <div class="toolbar ftr">
      <!--<div>-->
      <!--<div>-->
      <!--<div class="fl praise ftc cp " :class="{'yes':mainData.feedback==='approve',empty:!mainData.feedback}">-->
      <!--<i @click="support ('approve')"  class="iconfont  icon-zan   praise_block_icon"></i>-->
      <!--<span class="question-yes dib vm">{{mainData.approve}}</span>-->
      <!--</div>-->
      <!--<div class="fl praise ftc cp" :class="{'no':mainData.feedback==='oppose',empty:!mainData.feedback}">-->
      <!--<i @click="support ('oppose')"  class="iconfont  icon-cai  cp praise_block_icon"></i>-->
      <!--<span class="question-yes dib vm">{{mainData.oppose}}</span>-->
      <!--</div>-->
      <!--</div>-->
      <!--</div>-->
      <div v-if="mainData.is_self" class="">
        <tag_button class="tag_edit cp " @click="editor">
          <img src="../11_personal_center/img/编辑icon.png" alt="">
          <span class="font1_22_9">编辑</span></tag_button>
        <tag_button class=" cp" @click="deleteReply">
          <img src="../11_personal_center/img/编辑icon.png" alt="">
          <span class="font1_22_9">删除</span>
        </tag_button>
      </div>
      <transition
        enter-active-class="animated fadeInUp"
        leave-active-class="animated fadeOutDown"
      >
        <replyMsg v-if="showTextarea" ref="reply_content" @close="showTextarea=false" @submit="submit"></replyMsg>
      </transition>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->

<script>
  import Bus from '../../assets/js/02_bus'
  import replyMsg from './07_reply_msg'
  import tag_button from '../11_personal_center/08_tag_0'

  export default {
    name: 'reply',
    data() {
      return {
        showTextarea: false
      }
    },
    props: {
      mainData: Object,
    },
    methods: {
      editor() {
        this.showTextarea = !this.showTextarea
        this.$nextTick().then(res => {
          if (!this.$refs.reply_content) return
          this.$refs.reply_content.content = this.mainData.reply
        })
      },
      //评论删除功能 接口未写正确。
      deleteReply() {
        var obj = {};
        obj.faqanswerreply_id = this.mainData.id;
        //提问ID  回答ID 回复ID
        // custom_user_id
        this.$post('community/del/faqanswerreply', obj).then(res => {
          if (!res.data.err) {
            Bus.$emit('replyover');
            this.$fn.showNotice(this, res.data.msg, 'success')
          }
        })
      },
      submit(content) {
        var obj = {};
        obj.faqanswerreply_id = this.mainData.id;
        //提问ID  回答ID 回复ID
        // custom_user_id
        obj.reply = content;
        this.$post('/community/edit/faqanswerreply', obj).then(res => {
          if (!res.data.err) {
            Bus.$emit('replyover');
            this.$refs['reply_content'].content = ''
            this.showTextarea = false
            this.$fn.showNotice(this, res.data.msg, 'success')
          }
        })
      },
    },
    created() {
    },
    components: {
      replyMsg: replyMsg,
      tag_button: tag_button,
    }
  }

</script>
<style scoped>
  /*下面内容是和上面备注之后的dom相匹配的*/
  /*.praise_block_icon{*/
  /*color: #666;*/
  /*font-size: 30px;*/
  /*}*/
  /*.user_info {*/
  /*padding-top: 5px;*/
  /*}*/
  /*.empty:hover {*/
  /*background-color: #00bcd5;*/
  /*span{*/
  /*color: white;*/
  /*}*/
  /*.iconfont{*/
  /*color: white;*/
  /*}*/
  /*}*/
  /*.yes,.no{*/
  /*background-color: #00bcd5;*/
  /*span{*/
  /*color: white;*/
  /*}*/
  /*.iconfont{*/
  /*color: white;*/
  /*}*/
  /*}*/
  .msg-container {
    margin-bottom: 10px;
    box-sizing: border-box;
    /*margin-left: 53px;*/
    padding: 8px 0px 0px 0px;
  }

  .reply_container {
    padding: 8px 0 10px 0;
    /*border-bottom:1px solid rgba(0,0,0,0.09);*/
    /*margin: 12px 0;*/
    margin-bottom: 12px;
    width: 1104px;
    background-color: #fff;

  }

  .question-user-icon {
    width: 60px;
    height: 60px;
    margin-left: 16px;
    margin-right: 16px;
    border-radius: 50%;
  }

  .user_info {
    margin-top:16px;
    margin-bottom: 10px;
    padding-right: 40px;
    display: flex;
    justify-content: space-between;
    align-items: start;
  }

  .toolbar {
    /*display: flex;*/
    /*justify-content: space-between;*/
    padding: 0px 50px 8px 51px;
  }

  .tag_edit {
    margin-right: 30px;
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

  .img_box {
    width: 120px;
    height: 50px;
  }

  .replay_info_right {
    width: 972px;
  }

  .scan {
  }
</style>
