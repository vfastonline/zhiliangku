<template>
  <div class="login_block">
    <el-form
      :model="form_data"
      status-icon
      :rules="rules"
      ref="form_el" class="form_wrap">
      <el-form-item prop="username">
        <el-input v-model="form_data.username" :placeholder="'请输入登录手机号'"></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input @keyup.enter.native="submitForm('form_el','loginFun',form_data) " :placeholder="'请输入密码'"
                  type="password"
                  v-model="form_data.password"
                  auto-complete="off"></el-input>
      </el-form-item>
      <el-button @click="submitForm('form_el','loginFun',form_data)"
                 class="login-commen-container-button">
        <span class="font1_26_f"> 登录</span>
      </el-button>
    </el-form>
    <div class="ftr">
      <span @click="forget_password" class="cp">忘记密码？</span>
    </div>

  </div>
</template>

<script>
  import Vue from 'vue'
  import BlockTitle from './03_title'
  import Bus from '../../assets/js/02_bus'
  import {Dialog, Form, FormItem, Input} from 'element-ui'

  Vue.use(Dialog)
  Vue.use(FormItem)
  Vue.use(Form)
  Vue.use(Input)
  export default {
    name: "login_block",
    data() {
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'))
        }
        if (value.length < 6 || value.length > 16) {
          callback(new Error('请输入6-16位密码（区分大小写）'))
        }
        callback()
      }
      var check_phone_number = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('手机号不能为空'))
        }
        setTimeout(() => {
          var phonecheck = /^1[3|4|5|7|8][0-9]{9}$/
          if (phonecheck.test(value)) {
            callback()
          }
          callback(new Error('请输入正确的手机号'))
        }, 100)
      }
      return {
        form_data: {
          username: '',
          password: ''
        },
        rules: {
          username: [{validator: check_phone_number, trigger: 'blur'}],
          password: [{validator: validatePass, trigger: 'blur'}],
        }
      }
    },
    methods: {
      forget_password() {
        Bus.$emit('specify_display', {
          show_key: 'reset_password',
          title_key: '忘记密码'
        })
      },
      submitForm(formName, funkey, data, callbackfun, param) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            if (funkey) {
              this[funkey](data, callbackfun, param)
            }
          } else {
            console.log('error submit!!')
            return false
          }
        })
      },
      loginFun() {
        this.$post('/customuser/login', this.form_data).then(res => {
          if (!res.data.err) {
            if (res.data.msg === 'success') this.centerDialogVisible = false // 察觉暂无用
            for (var k in res.data.data.user) {
              localStorage[k] = res.data.data.user[k]
            }
            this.$fn.showNotice(this, '您已成功登录', 'success')
            this.$emit('log_in_success')
            Bus.$emit('refreshAvatar')
          }
        })
      }
    },
    components: {
      BlockTitle: BlockTitle
    },
    created() {
      Bus.$on('loginPagerLogin', this.loginFun)
    }
  }
</script>
<style>
  /*@import "./style/01_dialog_style.scss";*/
  /*@import "./style/02_input_style.scss";*/

  .form_wrap > .el-button:hover {
    color: #FFF;
    border-color: #c6e2ff;
    background-color: #23b8ff;
  }
</style>
<style scoped>
  /*.login_block {*/
  .form_wrap .login-commen-container-button {
    width: 400px;
    background: #23b8ff 100%;
    display: inline-block;
    text-align: center;
    border-radius:4px;
    height: 40px;
    line-height: 40px;
    padding: 0 20px;
  }

  /*}*/
</style>
