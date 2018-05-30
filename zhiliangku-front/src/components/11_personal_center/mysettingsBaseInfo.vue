<template>
  <div class="settings-container hc">
    <div class="setting-item r">
      <div class="tag font14pl3a3c50">昵称：</div>
      <div class="set-content">
        <el-input :maxlength="20" v-model="value0"></el-input>
      </div>
    </div>
    <div class="setting-item r">
      <div class="tag font14pl3a3c50">性别：</div>
      <div class="set-content">
        <el-radio v-model="value1" label="男">男</el-radio>
        <el-radio v-model="value1" label="女">女</el-radio>
      </div>
    </div>
    <div class="setting-item r">
      <div class="tag font14pl3a3c50">个性签名：</div>
      <div class="set-content">
        <el-input type='textarea' :maxlength="120" v-model="value2"></el-input>
      </div>
    </div>
    <rcb @submit="submit" :layer="['submit'] "></rcb>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
  import Bus from '../../assets/js/02_bus'
  import rcb from './resumeContentButton'
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
        mainData: ''
      }
    },
    methods: {
      submit() {
        this.$post('/personal_center/personal_settings/update/basicinfo', {
          custom_user_id: localStorage.uid,
          nickname: this.value0,
          sex: this.value1,
          signature: this.value2
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
        this.initForm(this, this.mainData, ['nickname', 'sex',
          'signature'
        ], [
          'value0', 'value1', 'value2'
        ])
      })
      Bus.$emit('requirePersonalData')
    },
    components: {
      rcb: rcb
    }
  }

</script>
<style lang='scss' scoped>
  @import './style/04_my_setting.scss';

</style>
