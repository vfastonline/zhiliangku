<template>
  <div id="app">
    <!--<project-header></project-header>-->
    <!-- <post-match></post-match> -->
    <!--<carousel></carousel>-->
    <!--<subtitle :enTitle="a" :title="b" :slogon="c"></subtitle>-->
    <!--<carrerps></carrerps>-->
    <!--<interview-cover></interview-cover>-->
    <!--<cooperator ></cooperator>-->
    <!--<project-footer></project-footer>-->
    <router-view/>  
  </div>
</template>

<script>
export default {
  name: 'app',
  data(){
    return {
      a:'Live Course',
      b:'课程直播',
      c:'好好学习，天天向上'
    }
  },
  methods:{
    jj(){
      console.log(111)
    }
  }
}
</script>
<style lang="scss">
  @import "./style/style";
</style>
<style lang="scss">
  @import "./style/bass";
</style>