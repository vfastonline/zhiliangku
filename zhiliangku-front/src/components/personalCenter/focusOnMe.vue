<template>
  <div>
    <companyInfo></companyInfo>
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
      msg: 'Welcome to Your Vue.js App'
    }
  },
  components:{
    companyInfo:companyInfo
  }
}
</script>
