<template>
  <div @click="handleClick" class="mainwidth rise qc-container marginbottom24 pointer">
    <div class="clearfix">
      <img class="floatl qc-user-icon" :src="mainData.custom_user_avatar" alt="">
      <div class=" qc-text-container">
        <div class="marginbottom8 ">
          <span class="font14pl7c7e8c qctc-tag">{{mainData.custom_user_nickname}}</span>
          <span class="font14pl7c7e8c qctc-tag">{{mainData.create_time}}提问</span>
        </div>
        <div class="font20pr3a3c50 clearfix marginbottom8">
          <div class="floatl qctc-qustion-content">{{mainData.title}}</div>
          <div class="floatr">
            <span class="font16pl3a3c50">{{mainData.faq_answer_count}}回答</span>
            <span class="font16pl3a3c50">{{mainData.browse_amount}} &nbsp; 次浏览</span>
          </div>
        </div>
        <div>
          <div class="font14pr23b8ff">悬赏 {{mainData.reward}} 积分</div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
  .qc-container {
    box-sizing: border-box;
    padding: 24px 32px 38px 32px;
    background: white;
  }

  .qc-user-icon {
    width: 64px;
    height: 64px;
    border-radius: 50%;
  }

  .qc-text-container {
    margin-left: 80px;
  }

  .qctc-tag {
    margin-right: 16px;
  }

  .qctc-qustion-content {
    max-width: 845px;
  }

</style>
<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {

      }
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
