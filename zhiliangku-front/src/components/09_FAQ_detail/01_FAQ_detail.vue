<template>
  <div class=" incenter">
    <div class="question-container">
      <question :mainData="mainData"></question>
    </div>
    <anwserlist :mainData="mainData"></anwserlist>
    <richtext class="richtext incenter"></richtext>
<<<<<<< HEAD
    <mypager v-show="showpager" ref="pager" @updata="jj()" @pagerGetData='manipulationData' :key="pagerkey" :url="url" :addition="params" :firstData="true"></mypager>
=======
    <mypager v-show="showpager" ref="pager" @updata="jj()" @pagerGetData='manipulationData' :key="pagerkey" :url="url" :additionData="params" :firstData="true"></mypager>
>>>>>>> af948a6c0b53649fb59e6c8e61b7d2d4a6ffd544
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .incenter {
    background-color: #fafafa;
  }
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
  import question from './02_question_content'
  import anwserlist from './03_anwser_list'
  import richtext from './05_vue_qill_editor'
  import Bus from '../../assets/js/02_bus'
  import mypager from '../00_common/06_pager'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        pagerkey: '',
        mainData: {},
        params: {},
        url: '/community/faq/detail/info',
        showpager: false
      }
    },
    props: {

    },
    methods: {
      jj(){
        console.log(123)
      },
      manipulationData(res) {
        console.log(res.data);
        var arr = res.data.data.faq_answer_list;
        if(res.data.paginator.total_count>12){
          this.showpager=true
        }
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
        this.$refs.pager.upData()
      })
      this.params={
        'faq_id':this.$fn.funcUrl('faq_id')
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
