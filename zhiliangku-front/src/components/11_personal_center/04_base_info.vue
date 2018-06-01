<template>
  <div class="settings-container ">
    <div class="setting-item ">
      <div class="tag font1_18_6 ftj ">
        <span>昵称</span>
      </div>
      <div class="tag colon"> :</div>
      <div class="value_container">
        <el-input v-if="switch_value" class="set_value" :maxlength="20" v-model="value0"></el-input>
        <span v-else class="dib set_value info_display font1_16_6">{{value0}}</span>
      </div>
    </div>
    <div class="setting-item ">
      <div class="tag font1_18_6 ftj">
        <span>性别</span>
      </div>
      <div class="tag colon"> :</div>
      <div class="set_value">
        <span v-if="!switch_value">
          <el-radio v-model="value1" :disabled="switch_value" label="男">男</el-radio>
          <el-radio v-model="value1" :disabled="switch_value" label="女">女</el-radio>
        </span>
        <span v-else>
          <el-radio v-model="value1" label="男">男</el-radio>
          <el-radio v-model="value1" label="女">女</el-radio>
        </span>
      </div>
    </div>
    <div class="setting-item ">
      <div class="tag font1_18_6 ftj">
        <span>所在院校</span>
      </div>
      <div class="tag colon"> :</div>
      <div class="value_container">
        <el-input v-if="switch_value" class="set_value" :maxlength="20" v-model="value2"></el-input>
        <span v-else class="dib set_value info_display font1_16_6">{{value2}}</span>
      </div>
    </div>
    <div class="setting-item r ">
      <div class="tag font1_18_6 ftj">
        <span>个性签名</span>
      </div>
      <div class="tag colon"> :</div>
      <div class="value_container">
        <el-input v-if="switch_value" class="set_value" :maxlength="30" v-model="value3"></el-input>
        <span v-else class="dib set_value info_display font1_16_6">{{value3}}</span>
      </div>
    </div>
    <div class="ftr">
      <BlueButton v-if="switch_value" @click.native="submit"><span  class="font1_20_f button_content">保存</span></BlueButton>
      <BlueButton v-else @click.native="switch_value=true"><span  class="font1_20_f button_content">编辑</span></BlueButton>
    </div>
    <div></div>
  </div>
</template>
<style lang="scss" scoped>
  .button_content{
    padding: 0 30px;
  }
  .settings-container {
    width: 730px;
  }

  .setting-item {
    display: flex;
    justify-content: space-between;
    margin-bottom: 28px;
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
    flex:0 0 12px;
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
<style lang="scss">
  @import "../../assets/style/baseConstScss";

  .settings-container {
    .el-radio__inner {
      height: 24px;
      width: 24px;
      border-color: $c6;
    }

    .el-radio__inner::after {
      cursor: pointer;
      background-color: $cf;
    }

    .el-radio__inner::after {
      width: 12px;
      height: 12px;
      background-color: $cb4;
    }

    .el-radio__input.is-checked .el-radio__inner {
      border-color: $c6;
      background: white;
    }
    .value_container {
      background-color: #fff;
    }
  }
</style>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
  import Bus from '../../assets/js/02_bus'
  import {Radio} from 'element-ui'
  import Vue from 'vue'
  import BlueButton from '../../components/00_common/04_blue_button'
  Vue.use(Radio)
  export default {
    name: 'HelloWorld',
    data() {
      return {
        value0: '',
        value1: '',
        value2: '',
        value3: '',
        value4: '',
        value5: '',
        value6: '',
        mainData: '',
        switch_value: ''
      }
    },
    methods: {
      submit() {
        this.switch_value=false
        this.$post('/personal_center/personal_settings/update/basicinfo', {
          custom_user_id: localStorage.uid,
          nickname: this.value0,
          sex: this.value1,
          institutions: this.value2,
          signature: this.value3
        }).then(res => {
          if (!res.data.err) {
            Bus.$emit('refreshPersonalData')
            this.$notify({
              type: 'success',
              message: '已为您设置成功',
              offset: 100,
              duration: 3000,
              position: 'bottom-right'
            });
          }
          console.log(res)
        })
      }
    },
    created() {
      Bus.$on('havePersonalData', (res) => {
        this.mainData = res;
        this.initForm(this, this.mainData,
          ['nickname', 'sex', 'institutions', 'signature'],
          ['value0', 'value1', 'value2', 'value3']
        )
      })
      Bus.$emit('requirePersonalData')
    },
    components: {
      BlueButton:BlueButton
    }
  }

</script>

