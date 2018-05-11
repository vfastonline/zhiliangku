<template>
  <div id="app">
    <projectHeader></projectHeader>
    <interviewInfoHeader :mainData="mainData"></interviewInfoHeader>
    <interviewInfo :mainData="mainData"></interviewInfo>
    <projectFooter></projectFooter>
  </div>
</template>
<style>

</style>
<script>

  import projectHeader from '../../components/home/projectHeader.vue'
  import projectFooter from '../../components/home/projectFooter.vue'
  import interviewInfoHeader from '../../components/interview/interviewInfoHeader.vue'
  import interviewInfo from '../../components/interview/interviewInfo.vue'
  import Bus from '../../assets/js/bus'
  export default {
    data() {
      return {
        mainData:{}
      }
    },
    methods: {
      jj() {
        console.log(111)
      }
    },
    components: {
      projectHeader:projectHeader,
      projectFooter:projectFooter,
      interviewInfoHeader:interviewInfoHeader,
      interviewInfo:interviewInfo
    },
    methods: {},
    created() {
      this.$get('/interview_questions/enterpriseinfo/detail/info?enterpriseinfo_id='+this.$fn.funcUrl('enterpriseinfo_id')).then(res=>{
      this.mainData=res.data.data;
      console.log(res)
    })
    }
  }

</script>
<style lang="scss">
  @import "../../style/style";

</style>
<style lang="scss">
  @import "../../style/bass";

</style>

 