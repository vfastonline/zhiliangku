<template>
  <div  class="no_product ">{{str}}</div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.no_product{
    min-height: 400px;
    line-height: 400px;
    text-align: center;
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
      str:String
  },
  methods:{

  },
  created(){

  },
  components:{
    
  }
}
</script>


