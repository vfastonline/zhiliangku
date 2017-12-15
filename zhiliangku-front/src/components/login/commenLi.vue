<template>
  <div class="login-comen-li">
    <div class="font14pl5A646E login-commen-li-tag">{{mainData.tag}}</div>
    <div>
      <el-input :type="mainData.type?mainData.type:'text'" placeholder="请输入内容" 
      v-model="value" :clearable="true">
      </el-input>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style >
.login-comen-li{
    margin-bottom:24px;
}
.login-commen-li-tag{
    margin-bottom:8px; 
}
.el-input__inner{
    border-radius:none;
}
</style>
<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        value:''
      }
    },
    props:{
        mainData:Object
    }
  }

</script>
