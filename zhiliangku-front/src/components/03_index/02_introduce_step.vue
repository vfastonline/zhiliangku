<template>
  <div class="introduce_step" >
    <img v-lazy="stepData.pathwel" alt="">
    <h3 class="step_title ftc font1_32_6">{{stepData.title}}</h3>
    <p class="step_text font1_18_9">{{stepData.desc}}</p>
  </div>
</template>
<script>
  import Vue from 'vue'
  Vue.use(window.VueLazyload)
  export default {
    name: "introduce_step",
    data() {
      return {}
    },
    props: {
      stepData: {
        type: Object,
        default: function () {
          return {
            title: 'have no msg',
            desc: 'have no msg'
          }
        }
      }
    }
  }
</script>

<style scoped>
  .introduce_step {
    height: 456px;
  }

  .step_title {
    margin: 30px 0 20px 0;
  }

  .step_text {
    padding: 20px;
  }
</style>
