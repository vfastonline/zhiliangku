<template>
  <div>
    <companyInfo v-for="(item,index) in mianData" :key="index" :mainData="item"></companyInfo>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
<script>
import companyInfo from './companyInfo'
export default {
  name: 'HelloWorld',
  data () {
    return {
      mianData:{}
    }
  },
  created(){
    this.$get('/personal_center/job/focusonmybusiness?custom_user_id='+localStorage.uid).then(res=>{
      this.$fn.addString(this.$myConst.httpUrl,res.data.data,'logo')
      this.mianData=res.data.data
    })
  },
  components:{
    companyInfo:companyInfo
  }
}
</script>
