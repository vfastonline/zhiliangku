<template>
  <div class="reply_container">
    <div class="user_info">
      <div class="fl ftc img_box">
        <img class="question-user-icon" :src="$myConst.httpUrl+mainData.custom_user_avatar" alt="">
      </div>
      <div class="info_right">
        <span class="font14pl7c7e8c">{{mainData.custom_user_nickname}}</span>
        <span class="user_status">{{mainData.role}}</span>
        <span class="font14pl7c7e8c scan">{{mainData.create_time}}</span>
      </div>
    </div>
    <div class="msg-container">
      {{mainData.reply}}
    </div>
    <div class="toolbar">
      <div>
        <div class="fl praise">
          <i @click="support ('approve')" v-if="state" class="iconfont  icon-zan  cp beforeApprove"></i>
          <i @click="notice" v-if="mainData.feedback=='approve'" class="iconfont  icon-zan1  cp "
             :class="{'afterApprove':mainData.feedback=='approve'}"></i>
          <span class="question-yes  "
                :class="{'font16fbc02d':mainData.feedback=='approve'}">假1{{mainData.approve}}</span>
        </div>
        <div class="fl praise">
          <i @click="support ('oppose')" v-if="state1" class="iconfont  icon-cai  cp beforeOppose"></i>
          <i @click="notice" v-if="mainData.feedback=='oppose'" class="iconfont  icon-buzan  cp "
             :class="{'afterOppose':mainData.feedback=='oppose'}"></i>
          <span class="question-yes" :class="{'font16fbc02d':mainData.feedback=='oppose'}">假0{{mainData.oppose}}</span>
        </div>
        <!--红心-->
        <div class="fl">
          <i @click="support ('oppose')" v-if="state1" class="iconfont  icon-cai  cp beforeOppose"></i>
          <i @click="notice" v-if="mainData.feedback=='oppose'" class="iconfont  icon-buzan  cp "
             :class="{'afterOppose':mainData.feedback=='oppose'}"></i>
        </div>
      </div>
      <div>
        <span @click="adoptAnwser" v-if="showAdopt" class="adopt cp">采纳该答案</span>
        <span v-if="showAreadyAdopt" class="adopt">您已采纳该答案</span>
        <span @click="showTextarea=!showTextarea" class="cp reply">回复</span>
      </div>

    </div>
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
    width: 40x;
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
    padding: 8px 120px;
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
    padding-top:35px;
    width:120px;
    height:50px;
  }
  .info_right {
    margin-left:90px;
    margin-top:20px;
  }
</style>
<script>
  export default {
    name: 'reply',
    data() {
      return {}
    },
    props: {
      mainData: Object
    },
    methods: {},
    created() {

    },
    components: {}
  }

</script>
