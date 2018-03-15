<template>
  <div class="reply_container">
    <div class="relative user_info">
      <img class="question-user-icon imgmiddle" :src="$myConst.httpUrl+mainData.custom_user_avatar" alt="">
      <span class="font14pl7c7e8c">{{mainData.custom_user_nickname}}</span>
      <span class="user_status" >{{mainData.role}}</span>
      <span class="font14pl7c7e8c scan">{{mainData.create_time}}</span>
    </div>
    <div class="msg-container">
        {{mainData.reply}}
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.msg-container{
    margin-bottom:10px;
}
.reply_container{
    padding: 8px 0 10px 0;
    border-bottom:1px solid rgba(0,0,0,0.09);
}
.question-user-icon {
    width: 48px;
    height: 48px;
    margin-right: 32px;
    border-radius: 50%;
  }
.user_info{
    margin-bottom: 10px;
}
</style>
<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {}
    },
    props: {
      mainData:Object
    },
    methods: {

    },
    created() {

    },
    components: {

    }
  }

</script>
