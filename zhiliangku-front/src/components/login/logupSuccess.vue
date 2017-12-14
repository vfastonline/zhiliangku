<template>
  <div>
    <el-button type="text" @click="centerDialogVisible = true">点击打开 Dialog</el-button>
    <el-dialog :show-close="false" :visible.sync="centerDialogVisible">
      <div slot="title" class="fontcenter font18plffffff marginbottom8">账号创建</div>
      <div class="logup-success-body">
          <img class="marginbottom24 incenter " src="../../assets/img/icons/注册弹窗 邮箱激活弹窗_对勾.svg" alt="">
          <div class="fontcenter marginbottom8">账号创建成功</div>
          <!-- <img class="marginbottom24 incenter " src="../../assets/img/icons/找回密码弹窗_邮件找回_邮件.svg" alt=""> -->
          <div class="fontcenter marginbottom24">邮件已发至<span class="font14pr23b8ff">wangxinmu@qq.com</span></div>
      </div>
      <el-button :class="['login-commen-container-button','font20plffffff','fontcenter','incenter','pointer']">去邮箱验证</el-button>
    </el-dialog>

  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.longin-bottom-icons{
  margin-right:24px;
}
.logup-success-body{
    padding-top: 70px;
}
.logup-success-body img{
    display: block;
}
.login-bottom-button{
  margin-top:8px;
  width:300px;
  height:40px;
  border:2px solid #ffffff;
  line-height:40px;
}
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
