<template>
  <div class="settings-container incenter">
    <div class="setting-item relative">
      <div class="tag font14pl3a3c50">邮箱：</div>
      <div class="set-content">
        <div class="sc-info-li">wangxinmu@qq.com
          <span class="font14pr424242"> </span>
        </div>
        <span @click="changeShow('email','修改邮箱')" class="bind-button font14pr424242 pointer">{{str1}}</span>
      </div>
    </div>
    <div class="setting-item relative">
      <div class="tag font14pl3a3c50">手机号：</div>
      <div class="set-content">
        <div class="sc-info-li">wangxinmu@qq.com
          <span class="font14pr424242"> </span>
        </div>
        <span @click="changeShow('phone','修改手机号')" class="bind-button font14pr424242 pointer">{{str1}}</span>
      </div>
    </div>
    <div class="setting-item relative">
      <div class="tag font14pl3a3c50">微信：</div>
      <div class="set-content">
        <div class="sc-info-li">
          <span class="font14pr424242"> 可用于直接登陆，与内容分享</span>
        </div>
        <span class="bind-button font14pr424242 pointer">{{str1}}</span>
      </div>
    </div>
    <el-dialog :width="'650px'" :title="dialogTitle" :visible.sync="show">
      <div class="dialog-li incenter emial-container relative">
        <div class="input-li relative">
          <div class="tags">邮箱地址：</div>
          <el-form :model="emailform" :rules="emailRule">
            <el-form-item prop="email">
              <el-input v-model="emailform.email" auto-complete="off"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </div>
      <div class="dialog-li incenter emial-container relative">
        <div class="input-li relative">
          <div class="tags">手机号：</div>
          <el-form :model="phoneform" :rules="phoneRule">
            <el-form-item prop="phone">
              <el-input v-model="phoneform.phone" auto-complete="off"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </div>
      <div class="dialog-li incenter emial-container relative">
        <div class="input-li relative">
          <div class="tags">短信验证码：</div>
          <el-form :model="phoneform" :rules="phoneRule">
            <el-form-item prop="phone">
              <el-input v-model="phoneform.phone" auto-complete="off"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </div>
      <rcb :styleData="buttonContainerStyle" class="footer-button-group" slot="footer"></rcb>
    </el-dialog>
  </div>
</template>
<script>
  import rcb from './resumeContentButton'
  export default {
    name: 'HelloWorld',
    data() {
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
        callback(new Error('请输入正确的邮箱'))
      }
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        }
        if (value.length < 6 || value.length > 16) {
          callback(new Error('请输入6-16位密码（区分大小写）'))
        }
        callback()
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
        phoneform:{
          phone:''
        },
        phoneRule:{
          phone:[{
            validator:checkPhone,
            trigger:'blur'
          }]
        },
        show: false,
        dialogTitle: '',
        dialogContent: '',
        buttonContainerStyle: {
          'text-align': 'center'
        },
        ruleForm1: {
          age: '',
          pass: ''
        },
        ruleForm2: {
          age: '',
          pass: ''
        },
        value0: '',
        value1: '',
        value2: '',
        value3: '',
        value4: '',
        value5: '',
        value6: '',
        str1: '更改',
        str2: '更改',
        str3: '立即绑定',
      }
    },
    methods: {
      changeShow(type, str) {
        this.dialogTitle = str;
        this.show = !this.show;
        this.dialogContent = type;
      }
    },
    components: {
      rcb: rcb
    }
  }

</script>
<style lang="scss">
  .sc-info-li {
    background: white;
    line-height: 42px;
    height: 42px;
    padding: 0 100px 0 32px;
  }

  .dialog-li {
    width: 570px;
  }

  .input-li {
    width: 473px;
    margin-left: 94px;
    .tags{
      position: absolute;
      width:85px;
      top:50%;
      text-align: right;
      left:-100px;
      transform: translate(0,-50%)
    }
  }

</style>
<style lang='scss' scoped>
  @import '../../style/scss/components/mysettings.scss';

</style>
