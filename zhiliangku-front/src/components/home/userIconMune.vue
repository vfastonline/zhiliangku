<template>
  <div class="uim-container floatr">
    <div @click="logout()">退出登陆</div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.uim-container{
    padding:24px 24px 9px 24px;
    width:229px;
    line-height: 32px;
    background:white;
}
</style>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  methods:{
      logout(){
        this.$post('customuser/logout').then(res=>{
          if(!res.data.err){
              this.$parent.$emit('logout')
          }
        })
      },
  }
}
</script>


