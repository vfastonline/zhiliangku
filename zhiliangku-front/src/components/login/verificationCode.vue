<template>
  <div>
    <el-button type="text" @click="centerDialogVisible = true">点击打开 Dialog</el-button>
    <el-dialog :show-close="false" :visible.sync="centerDialogVisible">
      <div slot="title" class="fontcenter font18plffffff marginbottom8">找回密码</div>
     <el-form :model="ruleForm2" status-icon :rules="rules2" ref="myform">
        <el-form-item label="请输入短信验证码" prop="age">
          <el-input v-model="ruleForm2.age"></el-input>
        </el-form-item>
        <el-form-item label="输入新的密码" prop="pass">
          <el-input type="password" v-model="ruleForm2.pass" auto-complete="off"></el-input>
        </el-form-item>
        <el-button :class="['marginbottom8','login-commen-container-button','font20plffffff','fontcenter','incenter','pointer']">登陆</el-button>
        <div class="incenter ">
          <span class="font14pl7c7e8c">
            返回修改邮箱手机号
          </span>
        </div>
      </el-form>
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

