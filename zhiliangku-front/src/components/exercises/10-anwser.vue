<template>
  <div class="anwser-container incenter">
    <div class="relative userinfo">
      <img class="question-user-icon imgmiddle" :src="$myConst.httpUrl+mainData.custom_user_avatar" alt="">
      <span class="font14pl7c7e8c">{{mainData.custom_user_nickname}}</span>
      <span class="font14pl7c7e8c scan">{{mainData.create_time}}</span>
    </div>
    <div v-html="mainData.answer">
    </div>
    <div class="toolbar">
      <div>
        <i @click="support ()" v-show="!mainData.approve" class="iconfont  icon-zan  pointer weizan"></i>
        <i @click="oppose ()" else class="iconfont  icon-zan1  pointer yizan"></i>
        <span class="question-yes font16fbc02d">{{mainData.approve}}</span>
      </div>
      <div class="pointer">
        <span>展开回复</span>
        <i class="iconfont icon-zhankai"></i>
      </div>
    </div>
    <reply v-for="(item,index) in mainData.answer_reply_list" :key="index" :mainData="item"></reply>
    <replyMsg></replyMsg>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
  import reply from './13-reply'
  import replyMsg from './14-reply-msg'
  export default {
    name: 'HelloWorld',
    data() {
      return {}
    },
    props: {
      mainData: Object
    },
    methods: {
      support(type) {
        var obj;
        switch (type) {
          case 0:
            obj = {
              oppose: 0,
              approve: 1
            };
            break;
          case 1:
            obj = {
              oppose: 1,
              approve: 0
            };
            break;
          default:
            break;
        }
        this.$post('/community/appraisal/faqanswer', obj).then(res => {
          console.log(res)
        })
      }
    },
    created() {

    },
    components: {
      reply: reply,
      replyMsg: replyMsg
    }
  }

</script>

<style scoped>
  .user_status {
    background: #FCF8E3;
    border-radius: 3px;
    padding: 2px;
    margin-left: 5px;
  }

  .userinfo {
    margin-bottom: 10px;
  }

  .icon-zhankai {
    transition: all ease 0.5s;
  }

  .toolbar {
    display: flex;
    justify-content: space-between;
  }

  .weizan {
    font-size: 22px;
    color: #666;
  }

  .yizan {
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
  }

  .msg-container {
    padding-left: 80px;
  }

  .msg-moudel {}

</style>
