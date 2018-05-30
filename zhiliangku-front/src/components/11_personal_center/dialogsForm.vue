<template>
  <div>
    <el-dialog :width="'650px'" :title="dialogTitle" :visible.sync="show">
      <div v-if="dialogContent=='email'" class="dialog-li incenter emial-container relative">
        <div class="input-li relative">
          <div class="tags">邮箱地址：</div>
          <el-form :model="emailform" ref="email" :rules="emailRule">
            <el-form-item prop="email">
              <el-input v-model="emailform.email" auto-complete="off"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </div>
      <div v-if="dialogContent=='phone'" class="dialog-li incenter emial-container relative">
        <div class="input-li relative">
          <div class="tags">手机号：</div>
          <el-form :model="phoneform" ref="phone" :rules="phoneRule">
            <el-form-item prop="phone">
              <el-input v-model="phoneform.phone" auto-complete="off"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </div>
      <div v-if="needpassword" class="dialog-li incenter emial-container relative">
        <div class="input-li relative">
          <div class="tags">密码：</div>
          <el-form :model="passwordform" ref="password" :rules="passwordRule">
            <el-form-item prop="password">
              <el-input v-model="passwordform.password" auto-complete="off"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </div>
      <div v-if="needpassword" class="dialog-li incenter emial-container relative">
        <div class="input-li relative">
          <div class="tags">重复密码：</div>
          <el-form :model="passwordcheckform" ref="passwordcheck" :rules="passwordcheckRule">
            <el-form-item prop="passwordcheck">
              <el-input v-model="passwordcheckform.passwordcheck" auto-complete="off"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </div>
      <div v-if="dialogContent=='phone'" class="dialog-li incenter emial-container relative">
        <div class="input-li relative">
          <div class="tags">短信验证码：</div>
          <el-form class="" :model="codeform" ref="code" :rules="codeRule">
            <el-form-item prop="code">
              <el-input :style="{width:'318px','margin-right':'16px'}" v-model="codeform.code" auto-complete="off"></el-input>
              <el-button @click="getCode(phoneform)" :style="{width:'134px'}">{{buttonStr}}</el-button>
            </el-form-item>
          </el-form>
        </div>
      </div>
      <rcb @submit="submit(dialogContent)" @cancel="changeShow()" :styleData="buttonContainerStyle" class="footer-button-group"
        slot="footer" :layer="['cancel','submit']"></rcb>
    </el-dialog>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


</style>
<script>
  import Bus from '../../assets/js/02_bus'
  import rcb from './resumeContentButton'
  export default {
    name: 'HelloWorld',
    data() {
      var checkCode = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('验证码不能为空'));
        }else{
          return callback()
        }
      }
      var checkEmail = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('邮箱不能为空'))
        }
        var emailcheck = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
        if (emailcheck.test(value)) {
          callback()
        }
        callback(new Error('请输入正确的邮箱'))
      }
      var checkPhone = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('手机不能为空'))
        }
        var phonecheck = /^1[3|4|5|7|8][0-9]{9}$/;
        if (phonecheck.test(value)) {
          callback()
        }
        callback(new Error('请输入正确的手机号'))
      }
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        }
        if (value.length < 6 || value.length > 16) {
          callback(new Error('请输入6-16位密码（区分大小写）'))
        }
        if (this.passwordcheckform.passwordcheck != '') {
          this.$refs.passwordcheck.validateField('passwordcheck')
        }
        console.log(this)
        callback()
      };
      var validatePass2 = (rule, value, callback) => {

        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.passwordform.password) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
      return {
        emailform: {
          email: ''
        },
        emailRule: {
          email: [{
            validator: checkEmail,
            trigger: 'blur'
          }]
        },
        phoneform: {
          phone: ''
        },
        phoneRule: {
          phone: [{
            validator: checkPhone,
            trigger: 'blur'
          }]
        },
        passwordform: {
          password: ''
        },
        passwordRule: {
          password: [{
            validator: validatePass,
            trigger: 'blur'
          }]
        },
        passwordcheckform: {
          passwordcheck: ''
        },
        passwordcheckRule: {
          passwordcheck: [{
            validator: validatePass2,
            trigger: 'blur'
          }]
        },
        codeform: {
          code: ''
        },
        codeRule: {
          code: [{
            validator: checkCode,
            trigger: 'blur'
          }]
        },
        show: false,
        dialogTitle: '',
        dialogContent: '',
        buttonContainerStyle: {
          'text-align': 'center'
        },
        buttonStr: '点击获取验证码',
        email: '',
        phone: '',
        password: '',
        passwordcheck: '',
        code: ''
      }
    },
    props: {
      needpassword: Boolean
    },
    methods: {
      changeShow(type, str, c) {
        if (str) {
          this.dialogTitle = str;
        }
        if (type) {
          this.dialogContent = type;
        }
        if (!c) {
          this.show = !this.show;
        }
      },
      getCode(phoneform) {
        this.guard(['phone']);
        if (!this.flag) {
          return
        }
        this.$post('/customuser/send_sms', {
          phone: this.phoneform.phone
        }).then(res => {
          if (!res.data.err) {
            this.buttonStr = '已发送验证码'
          }
          console.log(res)
        })
      },
      guard(formNamearr) {
        var flag = true;
        for (var i = 0; i < formNamearr.length; i++) {
          this.$refs[formNamearr[i]].validate((valid) => {
            if (valid) {
              this[formNamearr[i]] = true;
              return true
            } else {
              this[formNamearr[i]] = false
              return false;
            }
          })
          if (this[formNamearr[i]] == false) {
            flag = false
          }
        }
        this.flag=flag;
        return flag
      },
      handlephone(dialogContent) {
        var postdata = {
          custom_user_id: localStorage.uid,
          phone: this.phoneform.phone,
          verify_code: this.codeform.code
        };
        var validarr = [dialogContent, 'code'];
        if (this.needpassword) {
          postdata.password = this.passwordform.password;
          validarr = [dialogContent, 'password', 'passwordcheck', 'code']
        }
        if (this.guard(validarr)) {
          this.$post('/personal_center/personal_settings/accountbind/phone', postdata).then(res => {
            if (!res.data.err) {
              this.sendMsgToDialogsForm(dialogContent, this.phoneform.phone, '修改手机号')
              this.sendMsg()
            }
          })
        }

      },
      sendMsg(){
        Bus.$emit('countDataChange')
      },
      handleemail(dialogContent) {
        var postdata = {
          email: this.emailform.email,
          custom_user_id: localStorage.uid,
        };
        var validarr = [dialogContent]
        if (this.needpassword) {
          postdata.password = this.passwordform.password
          validarr = [dialogContent, 'password', 'passwordcheck']
        }
        if (this.guard(validarr)) {
          this.$post('/customuser/send_activation_mail', postdata).then(res => {
            if (!res.data.err) {
              this.sendMsgToDialogsForm(dialogContent, this.emailform.email, '修改邮箱')
               this.sendMsg()
            }
          })
        }
      },
      submit(dialogContent) {
        switch (dialogContent) {
          case 'email':
            this.handleemail(dialogContent)
            break;
          case 'phone':
            this.handlephone(dialogContent)
            break;
          default:
            break;
        }
      },
      sendMsgToDialogsForm(type, data, title) {
        this.show = false;
        Bus.$emit('openDialogs', {
          type: type,
          data: data,
          title: title
        })
      }
    },
    created() {
      Bus.$on('dialogsFormOpen', res => {
        this.show = true;
        this.dialogContent = res.type;
        this.dialogTitle = res.title;
      })
      Bus.$on('dialogsFormClose', res => {
        this.show = false
      })

      console.log(this.password)
    },
    components: {
      rcb: rcb
    }
  }

</script>
