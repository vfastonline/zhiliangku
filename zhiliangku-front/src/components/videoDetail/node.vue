<template>
<div class="video-node-container">
  <div v-html="mainData" class="incenter video-node-content">
  </div>
</div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.video-node-content{
    width:700px;
    min-height:500px;
    /* background:skyblue; */
}
.video-node-container{
    background:#fafafa;
    padding-top:32px;
}
</style>
<script>
import Bus from '../../assets/js/bus'
export default {
  name: 'notes',
  data () {
    return {
      name:'notes',
      mainData:'1231221',
    }
  },
  props:{
    
  },
  created(){
    Bus.$on('noteData',(obj)=>{
      this.mainData=(obj+'').replace(/src="/g,'src="'+this.$myConst.httpUrl);
    })
    if(this.$parent.$parent.noteData){
      this.mainData=(this.$parent.$parent.noteData+'').replace(/src="/g,'src="'+this.$myConst.httpUrl);
    }
  }
}
</script>


