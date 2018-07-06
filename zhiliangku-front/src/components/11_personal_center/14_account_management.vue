<template>
  <div class="settings-container ">
    <div class="setting-item ">
      <div class="tag font1_18_6 ftj ">
        <span>手机号码</span>
      </div>
      <div class="tag colon"> :</div>
      <div class="value_container">
        <span class="dib set_value info_display font1_16_6">{{base_info.phone}}</span>
      </div>
    </div>
    <div class="setting-item ">
      <div class="tag font1_18_6 ftj ">
        <span>密码</span>
      </div>
      <div class="tag colon"> :</div>
      <div class="value_container">
        <el-form class="set_value form_wrap" :model="form_data"
                 status-icon
                 :rules="rules"
                 ref="form_el"
                 :disabled="!switch_value"
        >
          <el-form-item prop="password">
            <el-input :placeholder="'请输入密码'"
                      type="password"
                      v-model="form_data.password"
                      auto-complete="off">

            </el-input>
          </el-form-item>
        </el-form>
        <!--<span v-else class="dib set_value info_display font1_16_6">{{form_data}}</span>-->
      </div>
    </div>
    <div class="setting-item ">
      <div class="tag font1_18_6 ftj ">
        <span>新密码</span>
      </div>
      <div class="tag colon"> :</div>
      <div class="value_container">
        <el-form class="set_value form_wrap" :model="form_data"
                 status-icon
                 :rules="rules"
                 ref="form_el"
                 :disabled="!switch_value"
        >
          <el-form-item prop="password_new">
            <el-input :placeholder="'请输入新密码'"
                      type="password"
                      v-model="form_data.password_new"
                      auto-complete="off">

            </el-input>
          </el-form-item>
        </el-form>
      </div>
    </div>
    <div class="ftr">
      <BlueButton v-if="switch_value" @click.native="submit"><span class="font1_20_f button_content">保存</span>
      </BlueButton>
      <BlueButton v-else @click.native="switch_value=true"><span class="font1_20_f button_content">编辑</span>
      </BlueButton>
    </div>
  </div>
</template>
<style lang="scss">
  @import "../../assets/style/baseConstScss";

</style>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
  import Bus from '../../assets/js/02_bus'
  import {Form, FormItem, Input} from 'element-ui'
  import Vue from 'vue'
  import BlueButton from '../../components/00_common/04_blue_button'

  Vue.use(Form)
  Vue.use(FormItem)
  Vue.use(Input)
  export default {
    name: 'HelloWorld',
    data() {

      // let validatePass2 = (rule, value, callback) => {
      //   if (value === '') {
      //     callback(new Error('请再次输入密码'))
      //   } else if (value !== this.form_data.password) {
      //     callback(new Error('两次输入密码不一致!'))
      //   } else {
      //     callback()
      //   }
      // }
      let validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'))
        }
        if (value.length < 6 || value.length > 16) {
          callback(new Error('请输入6-16位密码（区分大小写）'))
        }
        callback()
      }
      return {
        value0: '',
        mainData: '',
        switch_value: '',
        form_data: {
          password_new: '',
          password: '',
          password_repeat: '',
          code: ''
        },
        rules: {
          password_new: [{validator: validatePass, trigger: 'blur'}],
          password: [{validator: validatePass, trigger: 'blur'}],
          // password_repeat: [{validator: validatePass2, trigger: 'blur'}],
        },
        base_info: {}
      }
    },
    methods: {
      submit() {
        let obj = {
          old_password: this.form_data.password,
          password: this.form_data.password_new
        }
        this.$post('/personal_center/personal_settings/change/password', obj).then(res => {
          if (!res.data.err) {
            Bus.$emit('refreshPersonalData')
            this.$notify({
              type: 'success',
              message: '已为您设置成功',
              offset: 100,
              duration: 3000,
              position: 'bottom-right'
            })
            this.switch_value = false
          }
        })
      },
      get_base_info() {
        this.$get('/personal_center/basic/info').then(res => {
          this.base_info = res.data.data
        })
      }
    },
    created() {
      this.get_base_info()
      Bus.$on('havePersonalData', (res) => {
        this.mainData = res
        this.initForm(this, this.mainData,
          ['nickname', 'sex', 'institutions', 'signature'],
          ['value0', 'value1', 'value2', 'value3']
        )
      })
      Bus.$emit('requirePersonalData')
    },
    components: {
      BlueButton: BlueButton
    }
  }

</script>

<style lang="scss" scoped>
  .button_content {
    padding: 0 30px;
  }

  .settings-container {
    width: 730px;
  }

  .setting-item {
    display: flex;
    justify-content: space-between;
    margin-bottom: 28px;
    height: 40px;
  }

  .tag {
    width: 100px;
    flex: 0 0 100px;
    line-height: 40px;
    overflow: hidden;
    height: 40px;
  }

  .colon {
    width: 38px;
    flex: 0 0 12px;
  }

  .set_value {
    box-sizing: border-box;
    width: 600px;
    flex: 0 0 600px;
    line-height: 40px;
  }

  .info_display {
    padding: 0 15px;
  }
</style>
