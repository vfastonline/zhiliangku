<template>
  <section class="mw hc examInfo__section--outer">
    <title_tag :text="'考试详情'">
      <img  slot="icon" src="./img/02_note.png" alt="">
    </title_tag>
    <section class="examInfo__section--main rose">
      <div class="examInfo__div--first_line"><span class="examInfo__tag--name font1_20_3">考试名称</span><span
        class="examInfo__tag--value font1_16_9">啦啦啦啦</span></div>
      <div class="justify">
        <span class="examInfo__tag--container"><span class="examInfo__tag--name font1_20_3">考试时间</span><span
          class="examInfo__tag--value font1_16_9">sjdkjfsdk</span></span>
        <span class="examInfo__tag--container"><span class="examInfo__tag--name font1_20_3">考试时间</span><span
          class="examInfo__tag--value font1_16_9">sjdkjfsdk</span></span>
      </div>
      <div class="justify justify_last">
        <span class="examInfo__tag--container"><span class="examInfo__tag--name font1_20_3">考试时间</span><span
          class="examInfo__tag--value font1_16_9">sjdkjfsdk</span></span>
        <span class="examInfo__tag--container"><span class="examInfo__tag--name font1_20_3">考试时间</span><span
          class="examInfo__tag--value font1_16_9">sjdkjfsdk</span></span>
      </div>
    </section>
  </section>
</template>

<script>
  import title_tag from './02_title_tag'

  export default {
    name: "exam_sample_info",
    components: {
      title_tag: title_tag
    }
  }
</script>

<style scoped>
  .examInfo__section--outer {
    margin-top: 50px;
  }

  .examInfo__section--main {
    padding: 25px 225px;
    border-radius: 0 0 10px 10px;
  }

  .examInfo__div--first_line {
    margin-bottom: 25px;
  }

  .examInfo__tag--container {
    width: 220px;
  }

  .examInfo__tag--name {
    margin-right: 28px;
  }

  .justify {
    margin-bottom: 25px;
    display: flex;
    justify-content: space-between;
  }

  .justify_last {
    margin-bottom: 0px;
  }
</style>
