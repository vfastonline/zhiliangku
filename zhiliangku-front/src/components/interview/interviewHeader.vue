<template>
  <div class="interview-header-container " :style="{'background':'url('+imgurl+')'}">
    <div class="mainwidth incenter relative interview-header">
        <div class="middle"><span class=" font36plffffff">企业面试题</span></div>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.interview-header-container{
    background: skyblue;
}
.interview-header{
    height:250px;
}

</style>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      imgurl:{}
    }
  },
  props:{

  },
  methods:{

  },
  created(){
    this.$get('/slides/list?catgory=3').then(res=>{
       this.imgurl= this.$fn.addString(this.$myConst.httpUrl, res.data.data, 'pathwel')
    })
  },
  components:{
    
  }
}
</script>


