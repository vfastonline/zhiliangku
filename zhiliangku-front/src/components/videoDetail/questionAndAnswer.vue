<template>
  <div class="qa-container">
    <div class="mainwidth incenter">
     <qustionli></qustionli>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.qa-container{
  padding-top:32px;
    background:#fafafa;
    min-height:500px;
}
</style>
<script>
import qustionli from './questionCommen'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    },
    components:{
      qustionli:qustionli
    }
  }

</script>
