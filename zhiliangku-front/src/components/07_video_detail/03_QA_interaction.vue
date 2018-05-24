<template>
  <div class="qa-container ">
    <SubmitQuestion class="a submit_block rose" v-if="editor_switch" @close="editor_switch=false"
                    @submit_success="up_data"></SubmitQuestion>
    <div class="mw hc">
      <question_li :class="{'question_unit':!editor_switch,'rise':!editor_switch,'cp':!editor_switch}"
                   class=" mt24" v-for="(item) in mainData" :key="item.id"
                   @haveClick="question_unit_click"
                   :mainData="item"></question_li>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .mt24 {
    margin-bottom: 24px;
  }

  .question_unit:hover {
    background-color: #ffffff;
  }

  .qa-container {
    padding-top: 32px;
    min-height: 500px;
    background-color: white;
  }

  .submit_block {
    left: 50%;
    transform: translate(-50%);
  }
</style>
<script>
  import question_li from './04_QA_unit'
  import SubmitQuestion from './07_submit_question'
  import Bus from '../../assets/js/02_bus'

  export default {
    name: 'question_answer',
    data() {
      return {
        mainData: {},
        editor_switch: false
      }
    },
    methods: {
      question_unit_click(){
        if(this.editor_switch)return
        console.log('hei hei')
      },
      up_data() {
        this.get_data()
        this.editor_switch = false
      },
      get_data() {
        this.$get('/community/faq/list/info?video_id=' + this.$fn.funcUrl('video_id')).then(res => {
          console.log(res)
          this.$fn.addString(this.$myConst.httpUrl, res.data.data, 'custom_user_avatar')
          this.mainData = res.data.data
        })
      },
      switch_change() {
        this.editor_switch = true
      }
    },
    components: {
      question_li: question_li,
      SubmitQuestion: SubmitQuestion
    },
    created() {
      this.get_data()
      Bus.$on('submit_question',this.switch_change)
    }
  }

</script>
