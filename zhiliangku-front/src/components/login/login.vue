<template>
  <div>
    <el-button type="text" @click="centerDialogVisible = true">点击打开 Dialog</el-button>
    <el-dialog :show-close="false" :visible.sync="centerDialogVisible">
      <el-form :model="dynamicValidateForm" ref="dynamicValidateForm"  class="demo-dynamic">
        <el-form-item prop="email" :rules="[
      { required: true, message: '请输入邮箱地址', trigger: 'blur' },
      
      { type: 'email', message: '请输入正确的邮箱地址', trigger: 'blur,change' }
      ]">
          <el-input v-model="dynamicValidateForm.email"></el-input>
        </el-form-item>
      </el-form>
    </el-dialog>

  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


</style>
<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        centerDialogVisible: false,
        dynamicValidateForm: {
          email: ''
        }
      }
    }
  }

</script>
