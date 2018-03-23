<template>
  <div>
    <img class="homeimg" :src="imgurl" alt="">
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.homeimg{
    width: 100%;
    height: 400px;
}
</style>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
        imgurl:''
    }
  },
  props:{

  },
  methods:{
      getImg(){
          this.$get('/slides/list?category=1').then(res=>{
              var url=res.data.data[0].pathwel;
              this.imgurl=this.$myConst.httpUrl+url;
          })
      }
  },
  created(){
      this.getImg()
  },
  components:{
    
  }
}
</script>


