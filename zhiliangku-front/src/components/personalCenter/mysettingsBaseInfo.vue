<template>
  <div class="settings-container incenter">
    <div class="setting-item relative">
      <div class="tag font14pl3a3c50">昵称：</div>
      <div class="set-content">
        <el-input></el-input>
      </div>
    </div>
    <div class="setting-item relative">
      <div class="tag font14pl3a3c50">性别：</div>
      <div class="set-content">
        <el-radio v-model="value0" label="男" >男</el-radio>
        <el-radio v-model="value0" label="女">女</el-radio>
      </div>
    </div>
    <div class="setting-item relative">
      <div class="tag font14pl3a3c50">个性签名：</div>
      <div class="set-content">
        <el-input></el-input>
      </div>
    </div>
    <rcb class="setting-item"></rcb>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
import rcb from './resumeContentButton'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        value0:'',
        value1:'',
        value2:'',
        value3:'',
        value4:'',
        value5:'',
        value6:'',
      }
    },
    components:{
      rcb:rcb
    }
  }
</script>
<style lang='scss' scoped>
@import '../../style/scss/components/mysettings.scss';
</style>

