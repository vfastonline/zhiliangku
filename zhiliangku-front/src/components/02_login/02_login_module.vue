<template>
  <div>
    <el-dialog
      :visible.sync="module_show"
      width="500px"
      :show-close="false"
      center>
      <BlockTitle @close="module_show=false" slot="title" :block_title="title_key"></BlockTitle>
      <LogupBlock @log_up_success="specify_display('log_in')" v-show="block_show_switch.log_up"></LogupBlock>
      <LoginBlock @log_in_success="success" v-show="block_show_switch.log_in"></LoginBlock>
      <ResetPassword v-show="block_show_switch.reset_password"></ResetPassword>
    </el-dialog>

  </div>
</template>

<script>
  import Vue from 'vue'
  import BlockTitle from './03_title'
  import {Dialog, Form, FormItem, Input} from 'element-ui'
  import LoginBlock from './04_login_block'
  import LogupBlock from './05_logup_block'
  import Bus from '../../assets/js/02_bus'
  import ResetPassword from './06_reset_password'

  Vue.use(Dialog)
  Vue.use(FormItem)
  Vue.use(Form)
  Vue.use(Input)
  export default {
    name: "login_module",
    data() {
      return {
        module_show: false,
        block_show_switch: {
          log_in: false,
          log_up: false,
          reset_password:false
        },
        title_key:'登录'
      }
    },
    methods: {
      success(){
        this.module_show=false
        this.$emit('success')
      },
      specify_display(data) {
        this.module_show = true
        this.title_key=data.title_key
        var map = this.block_show_switch
        for (var k in map) {
          map[k] = false
        }
        map[data['show_key']] = true
      }
    },
    components: {
      BlockTitle: BlockTitle,
      LoginBlock: LoginBlock,
      LogupBlock: LogupBlock,
      ResetPassword:ResetPassword
    },
    created() {
      Bus.$on('specify_display', this.specify_display)
      Bus.$on('loginPagerLogin',function(obj){
         
      })
    }
  }
</script>
<style>
  @import "./style/01_dialog_style.scss";
  @import "./style/02_input_style.scss";
</style>
<style scoped>
  .login-commen-container-button {
    width: 400px;
    background: #23b8ff 100%;
  }
</style>
