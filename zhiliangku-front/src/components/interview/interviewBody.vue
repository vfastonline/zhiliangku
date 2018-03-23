<template>
  <div class="interviewBody">
    <container :myStyle="{className:['mainwidth','incenter','clearfix']}" >
      <interviewCover @click="go(item)" :myStyle="interviewStyle" 
      :layout="['number','company']" 
      v-for="(item,index) in mainData" :key="index" 
      :index="index" :mainData="item"></interviewCover>
    </container>
    <!-- <button @click="jj()">click!</button> -->
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.interviewBody{
  margin-top:48px;
}
</style>
<script>
  import apager from './apager'
  import container from '../courseInfo/container'
  import interviewCover from '../home/interviewCover'
  import Bus from '../../assets/js/bus'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        interviewStyle: {
          outerStyle: {
            'width': '362px',
            'margin-right': '32px',
            'margin-bottom':'32px'
          },
          className:['floatl','rise'],
          imgStyle: {
            height: '148px'
          },
          num: 3
        },
        "mainData": [
        ],
      }
    },
    props: {

    },
    methods: {
      jj(){
        Bus.$emit('additionEnter',{})
      },
      initMainData(data) {

      },
      go(item){
        // console.log(window.location.host+'/interview_questions/enterpriseinfo/detail/?enterpriseinfo_id='+item.id)
        // console.log(window.location.href)
        window.location.href='https://'+window.location.host+'/interview_questions/enterpriseinfo/detail/?enterpriseinfo_id='+item.id;
      }
    },
    created() {
      Bus.$on('pagerGetData',res=>{
        this.$fn.addString(this.$myConst.httpUrl,res.data.data,'question_img')
        this.mainData=res.data.data
      })
    },
    components: {
      container: container,
      interviewCover: interviewCover,
      apager:apager
    }
  }

</script>
