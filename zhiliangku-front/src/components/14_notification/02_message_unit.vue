<template>
  <div class="hc mw main_message">
    <div class="message_content">
      <div class="font1_18_3">系统消息</div>
      <p class="font1_18_9 system_messages">{{main_data.content}}</p>
    </div>
    <div class="ftr message_bottom font1_18_9">
      <span v-if="main_data.have_read===false" @click="flagMessage(main_data.id)" class="cp font1_18_b4">标记为已读</span>
      <span  v-if="main_data.have_read===true" @click="flagMessage(main_data.id)"  class="cp font1_18_b4">已读</span>
      <span>{{main_data.create_time}}</span>
    </div>
  </div>
</template>

<script>
  export default {
    name: "message.vue",
    props: {
      main_data: {}
    },
    created() {
      console.log(this.$props)
    },
    methods: {
      flagMessage(id) {
        var obj={
          pk_id: id
        }
        this.$post('/notification/markasread',obj).then(res=> {
          if(res.data.msg=="success"){
            this.main_data.have_read=!this.main_data.have_read
          }
        })
      }
    }
  }
</script>

<style scoped>
  .main_message {

  }
  .message_content {
    min-height:108px;
    padding:20px 50px 30px;
    background-color:#fff;
  }
  .system_messages {
    padding-top: 15px;
    line-height: 27px;
  }
  .message_bottom {
    padding:13px 40px 37px 0;
  }
</style>
