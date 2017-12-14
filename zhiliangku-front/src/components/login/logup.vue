<template>
  <div>
    <el-button type="text" @click="centerDialogVisible = true">点击打开 Dialog</el-button>
    <el-dialog :show-close="false" :visible.sync="centerDialogVisible">
      <div slot="title" class="fontcenter font18plffffff marginbottom8">账号创建</div>
     <el-form :model="ruleForm2" status-icon :rules="rules2" ref="myform">
        <el-form-item label="请输入邮箱/手机号注册" prop="age">
          <el-input v-model="ruleForm2.age"></el-input>
        </el-form-item>
        <el-form-item label="6-16位密码（区分大小写）" prop="pass">
          <el-input type="password" v-model="ruleForm2.pass" auto-complete="off"></el-input>
        </el-form-item>
        <el-button :class="['marginbottom8','login-commen-container-button','font20plffffff','fontcenter','incenter','pointer']">登陆</el-button>
        <div class="clearfix">
          <div class="floatl font14pl5A646E">其他登陆方式:</div>
          <div class="icons floatr">
            <img class="longin-bottom-icons pointer" src="../../assets/img/icons/QQ.svg" alt="">
            <img class="longin-bottom-icons pointer" src="../../assets/img/icons/wechat.svg" alt="">
            <img class="pointer" src="../../assets/img/icons/weibo.svg" alt="">
          </div>
        </div>
      </el-form>
      <div slot="footer" class="login-bottom-button incenter fontcenter pointer font20plffffff">已有账号，去登陆</div>
    </el-dialog>

  </div>
</template>
<script>
  export default {
    name: 'HelloWorld',
    data() {
      var checkAge = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('邮箱/手机号不能为空'));
        }
        setTimeout(() => {
          var phonecheck = /^1[3|4|5|7|8][0-9]{9}$/;
          var emailcheck = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
          if (phonecheck.test(value) || emailcheck.test(value)) {
            callback()
          } else {
            callback(new Error('请输入正确的邮箱/手机号'))
          }
        }, 300);
      };
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        }
        if (value.length < 7 || value.length > 16) {
          callback(new Error('请输入6-16位密码（区分大小写）'))
        }
        callback()
      };
      return {
        centerDialogVisible: false,
        dynamicValidateForm: {
          email: ''
        },
        ruleForm2: {
          age: '',
          pass:''
        },
        rules2: {
          age: [{
            validator: checkAge,
            trigger: 'blur'
          }],
           pass: [{
            validator: validatePass,
            trigger: 'blur'
          }],
        }
      }
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .longin-bottom-icons {
    margin-right: 24px;
  }

  .login-bottom-button {
    margin-top: 8px;
    width: 300px;
    height: 40px;
    border: 2px solid #ffffff;
    line-height: 40px;
  }

</style>
