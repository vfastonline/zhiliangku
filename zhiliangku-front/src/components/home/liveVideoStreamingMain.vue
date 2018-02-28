<template>
  <div>
    <subtitle :msg="msg"></subtitle>
    <lvs></lvs>
  </div>
</template>
<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        msg:{
            enTitle:'Live Video',
            title:'直播课程',
            slogon:'天天好课，惊喜不断'
        }
      }
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


</style>
