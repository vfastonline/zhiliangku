<template>
  <div class="settings-container hc">
    <div class="setting-item r">
      <div class="tag font14pl3a3c50">收货地址：</div>
      <div class="set-content">
        <el-input v-model="value0"></el-input>
      </div>
    </div>
    <div class="setting-item r">
      <div class="tag font14pl3a3c50">收货人：</div>
      <div class="set-content">
        <el-input v-model="value1"></el-input>
      </div>
    </div>
    <div class="setting-item r">
      <div class="tag font14pl3a3c50">联系电话：</div>
      <div class="set-content">
        <el-input v-model="value2"></el-input>
      </div>
    </div>
    <rcb   @submit="submit(orgnizeData())" :layer="['submit']"></rcb>
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
      }
    },
    methods:{
      orgnizeData(){
        var obj={
          custom_user_id:localStorage.uid,
          receiver:this.value0,
          address:this.value1,
          contact_number:this.value2
        }
        return obj
      },
      submit(data){
        if(!data)return;
        this.$post('/personal_center/personal_settings/user/address',data).then(res=>{
          if(!res.data.err){
            this.$notify({
              type: 'success',
              message: '已为您设置成功',
              offset: 100,
              duration: 3000,
              position: 'bottom-right'
            });
          }
        })
      },
    },
    created(){
      this.$get('/personal_center/personal_settings/user/address?custom_user_id='+localStorage.uid).then(res=>{
        this.initForm(this, res.data.data, ['receiver', 'address', 'contact_number'], [
        'value0','value1','value2'
      ])
      })
    },
    components:{
        rcb:rcb
    }
  }
</script>
<style lang='scss' scoped>
@import './style/04_my_setting.scss';
</style>

