<template>
  <div class="add_reply_msg hc">
    <!-- <div class="pointer marginbottom8"><span>回复</span> <i class="iconfont icon-chakantiezihuifu"></i></div> -->
    <div class="reply_msg">
      <el-input v-model="content" class="text_area" type="textarea"></el-input>
      <div class="ftr">
        <GreyButton @click="cancel_content" :S="{padding:'9px 10px','font-size':'0px'}"><span class="font1_20_f cancel">{{cancel}}</span>
        </GreyButton>
        <BlueButton @click="$emit('submit',content)"><span class="font1_20_f submit">{{submit}}</span></BlueButton>
      </div>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .text_area {
    margin-bottom: 15px;
  }

  .add_reply_msg {
    padding-top: 12px;
  }

  .reply_msg {
  }

  .submit, .cancel {
    padding: 0 30px;
  }

  .cancel {
    padding-right: 20px;
  }
</style>
<script>
  import Bus from '../../assets/js/02_bus'
  import BlueButton from '../../components/00_common/04_blue_button'
  import GreyButton from '../../components/00_common/02_grey_button'

  export default {
    name: 'reply_msg',
    data() {
      return {
        content: ''
      }
    },
    props: {
      mainData: Object,
      cancel:{default:'取消'} ,
      submit:{default:'提交'}
    },
    methods: {
      cancel_content() {
        this.content = ''
        this.$emit('close')
      }
    },
    created() {
      Bus.$on('editor_reply')
    },
    components: {
      BlueButton: BlueButton,
      GreyButton: GreyButton
    }
  }
</script>


