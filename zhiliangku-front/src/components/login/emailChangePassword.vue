<template>
  <div class="loginpage-continer incenter">
    <el-form :model="ruleForm2" status-icon :rules="rules2" ref="ruleForm2" label-width="100px">
      <el-form-item label="输入新密码：" prop="pass">
        <el-input type="password" placeholder="6-16位密码，区分大小写" v-model="ruleForm2.pass" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item label="再次输入：" placeholder="再次输入密码" prop="checkPass">
        <el-input type="password" placeholder="" v-model="ruleForm2.checkPass" auto-complete="off"></el-input>
      </el-form-item>
    </el-form>
    <div class="fontcenter loginpage-button">
      <el-button type="primary" @click="submitForm('ruleForm2')">确定</el-button>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .loginpage-continer {
    padding-top: 128px;
    width: 540px;
  }
  .longinpage-bottom-icons{
    margin-right: 24px;
    margin-left:24px;
  }
  .other-login{
    margin-right:138px;
  }
  .loginpage-button{
    margin-bottom:28px;
  }
  .loginpage-forget{
    margin-bottom:16px;
  }
</style>
<script>
import Bus from '../../assets/js/bus'
 var Base64 = require('js-base64').Base64;
  export default {
    data() {
      var usernameType = {
        phone: false,
        email: false
      };
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        }
        if (value.length < 6 || value.length > 16) {
          callback(new Error('请输入6-16位密码（区分大小写）'))
        }
        callback()
      };
       var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.ruleForm2.pass) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
      return {
        ruleForm2: {
          pass: '',
          checkPass: '',
        },
        rules2: {
          pass: [{
            validator: validatePass,
            trigger: 'blur'
          }],
          checkPass: [{
            validator: validatePass2,
            trigger: 'blur'
          }]
        },
        usernameType: usernameType,
        Base64:Base64
      };
    },
    methods: {
      forgetPassword(){
        Bus.$emit('forgetPassword',this.ruleForm2.account)
      },
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!');
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      postData(){
          this.$post('/customuser/retrieve_password_by_email/',this.orgnizeData()).then(res=>{
              if(!res.data.err){
                  window.location.href='/login/'
              }
          })
      },
      orgnizeData(){
          var obj={};
          obj.hash=this.$fn.funcUrl('hash');
          obj.password=this.ruleForm2.pass;
          return obj
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    },
    created(){
      // document.referrer
       this.wxBase64Url =
        'https://open.weixin.qq.com/connect/qrconnect?appid=wx7c9efe7b17c8aef2&redirect_uri=http%3a%2f%2fwww.zhiliangku.com%2fcustomuser%2fweixin%2flogin&response_type=code&scope=snsapi_login&state=' +
        this.Base64.encode('/') + '#wechat_redirect';
      this.qqBase64Url =
        'https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response_type=code&client_id=101447834&redirect_uri=http%3A%2F%2Fwww.zhiliangku.com%2Fcustomuser%2Fqq%2Flogin&state=' +
        this.Base64.encode('/') + '&scope=get_user_info,get_info';
    }
  }

</script>
