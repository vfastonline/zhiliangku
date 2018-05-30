<template>
  <div class="settings-container incenter">
    <div class="setting-item relative">
      <div class="tag font14pl3a3c50">旧密码：</div>
      <div class="set-content">
        <el-input v-model="value0"></el-input>
      </div>
    </div>
    <div class="setting-item relative">
      <div class="tag font14pl3a3c50">新密码：</div>
      <div class="set-content">
        <el-input v-model="value1"></el-input>
      </div>
    </div>
    <!-- <div class="setting-item relative">
      <div class="tag font14pl3a3c50">再次确认：</div>
      <div class="set-content">
        <el-input v-model="value2"></el-input>
      </div>
    </div> -->
    <rcb @submit="submit(orgnizeData())" :layer="['submit']"></rcb>
  </div>
</template>
<script>
  import rcb from './resumeContentButton'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        value0: '',
        value1: '',
        value2: '',
      }
    },
    methods: {
      orgnizeData() {
        if (!this.value1) {
          this.$notify({
            type: 'warning',
            message: '请您输入新密码',
            offset: 100,
            duration: 3000,
            position: 'bottom-right'
          });
          return
        }
        if (this.value0.length < 6 || this.value0.length > 16) {
          this.$notify({
            type: 'warning',
            message: '请您输入6-16位密码（区分大小写）',
            offset: 100,
            duration: 3000,
            position: 'bottom-right'
          });
          return
        }
        var obj = {
          custom_user_id: localStorage.uid,
          old_password: this.value0,
          password: this.value1
        }
        return obj
      },
      reset() {
        this.value0 = '',
          this.value1 = ''
      },
      submit(data) {
        if(!data)return;
        this.$post('/personal_center/personal_settings/change/password', data).then(res => {
          if (!res.data.err) {
            this.$notify({
              type: 'success',
              message: res.data.msg,
              offset: 100,
              duration: 3000,
              position: 'bottom-right'
            });
            this.reset();
          }
        })
      }
    },
    components: {
      rcb: rcb
    }
  }

</script>
<style lang='scss' scoped>
  @import './style/04_my_setting.scss';

</style>
