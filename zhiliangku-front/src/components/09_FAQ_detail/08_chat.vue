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
        <span class="font1_16_9 createTime">{{mainData.create_time}}</span>
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
          <span @click="showTextarea=!showTextarea"  class="cp reply">回复</span>
          <span class="cp" @click="showReply()">
              <span>展开回复</span>
              <i class="iconfont icon-zhankai" :class="{'spread':showr}"></i>
            </span>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: "chat",
      props: {
          main_data: {}
      }
    }
</script>

<style scoped>

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
    padding-left:52px;
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
    margin: 32PX 50px;
    background: white;
    border-radius:10px;
  }
  .anwser_info_left {
    padding-top:43px;
    width:120px;
  }

  .anwser_info_right {
    margin-left:120px;
    padding:65px 32px 32px 0;
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

</style>
