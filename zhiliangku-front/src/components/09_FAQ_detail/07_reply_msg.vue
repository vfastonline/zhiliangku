<template>
  <div class="add_reply_msg">
    <!-- <div class="pointer marginbottom8"><span>回复</span> <i class="iconfont icon-chakantiezihuifu"></i></div> -->
    <div class="reply_msg">
      <el-input v-model="content" class="text_area" type="textarea"></el-input>
      <el-button @click="sendReply">添加回复</el-button>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .text_area{
    margin-bottom: 15px;
  }
  .add_reply_msg{
    padding-top:12px;
  }
  .reply_msg{
  }
</style>
<script>
  import Bus from '../../assets/js/02_bus'
  export default {
    name: 'reply_msg',
    data () {
      return {
        content:''
      }
    },
    props:{
      mainData:Object
    },
    methods:{
      sendReply(){
        var obj={};
        obj.faq_answer_id=this.mainData.id;
        obj.custom_user_id=localStorage.uid;

        //提问ID  回答ID 回复ID
        // custom_user_id
        obj.reply=this.content;
        this.$post('/community/add/faqanswerreply',obj).then(res=>{
          if(!res.data.err){
            Bus.$emit('replyover');
            this.content=''
          }
        })
      }
    },
    created(){
      if(this.mainData.reply){
        this.content=this.mainData.reply
      }
    },
    components:{

    }
  }
</script>


