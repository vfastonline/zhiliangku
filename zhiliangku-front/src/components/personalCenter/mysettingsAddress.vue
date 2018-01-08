<template>
  <div class="settings-container incenter">
    <div class="setting-item relative">
      <div class="tag font14pl3a3c50">收货地址：</div>
      <div class="set-content">
        <el-input></el-input>
      </div>
    </div>
    <div class="setting-item relative">
      <div class="tag font14pl3a3c50">收货人：</div>
      <div class="set-content">
        <el-input></el-input>
      </div>
    </div>
    <div class="setting-item relative">
      <div class="tag font14pl3a3c50">联系电话：</div>
      <div class="set-content">
        <el-input></el-input>
      </div>
    </div>
    <rcb class="setting-item"></rcb>
  </div>
</template>
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
        str1:'更改',
        str2:'更改',
        str3:'立即绑定',
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

