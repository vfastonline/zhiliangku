<template>
  <div>
    <form style="display:none;">
      <input type="text">
      <input type="password">
    </form>
    <el-form
      :model="form_data"
      status-icon
      :rules="rules"
      ref="form_el" class="form_wrap">
      <el-form-item prop="phone">
        <el-input v-model="form_data.phone" :placeholder="'请输入登录手机号'"></el-input>
      </el-form-item>
      <el-form-item prop="code">
        <div class="code_container">
          <el-input :placeholder="'请输入验证码'"
                    v-model="form_data.code"
                    auto-complete="off">
          </el-input>
          <el-button @click="get_code" class="get_code_button"><span>{{code_str}}</span></el-button>
        </div>
      </el-form-item>
      <el-form-item prop="password">
        <el-input :placeholder="'请设置新密码'"
                  type="password"
                  v-model="form_data.password"
                  auto-complete="off">

        </el-input>
      </el-form-item>
      <el-form-item prop="password_repeat">
        <el-input :placeholder="'请确认新密码'"
                  type="password"
                  v-model="form_data.password_repeat"
                  auto-complete="off">
        </el-input>
      </el-form-item>
      <el-button @click="submitForm('form_el','reset_fun',form_data)" class="login-commen-container-button">
        <span class="font1_26_f"> 提交</span>
      </el-button>
      <input type="text" style="display:none;">
      <input type="password" style="display:none;">
    </el-form>
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
      var validateCode = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入验证码'));
        }
        if (value.length !== 4) {
          callback(new Error('请输入四位验证码'))
        }
        callback()
      }
      var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.form_data.password) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
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
          phone: '',
          password: '',
          password_repeat: '',
          code: ''
        },
        rules: {
          phone: [{validator: check_phone_number, trigger: 'blur'}],
          password: [{validator: validatePass, trigger: 'blur'}],
          password_repeat: [{validator: validatePass2, trigger: 'blur'}],
          code: [{validator: validateCode, trigger: 'blur'}]
        },
        code_str: '获取验证码'
      }
    },
    methods: {
      get_code() {
        if (typeof (this.code_str) === 'number') {
          this.$fn.showNotice(this, '请于' + this.code_str + 's后重试', 'info')
          return
        }
        this.$post('/customuser/send_sms', {phone: this.form_data.phone}).then(res => {
          console.log(res)
          if (!res.data.err) {
            this.code_str = 6;
            var interval = setInterval(() => {
              this.code_str--
              console.log(this)
              if (this.code_str === 0) {
                this.code_str = '获取验证码'
                clearInterval(interval)
              }
            }, 1000)
            return
          }
        })
      },
      forget_password() {
        this.$emit('forget_password')
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
      reset_fun() {
        var data = {
          phone: this.form_data.username,
          new_password: this.form_data.password,
          verify_code: this.form_data.code
        }
        this.$post('/customuser/retrieve_password_by_phone', data).then(res => {
          console.log(res)
          // 此处后端应该加上err
          if (!res.err) {
            this.$fn.showNotice(this, '密码修改成功，请登录', 'success')
            Bus.$emit('specify_display', {
              show_key: 'log_in',
              title_key: '登录'
            })
          }
        })
      },
    },
    components: {
      BlockTitle: BlockTitle
    }
  }
</script>
<style>
  @import "./style/01_dialog_style.scss";
  @import "./style/02_input_style.scss";

  .code_container {
    display: flex;
  }

   .code_container>.get_code_button {
    margin-left: 20px;
    width: 130px;
  }

  .form_wrap>.el-button:hover {
    color: #FFF;
    border-color: #c6e2ff;
    background-color:#23b8ff;
  }

</style>
<style scoped>
  .form_wrap .login-commen-container-button {
    width: 400px;
    background: #23b8ff 100%;
    display: inline-block;
    text-align: center;
    border-radius:4px;
    height: 40px;
    line-height: 40px;
  }

</style>
