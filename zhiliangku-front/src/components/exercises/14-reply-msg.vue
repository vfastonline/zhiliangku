<template>
  <div class="add_reply_msg">
    <!-- <div class="pointer marginbottom8"><span>回复</span> <i class="iconfont icon-chakantiezihuifu"></i></div> -->
    <div class="reply_msg">
        <el-input class="marginbottom8" type="textarea"></el-input> <el-button>添加回复</el-button>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.add_reply_msg{
    padding-top:12px;
}
.reply_msg{
    text-align: right ;
}
</style>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
    }
  },
  props:{

  },
  methods:{

  },
  created(){

  },
  components:{
    
  }
}
</script>


