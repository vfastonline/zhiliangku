<template>
  <div class="settings-container ">
    <div class="setting-item ">
      <div class="tag font1_18_6 ftj ">
        <span>手机号码</span>
      </div>
      <div class="tag colon"> :</div>
      <div class="value_container">
        <span class="dib set_value info_display font1_16_6">{{mainData.phone}}</span>
      </div>
    </div>
    <div class="setting-item ">
      <div class="tag font1_18_6 ftj ">
        <span>真实姓名</span>
      </div>
      <div class="tag colon"> :</div>
      <div class="value_container">
        <el-input v-if="switch_value" class="set_value" :maxlength="5" placeholder="五个汉字以内"
                  v-model="value0"></el-input>
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
          <el-radio v-model="value1" :disabled="!switch_value" label="男">男</el-radio>
          <el-radio v-model="value1" :disabled="!switch_value" label="女">女</el-radio>
        </span>
        <span v-else>
          <el-radio v-model="value1" label="男">男</el-radio>
          <el-radio v-model="value1" label="女">女</el-radio>
        </span>
      </div>
    </div>
    <div class="setting-item ">
      <div class="tag font1_18_6 ftj ">
        <span>出生年月</span>
      </div>
      <div class="tag colon"> :</div>
      <div class="value_container ">
        <el-date-picker
          class="set_value"
          v-if="switch_value"
          v-model="value2"
          @change="verify_value2"
          format="yyyy-MM-dd"
          type="date"
          placeholder="选择日期">
        </el-date-picker>
        <span v-else class="dib set_value info_display font1_16_6">{{value2|moment('YYYY-MM-DD')}}</span>
      </div>
    </div>
    <div class="setting-item ">
      <div class="tag font1_18_6 ftj">
        <span>所在院校</span>
      </div>
      <div class="tag colon"> :</div>
      <div class="value_container">
        <el-input v-if="switch_value" class="set_value" :maxlength="20" placeholder="十个汉字以内"
                  v-model="value3"></el-input>
        <span v-else class="dib set_value info_display font1_16_6">{{value3}}</span>
      </div>
    </div>
    <div class="setting-item ">
      <div class="tag font1_18_6 ftj">
        <span>所在班级</span>
      </div>
      <div class="tag colon"> :</div>
      <div class="value_container">
        <el-input v-if="switch_value" class="set_value" :maxlength="20" placeholder="十个汉字以内"
                  v-model="value4"></el-input>
        <span v-else class="dib set_value info_display font1_16_6">{{value4}}</span>
      </div>
    </div>
    <div class="setting-item ">
      <div class="tag font1_18_6 ftj">
        <span>计算机相关专业</span>
      </div>
      <div class="tag colon"> :</div>
      <div class="set_value">
        <span v-if="!switch_value">
          <el-radio v-model="value5" :disabled="!switch_value" :label="true">是</el-radio>
          <el-radio v-model="value5" :disabled="!switch_value" :label="false">否</el-radio>
        </span>
        <span v-else>
          <el-radio v-model="value5" :label="true">是</el-radio>
          <el-radio v-model="value5" :label="false">否</el-radio>
        </span>
      </div>
    </div>
    <div class="setting-item ">
      <div class="tag font1_18_6 ftj">
        <span>在校情况</span>
      </div>
      <div class="tag colon"> :</div>
      <div class="set_value">
        <span v-if="!switch_value">
          <el-radio v-model="value6" :disabled="!switch_value" :label="true">在读</el-radio>
          <el-radio v-model="value6" :disabled="!switch_value" :label="false">毕业</el-radio>
        </span>
        <span v-else>
          <el-radio v-model="value6" :label="true">在读</el-radio>
          <el-radio v-model="value6" :label="false">毕业</el-radio>
        </span>
      </div>
    </div>
    <div class="setting-item ">
      <div class="tag font1_18_6 ftj ">
        <span>学历</span>
      </div>
      <div class="tag colon"> :</div>
      <div class="value_container">
        <el-select class="set_value" v-if="switch_value" v-model="value7" placeholder="请选择学历">
          <el-option
            v-for="item in options"
            :key="item"
            :label="item"
            :value="item">
          </el-option>
        </el-select>
        <span v-else class="dib set_value info_display font1_16_6">{{value7}}</span>
      </div>
    </div>
    <div class="setting-item r ">
      <div class="tag font1_18_6 ftj">
        <span>个性签名</span>
      </div>
      <div class="tag colon"> :</div>
      <div class="value_container">
        <el-input v-if="switch_value" class="set_value" :maxlength="30" v-model="value8"></el-input>
        <span v-else class="dib set_value info_display font1_16_6">{{value8}}</span>
      </div>
    </div>
    <div class="ftr">
      <BlueButton v-if="switch_value" @click.native="submit"><span
        class="font1_20_f button_content">保存</span>
      </BlueButton>
      <BlueButton v-else @click.native="switch_value=true"><span class="font1_20_f button_content">编辑</span>
      </BlueButton>
    </div>
    <div></div>
  </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
  import Bus from '../../assets/js/02_bus'
  import {Radio, DatePicker, Select} from 'element-ui'
  import Vue from 'vue'
  import BlueButton from '../../components/00_common/04_blue_button'

  Vue.use(require('vue-moment'))
  Vue.use(Radio)
  Vue.use(DatePicker)
  Vue.use(Select)
  export default {
    name: 'HelloWorld',
    data() {
      return {
        options: ['小学', '初中', '高中', '大专', '本科', '研究生', '博士'],
        value0: '',
        value1: '',
        value2: '',
        value3: '',
        value4: '',
        value5: '',
        value6: '',
        value7: '',
        value8: '',
        mainData: '',
        switch_value: ''
      }
    },
    methods: {
      //应该把所有涉及到稍微复杂的表单的分配以及组织数据方法集合封装。但是目前没有这么去做，而且最优的解决方案是利用render函数。
      submit() {
        if(!this.verify_value2()){return}
        let arr = ['nickname', 'sex', 'birthday', 'institutions', 'class_s', 'is_computer', 'is_graduate', 'education', 'signature']
        let obj = this.organize_data(arr, 8)
        this.$post('/personal_center/personal_settings/update/basicinfo', obj).then(res => {
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
      }
      ,
      organize_data(arr, num) {
        let obj = {}
        for (let i = 0; i < num; i++) {
          obj[arr[i]] = this['value' + i]
        }
        return obj
      },
      verify_value2() {
        let value2=this.value2
        let now = new Date().getFullYear(), b_year = value2.getFullYear()
        if ((1 <= now - b_year) && (now - b_year <= 100)) {
          return true
        }
        this.$notify({
          type: 'warning',
          message: '请设置年龄在1-100之间',
          offset: 100,
          duration: 3000,
          position: 'bottom-right'
        })
        return false
      }
    }
    ,
    created() {
      //触发地点在01_user_info
      Bus.$on('havePersonalData', (res) => {
        this.mainData = res
        this.initForm(this, this.mainData,
          ['nickname', 'sex', 'birthday', 'institutions', 'class_s', 'is_computer', 'is_graduate', 'education', 'signature'],
          ['value0', 'value1', 'value2', 'value3', 'value4', 'value5', 'value6', 'value7', 'value8']
        )
        console.log(this)
      })
      Bus.$emit('requirePersonalData')
    }
    ,
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
    width: 600px !important;
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
