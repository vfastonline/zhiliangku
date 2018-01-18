<template>
  <div>
    <!-- 极有可能是bug的地方：回车键的体验 -->
    <el-dialog @close="modalClose()" :show-close="false" :visible.sync="centerDialogVisible">
      <!-- 1.login模块 -->
      <div v-show="allshow.loginActive" slot="title" class="fontcenter font18plffffff marginbottom8">登陆</div>
      <el-form v-show="allshow.loginActive" :model="ruleForm1" status-icon :rules="rules2" ref="myform1">
        <el-form-item label="请输入邮箱/手机号注册" prop="age">
          <el-input v-model="ruleForm1.age"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="pass">
          <el-input type="password" v-model="ruleForm1.pass" auto-complete="off"></el-input>
        </el-form-item>
        <el-button @click="submitForm('myform1','loginFun',ruleForm1)" :class="['marginbottom8','login-commen-container-button','font20plffffff','fontcenter','incenter','pointer']">登陆</el-button>
        <div class="marginbottom24 fontcenter">
          <span class="letterspace1 font14pr23b8ff pointer" @click="changeModal('getPasswordActive')">忘记密码了</span>
        </div>
        <div class="clearfix">
          <div class="floatl font14pl5A646E">其他登陆方式:</div>
          <div class="icons floatr">
            <a :href="qqBase64Url">
              <img class="longin-bottom-icons pointer" src="../../assets/img/icons/QQ.svg" alt="">
            </a>
            <a :href="wxBase64Url">
              <img class="longin-bottom-icons pointer" src="../../assets/img/icons/wechat.svg" alt="">
            </a>

          </div>
        </div>
      </el-form>
      <div v-show="allshow.loginActive" slot="footer">
        <div @click="changeModal('logupActive')" class="login-bottom-button incenter fontcenter pointer font20plffffff">
          <span>创建账号</span>
        </div>
      </div>
      <!--2. logup模块 -->
      <div v-show="allshow.logupActive" slot="title" class="fontcenter font18plffffff marginbottom8">账号创建</div>
      <el-form v-show="allshow.logupActive" :model="ruleForm2" status-icon :rules="rules2" ref="myform2">
        <el-form-item label="请输入邮箱/手机号注册" prop="age">
          <el-input v-model="ruleForm2.age"></el-input>
        </el-form-item>
        <el-form-item label="6-16位密码（区分大小写）" prop="pass">
          <el-input type="password" v-model="ruleForm2.pass" auto-complete="off"></el-input>
        </el-form-item>
        <el-button @click="submitForm('myform2','logupType',ruleForm2,changeModal,'verifyEmailActive')" :class="['marginbottom24','login-commen-container-button','font20plffffff','fontcenter','incenter','pointer']">创建</el-button>
        <div class="clearfix">
          <div class="floatl font14pl5A646E">其他登陆方式:</div>
          <div class="icons floatr">
            <a :href="qqBase64Url">
              <img class="longin-bottom-icons pointer" src="../../assets/img/icons/QQ.svg" alt="">
            </a>
            <a :href="wxBase64Url">
              <img class="longin-bottom-icons pointer" src="../../assets/img/icons/wechat.svg" alt="">
            </a>
          </div>
        </div>
      </el-form>
      <div v-show="allshow.logupActive" slot="footer">
        <div @click="changeModal('loginActive')" class="login-bottom-button incenter fontcenter pointer font20plffffff">
          <span>已有账号，去登陆</span>
        </div>
      </div>
      <!--3. getpassword模块 -->
      <div v-show="allshow.getPasswordActive" slot="title" class="fontcenter font18plffffff marginbottom8">找回密码</div>
      <el-form v-show="allshow.getPasswordActive" :model="ruleForm3" status-icon :rules="rules2" ref="myform3">
        <el-form-item label="请输入邮箱/手机号" prop="age">
          <el-input v-on:keydown.enter="null" v-model="ruleForm3.age"></el-input>
        </el-form-item>
        <el-button @click="submitForm('myform3','getPassType',ruleForm3,changeModal,'verificationCodeActive')" :class="['marginbottom8','login-commen-container-button','font20plffffff','fontcenter','incenter','pointer']">发送验证码</el-button>
      </el-form>
      <!--4. verificationCode 验证模块 -->
      <div v-show="allshow.verificationCodeActive" slot="title" class="fontcenter font18plffffff marginbottom8">找回密码</div>
      <el-form v-show="allshow.verificationCodeActive" :model="ruleForm4" status-icon :rules="rules2" ref="myform4">
        <el-form-item label="请输入短信验证码">
          <el-input v-model="ruleForm4.age"></el-input>
        </el-form-item>
        <el-form-item label="输入新的密码" prop="pass">
          <el-input type="password" v-model="ruleForm4.pass" auto-complete="off"></el-input>
        </el-form-item>
        <el-button @click="submitForm('myform4','modifyPass',ruleForm4,ruleForm3)" :class="['marginbottom8','login-commen-container-button','font20plffffff','fontcenter','incenter','pointer']">提交</el-button>
        <div class="incenter fontcenter">
          <span @click="changeModal('getPasswordActive')" class="font14pl7c7e8c pointer">
            返回修改邮箱手机号
          </span>
        </div>
      </el-form>
      <!--5. verifyCode 创建账号-->
      <div v-show="allshow.verifyCodeActive" slot="title" class="fontcenter font18plffffff marginbottom8">账号创建</div>
      <el-form v-show="allshow.verifyCodeActive" :model="ruleForm5" status-icon :rules="rules2" ref="myform5">
        <el-form-item label="请输入短信验证码">
          <el-input v-model="ruleForm5.age"></el-input>
        </el-form-item>
        <el-button @click="verifyPhoneCode()" :class="['marginbottom8','login-commen-container-button','font20plffffff','fontcenter','incenter','pointer']">登陆</el-button>
        <div class="incenter fontcenter">
          <span @click="changeModal('logupActive')" class="font14pl7c7e8c pointer">
            返回修改手机号
          </span>
        </div>
      </el-form>
      <!--6. success模块 -->
      <div v-show="allshow.verifyEmailActive" slot="title" class="fontcenter font18plffffff marginbottom8">账号创建</div>
      <div v-show="allshow.verifyEmailActive" class="logup-success-body">
        <img class="marginbottom24 incenter block" src="../../assets/img/icons/注册弹窗 邮箱激活弹窗_对勾.svg" alt="">
        <div class="fontcenter marginbottom8">账号创建成功</div>
        <!-- <img class="marginbottom24 incenter " src="../../assets/img/icons/找回密码弹窗_邮件找回_邮件.svg" alt=""> -->
        <div class="fontcenter marginbottom24">邮件已发至
          <span class="font14pr23b8ff">{{ruleForm2.age}}</span>
        </div>
      </div>
      <el-button @click="goEmailHome(ruleForm2.age)" v-show="allshow.verifyEmailActive" :class="['login-commen-container-button','font20plffffff','fontcenter','incenter','pointer']">去邮箱验证</el-button>
      <!--7. success 模块 -->
      <div v-show="allshow.goEmailActive" slot="title" class="fontcenter font18plffffff marginbottom8">账号创建</div>
      <div v-show="allshow.goEmailActive" class="logup-success-body">
        <img class="marginbottom24 incenter block" src="../../assets/img/icons/找回密码弹窗_邮件找回_邮件.svg" alt="">
        <div class="fontcenter marginbottom24">邮件已发至
          <!-- 这里确实是有bug存在的，需要修改 -->
          <span class="font14pr23b8ff">{{ruleForm3.age}}</span>
        </div>
      </div>
      <el-button @click="goEmailHome(ruleForm3.age)" v-show="allshow.goEmailActive" :class="['login-commen-container-button','font20plffffff','fontcenter','incenter','pointer']">去邮箱</el-button>
      <!-- 8.再次验证邮箱模块 -->
      <div v-show="allshow.emailVerifyAginActive" slot="title" class="fontcenter font18plffffff marginbottom8">账号创建</div>
      <div v-show="allshow.emailVerifyAginActive" class="logup-success-body">
        <img class="marginbottom24 incenter block" src="../../assets/img/icons/Email叹号.svg" alt="">
        <div class="marginbottom8 fontcenter font20pl3a3c50">邮箱未激活</div>
        <div class="marginbottom24 fontcenter font14pl5A646E">请尽快前往激活邮箱</div>
      </div>
      <div v-show="allshow.emailVerifyAginActive" class="login-middle-button-container incenter">
        <el-button @click="goEmailHome(keyEmail)" :class="['login-middle-button','font20plffffff','fontcenter','incenter','pointer']">去邮箱验证</el-button>
        <el-button @click="getEmailVerify(keyEmail)" :class="['login-middle-button','font20plffffff','fontcenter','incenter','pointer','floatr']">发送验证码</el-button>
      </div>
    </el-dialog>
  </div>
</template>
<script>
  var Base64 = require('js-base64').Base64;
  import Bus from '../../assets/js/bus'
  export default {
    name: 'HelloWorld',
    data() {
      // console.log(this)
      var usernameType = {
        phone: false,
        email: false
      };
      var checkAge = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('邮箱/手机号不能为空'));
        }
        setTimeout(() => {
          var phonecheck = /^1[3|4|5|7|8][0-9]{9}$/;
          var emailcheck = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
          usernameType.phone = false;
          usernameType.email = false;
          if (phonecheck.test(value)) {
            usernameType.phone = true;
            callback()
          }
          if (emailcheck.test(value)) {
            usernameType.email = true;;
            callback()
          }
          callback(new Error('请输入正确的邮箱/手机号'))
        }, 100);
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
      return {
        qqBase64Url: '',
        wxBase64Url: '',
        Base64: Base64,
        usernameType: usernameType,
        centerDialogVisible: false,
        dynamicValidateForm: {
          email: ''
        },
        ruleForm1: {
          age: '',
          pass: ''
        },
        ruleForm2: {
          age: '',
          pass: ''
        },
        ruleForm3: {
          age: '',
          pass: ''
        },
        ruleForm4: {
          age: '',
          pass: ''
        },
        ruleForm5: {
          age: '',
          pass: ''
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
        },
        allshow: {
          loginActive: false,
          logupActive: false,
          getPasswordActive: false,
          verificationCodeActive: false,
          verifyCodeActive: false,
          verifyEmailActive: false,
          goEmailActive: false,
          emailVerifyAginActive: false
        },
        //目标邮件地址
        keyEmail: ''
      }
    },
    methods: {
      getEmailVerify() {
        document.cookie = "xiejiabing=xiejiabing"
        this.$post('/customuser/send_activation_mail', {
          email: this.keyEmail
        }).then(res => {
          if (!res.data.err) {
            this.$notify({
              type: 'success',
              message: res.data.msg,
              offset: 100,
              duration: 3000,
              position: 'bottom-right'
            });
          }
        })
      },
      modalClose() {
        this.closeAll()
      },
      changeModal(key) {
        this.closeAll();
        this.allshow[key] = true;
      },
      closeAll() {
        for (var k in this.allshow) {
          this.allshow[k] = false;
        }
      },
      verifyPhoneCode() {
        var data = this.changeKeys(this.ruleForm2);
        data.verify_code = this.ruleForm5.age;
        this.$post('/customuser/register', data).then(res => {
          if (res) {
            if (res.data.msg == 'success') {
              debugger
              this.loginFun(this.ruleForm2)
              this.centerDialogVisible = false;
            }
          }
          console.log(res)
        })
      },
      submitForm(formName, funkey, data, callbackfun, param) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            if (funkey) {
              this[funkey](data, callbackfun, param)
            }
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      changeKeys(data, brr) {
        var keyarr = ['username', 'password'];
        if (brr) {
          keyarr = brr
        }
        var targetData = this.deepCopy(data);
        var newData = this.$fn.exchangeObjectKey(targetData, ['age', 'pass'], keyarr);
        var arr = ['age', 'pass'];
        for (var i = 0; i < arr.length; i++) {
          if (newData[arr[i]]) {
            delete newData[arr[i]];
          }
        }
        return newData;
      },
      haveKeyValue(key, data, datakey) {
        this[key] = data[datakey];
      },
      loginFun(data) {
        this.haveKeyValue('keyEmail', data, 'age')
        debugger
        var obj = this.changeKeys(data)
        this.$post('/customuser/login', this.changeKeys(data)).then(res => {
          if (!res.data.err) {
            if (res.data.msg = 'success') this.centerDialogVisible = false;
            //remenber user info
            for (var k in res.data.data.user) {
              localStorage[k] = res.data.data.user[k]
            }
            // console.log(res.data.data)
            // 由于data可能来自别的面页，而且别的页面有着不同的需求，那么此处应该写到loginfun函数之外，不过目前先迁就一次
            if (data.referrer) {
              this.goreferre()
              return
            }
            this.$parent.$emit('login')
          }
          console.log(res)
        })
      },
      goreferre() {
        window.location.href = document.referrer
      },
      logupFun(data, callback, param) {
        this.$post('/customuser/register', this.changeKeys(data)).then(res => {
          if (callback && !res.data.err) {
            this.$notify({
              type: 'success',
              message: '验证码已成功发送',
              offset: 100,
              duration: 3000,
              position: 'bottom-right'
            })
            callback(param)
          }
          console.log(res)
        })
      },
      getCode(data, callbackfun, param) {
        this.$post('/customuser/send_sms', this.changeKeys(data, ['phone', 'password'])).then(
          res => {
            console.log(res)
            if (callbackfun && !res.data.err) {
              callbackfun(param)
            }
          })
      },
      modifyPass(form4, form3) {
        var mainData = this.changeKeys(form4, ['verify_code', 'new_password']);
        mainData.phone = form3.age;
        this.$post('/customuser/retrieve_password_by_phone', mainData).then(res => {
          if (!res.data.err) {
            this.$notify({
              type: 'success',
              message: res.data.msg,
              offset: 100,
              duration: 3000,
              position: 'bottom-right'
            });
          }
          //此处是临时处理
          this.closeAll();
          console.log(res)
        })
      },
      getPassType(data, callbackfun, param) {
        this.haveKeyValue('keyEmail', data, 'age')
        if (this.usernameType.phone) {
          this.getCode(data, callbackfun, param)
        }
        if (this.usernameType.email) {
          this.$post('/customuser/send_email_retrieve_password', {
            email: this.keyEmail
          }).then(res => {
            if (!res.data.err) {
              callbackfun('goEmailActive')
            }
          })

        }
      },
      logupType(data, callbackfun) {
        this.haveKeyValue('keyEmail', data, 'age');
        if (this.usernameType.phone) {
          this.getCode(data, callbackfun, 'verifyCodeActive')
        }
        if (this.usernameType.email) {
          this.logupFun(data, callbackfun, 'verifyEmailActive');
          // 此处是直接进行了跳转，理论上讲，是不合适的。
        }
      },

      goEmailHome(email) {
        var hash = {
          'qq.com': 'http://mail.qq.com',
          'gmail.com': 'http://mail.google.com',
          'sina.com': 'http://mail.sina.com.cn',
          '163.com': 'http://mail.163.com',
          '126.com': 'http://mail.126.com',
          'yeah.net': 'http://www.yeah.net/',
          'sohu.com': 'http://mail.sohu.com/',
          'tom.com': 'http://mail.tom.com/',
          'sogou.com': 'http://mail.sogou.com/',
          '139.com': 'http://mail.10086.cn/',
          'hotmail.com': 'http://www.hotmail.com',
          'live.com': 'http://login.live.com/',
          'live.cn': 'http://login.live.cn/',
          'live.com.cn': 'http://login.live.com.cn',
          '189.com': 'http://webmail16.189.cn/webmail/',
          'yahoo.com.cn': 'http://mail.cn.yahoo.com/',
          'yahoo.cn': 'http://mail.cn.yahoo.com/',
          'eyou.com': 'http://www.eyou.com/',
          '21cn.com': 'http://mail.21cn.com/',
          '188.com': 'http://www.188.com/',
          'foxmail.coom': 'http://www.foxmail.com'
        };
        console.log(email)
        if (hash[email.split('@')[1]]) {
          window.open(hash[email.split('@')[1]])
          return
        } else {
          console.log('未知邮箱')
        }
      }
    },
    created() {
      Bus.$on('forgetPassword', (res) => {
        this.centerDialogVisible = true;
        this.allshow['getPasswordActive'] = true;
        if (res) {
          this.form3.age = res
        }
      })
      Bus.$on('loginPagerLogin', (res) => {
        this.loginFun(res)
      })
      this.$on('open', function (key) {
        this.centerDialogVisible = true;
        this.allshow[key] = true;
      })
      this.$on('noActive', function (name) {
        console.log('noActive')
        console.log(name)
        this.changeModal(name)
      })
      this.$on('logupTologin', function () {
        this.ruleForm1 = this.ruleForm2
      })
      this.wxBase64Url =
        'https://open.weixin.qq.com/connect/qrconnect?appid=wx7c9efe7b17c8aef2&redirect_uri=http%3a%2f%2fwww.zhiliangku.com%2fcustomuser%2fweixin%2flogin&response_type=code&scope=snsapi_login&state=' +
        this.Base64.encode(window.location.pathname) + '#wechat_redirect';
      this.qqBase64Url =
        'https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response_type=code&client_id=101447834&redirect_uri=http%3A%2F%2Fwww.zhiliangku.com%2Fcustomuser%2Fqq%2Flogin&state=' +
        this.Base64.encode(window.location.pathname) + '&scope=get_user_info,get_info';
      // 我的实现方式应该是,一个大组件,大组件是一直显示的，但是可以通过改变里面的参数来改变其显示的各种小组件
    },
    mounted() {

      // console.log(this)
      // console.log(this.$ajax)
      // console.log(this.$echarts)
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .login-middle-button-container {
    width: 340px;
    margin-left: -20px;
  }

  .longin-bottom-icons {
    margin-right: 24px;
  }

  .login-commen-container-button {
    width: 300px;
    background: #23B8FF 100%
  }

  .login-middle-button {
    width: 164px;
    background: #23B8FF 100%
  }

  .login-bottom-button {
    margin-top: 8px;
    width: 300px;
    height: 40px;
    border: 2px solid #ffffff;
    line-height: 40px;
  }

  .logup-success-body {
    padding-top: 70px;
  }

</style>
