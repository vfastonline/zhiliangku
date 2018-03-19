<template>
  <div class=" incenter">
    <div class="question-container">
      <question :mainData="mainData"></question>
    </div>
    <anwserlist :mainData="mainData"></anwserlist>
    <richtext class="richtext incenter"></richtext>
    <mypager ref="pager" @updata="jj()" @pagerGetData='manipulationData' :key="pagerkey" :url="url" :addition="params" :firstData="true"></mypager>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .question-container {
    background-color: white;
    padding-top: 44px;
    padding-bottom: 24px;
  }

  .richtext {
    width: 780px;
  }

</style>
<script>
  import question from './09-question'
  import anwserlist from './11-anwserList'
  import richtext from './15-richtexteditor.vue'
  import Bus from '../../assets/js/bus'
  import mypager from './06-pager.vue'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        pagerkey: '',
        mainData: {},
        params: {},
        url: '/community/faq/detail/info'
      }
    },
    props: {

    },
    methods: {
      jj(){
        console.log(123)
      },
      manipulationData(res) {
        var arr = res.data.data.faq_answer_list;
        if(arr){
          arr.forEach((el, index) => {
          if (el.optimal) {
            arr.unshift(arr.splice(index, 1)[0])
          }
        })
        }        
        this.mainData = res.data.data;
      },
    },
    created() {
      // this.getData()
      Bus.$on('replyover', () => {
        console.log(this.$refs.pager)
        this.$refs.pager.updata()
      })
      this.params={
        'custom_user_id':localStorage.uid,
        'faq_id':this.$fn.funcUrl('id')
      }
    },
    components: {
      question: question,
      anwserlist: anwserlist,
      richtext: richtext,
      mypager: mypager
    }
  }

</script>
