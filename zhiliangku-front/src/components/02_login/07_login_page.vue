<template>
  <div class="loginpage-continer hc">
    <el-form :model="ruleForm2" status-icon :rules="rules2" ref="ruleForm2" label-width="100px">
      <el-form-item label="账号：" prop="account">
        <el-input type="text" placeholder="请输入登录邮箱/手机号" v-model="ruleForm2.account" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item label="密码：" prop="pass">
        <el-input @keydown.enter.native="submitForm('ruleForm2')" type="password" placeholder="6-16位密码，区分大小写"
                  v-model="ruleForm2.pass" auto-complete="off"></el-input>
      </el-form-item>
    </el-form>
    <div class="ftc loginpage-button">
      <el-button type="primary" @click="submitForm('ruleForm2')">登录</el-button>
    </div>
    <div class="ftc loginpage-forget">
      <span class="font14pr23b8ff pointer " @click="forgetPassword">忘记密码？</span>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .loginpage-continer {
    padding-top: 128px;
    width: 540px;
  }
  .loginpage-button {
    margin-bottom: 28px;
  }

  .loginpage-forget {
    margin-bottom: 16px;
  }

</style>
<script>
  import Bus from '../../assets/js/02_bus'
  import {Button} from 'element-ui'
  import Vue from 'vue'
  Vue.use(Button)
  var Base64 = window.Base64
  export default {
    name: 'login_page',
    data() {
      var usernameType = {
        phone: false,
        email: false
      }
      var checkAccount = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('邮箱/手机号不能为空'))
        }
        setTimeout(() => {
          var phonecheck = /^1[3|4|5|7|8][0-9]{9}$/
          var emailcheck = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/
          usernameType.phone = false
          usernameType.email = false
          if (phonecheck.test(value)) {
            usernameType.phone = true
            callback()
          }
          if (emailcheck.test(value)) {
            usernameType.email = true
            callback()
          }
          callback(new Error('请输入正确的邮箱/手机号'))
        }, 100)
      }
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'))
        }
        if (value.length < 6 || value.length > 16) {
          callback(new Error('请输入6-16位密码（区分大小写）'))
        }
        callback()
      }
      return {
        ruleForm2: {
          account: '',
          pass: '',
        },
        rules2: {
          account: [{
            validator: checkAccount,
            trigger: 'blur'
          }],
          pass: [{
            validator: validatePass,
            trigger: 'blur'
          }]
        },
        usernameType: usernameType,
        Base64: Base64
      }
    },
    methods: {
      forgetPassword() {
        Bus.$emit('forgetPassword', this.ruleForm2.account)
      },
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            var obj = {}
            obj.age = this.ruleForm2.account
            obj.pass = this.ruleForm2.pass
            obj.referrer = true
            if (this.$fn.funcUrl('next')) {
              obj.url = 'https://' + window.location.host + decodeURIComponent(this.$fn.funcUrl('next'))
            }
            Bus.$emit('loginPagerLogin', obj)
          } else {
            console.log('error submit!!')
            return false
          }
        })
      },
      resetForm(formName) {
        this.$refs[formName].resetFields()
      }
    },
    created() {
      // document.referrer
      var str
      if (this.$fn.funcUrl('next')) {
        str = 'https://' + window.location.host + decodeURIComponent(this.$fn.funcUrl('next'))
      }
      this.wxBase64Url =
        'https://open.weixin.qq.com/connect/qrconnect?appid=wx7c9efe7b17c8aef2&redirect_uri=http%3a%2f%2fwww.zhiliangku.com%2fcustomuser%2fweixin%2flogin&response_type=code&scope=snsapi_login&state=' +
        this.Base64.encode(str || '/') + '#wechat_redirect'
      this.qqBase64Url =
        'https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response_type=code&client_id=101447834&redirect_uri=http%3A%2F%2Fwww.zhiliangku.com%2Fcustomuser%2Fqq%2Flogin&state=' +
        this.Base64.encode(str || '/') + '&scope=get_user_info,get_info'
    }
  }

</script>
