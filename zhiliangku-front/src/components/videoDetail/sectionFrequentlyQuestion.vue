<template>
<div class="sfq-container">
  <div class="incenter sfq-content">
    <sectionli></sectionli>
  </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.sfq-container{
    padding-top:32px;
    background:#fafafa;
    min-height:500px;
}
.sfq-content{
    width:780px;
}
</style>
<script>
import sectionli from './sectionCommen'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  components:{
    sectionli:sectionli
  }
}
</script>


