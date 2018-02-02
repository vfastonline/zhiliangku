<template>
  <div class="mainwidth">
      <span   class="nomoral pointer font16pr3a3c50" :class="{'active':activeTag==index}"  v-for="(item,index) in mainData" :key="index" @click="handleClick(item,index)" >{{item.label}}</span>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.nomoral{
    background: none;
    color: #3a3c50;
    padding:4px 16px;
}
.active{
    color: #ffffff;
    background: #23b8ff;
}
</style>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
        activeTag:-1
    }
  },
  props:{
      mainData:Array
  },
  methods:{
      handleClick(item,index){
          this.activeTag=index;
          this.$emit('haveClick',item)
      }
  },
  created(){
      
  },
  mounted(){
      this.handleClick({id:0},0)
  },
  components:{
    
  }
}
</script>


