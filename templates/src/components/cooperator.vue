<template>
  <div class="cooperator">
      <div class="cooperatortitle fontcenter font24pr2C343B">
          合作企业
      </div>
      <div>
      <img class="cooperatorLogo inxmiddle" src="../assets/img/cooperatorLogo.png" alt="">
      </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.cooperator{
    height:216px;
    width:100%;
    box-sizing: border-box;
    padding: 64px 0px;
}
.cooperatorLogo{
    height: 27px;
    width:1004px;
    margin-top:34px;
    
}
</style>
