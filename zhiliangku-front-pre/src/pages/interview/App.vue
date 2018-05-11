<template>
  <div id="app">
    <projectHeader></projectHeader>
    <interviewHeader></interviewHeader>
    <interviewList></interviewList>
    <interviewBody></interviewBody>
    <apager :initParam="{'custom_user_id':uid}" :url="'/interview_questions/enterpriseinfo/list/info'"></apager>
    <projectFooter></projectFooter>
  </div>
</template>
<style>

</style>
<script>

  import projectHeader from '../../components/home/projectHeader.vue'
  import projectFooter from '../../components/home/projectFooter.vue'
  import interviewHeader from '../../components/interview/interviewHeader.vue'
  import interviewList from '../../components/interview/interviewList.vue'
  import interviewBody from  '../../components/interview/interviewBody.vue'
  import apager from '../../components/interview/apager.vue'
  import Bus from '../../assets/js/bus'
  export default {
    data() {
      return {
        uid:''
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
      interviewHeader:interviewHeader,
      interviewList:interviewList,
      interviewBody:interviewBody,
      apager:apager
    },
    methods: {},
    created() {
      this.uid=localStorage.uid
    }
  }

</script>
<style lang="scss">
  @import "../../style/style";

</style>
<style lang="scss">
  @import "../../style/bass";

</style>

 