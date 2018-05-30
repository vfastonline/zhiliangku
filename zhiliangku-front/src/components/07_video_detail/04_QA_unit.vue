<template>
  <div @click="handleClick" class="mw  qc-container">
    <div class="clearfix">
      <div class="icon_box ftc fl vm ">
      <img class="qc-user-icon" :src="mainData.custom_user_avatar" alt="">        
      </div>
      <div class=" qc-text-container">
        <div class="mt8" >
          <span class="font1_14_9 qctc-tag">{{mainData.custom_user_nickname}}</span>
          <span class="font1_14_9 qctc-tag">{{mainData.create_time}}提问</span>
        </div>
        <div class="font1_20_3 clearfix mt8">
          <div class="fl qctc-qustion-content">{{mainData.title}}</div>
          <div class="fr">
            <span class="font1_16_3 anwser">{{mainData.faq_answer_count}}次回答</span>
            <span class="font1_16_3">{{mainData.browse_amount}}次浏览</span>
          </div>
        </div>
        <div class="clearfix">
          <!--<div class="font1_14_23b8ff">悬赏 {{mainData.reward}} 积分</div>-->
          <div class="font1_14_23b8ff">{{mainData.status_name}}</div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
  .anwser{
    margin-right:20px;
  }
  .qc-container {
    box-sizing: border-box;
    padding: 24px 32px 38px 0;
    background: #fcfcfc;
    margin-bottom: 20px;
    border-radius: 10px 
  }
  .icon_box {
    width: 120px;
  }
  .mt8 {
    margin-bottom: 8px;
  }

  .qc-user-icon {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    padding-top:5px;
  }

  .qc-text-container {
    margin-left: 120px;
  }

  .qctc-tag {
    margin-right: 16px;
  }

  .qctc-qustion-content {
    max-width: 845px;
  }
  .font1_14_9 {
    color: #7c7e8c;
  }

  .font1_14_23b8ff {
    color: #23b8ff;
    margin-top: 10px;
  }

</style>
<script>
  export default {
    name: 'question_unit',
    data() {
      return {}
    },
    props: {
      mainData: Object
    },
    methods: {
      handleClick() {
        this.$emit('haveClick')
      }
    },
    created() {
      // console.log(this.mainData)
      //   不能再这里处理，当数据改变时候，这个dom节点本身就会在，数据单纯改变了图片路径，却没有经历这个钩子
      //   this.$fn.addString(this.$myConst.httpUrl,this.mainData,'custom_user_avatar')
    }
  }

</script>
