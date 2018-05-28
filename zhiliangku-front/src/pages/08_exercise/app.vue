<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <exercisesProgress></exercisesProgress>
      <choiceQuestion></choiceQuestion>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>

</style>

<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import F from '../../components/01_header_footer/03_footer'
  import exercisesProgress from '../../components/10_exercise/01_progress'
  import choiceQuestion from '../../components/10_exercise/02_choice_question'

  export default {
    data() {
      return {}
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      choiceQuestion:choiceQuestion,
      exercisesProgress:exercisesProgress,
    }
  }
</script>
