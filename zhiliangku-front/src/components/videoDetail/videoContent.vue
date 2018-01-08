<template>
  <div>
    <div class="mainwidth vc-nav-bar incenter clearfix">
      <div class="floatl ">
        <router-link to="/note" class="font16pr3a3c50 pointer vc-nav-tag" >资料</router-link>
        <router-link to="/question" class="font16pr3a3c50 pointer vc-nav-tag" >问答</router-link>
        <router-link to="/section" class="font16pr3a3c50 pointer vc-nav-tag" >本节常见问题</router-link>
      </div>
      <div class="floatr">
        <router-link to="/submitQuestion" class="font16pr3a3c50 pointer vc-nav-tag" >提问</router-link>
      </div>
    </div>
    <router-view name="videoContent"></router-view>
  </div>
</template>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      name:'videoContent'
    }
  },
  created(){
    
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.router-link-active{
  color:#23B8FF;
}
.vc-nav-bar{
  line-height: 70px;
  background: white;
}
.vc-nav-tag{
  margin:0 40px;
}
</style>