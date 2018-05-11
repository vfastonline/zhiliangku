<template>
  <div class="no-data ">
      <div  class="msg">暂无数据 </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.no-data{
    height:200px;
    display: flex;
    justify-content: center;
    align-items: flex-end
}
.msg{
    padding-bottom:30px;
}
</style>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
    }
  },
  props:{
      
  },
  methods:{

  },
  created(){

  },
  components:{
    
  }
}
</script>


