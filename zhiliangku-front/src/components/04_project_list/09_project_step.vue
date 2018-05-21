<template>
  <section class="mw project_step  rise hc" :style="{'border':'1px solid'+colorArr[index],'margin-top':margin_top}">
    <div class="project_title font1_32_ff" :style="{'background-color':colorArr[index]}">项目一：大数据</div>
    <div class="info_container ">
      <p class="info_text dib vm font1_20_9">
      </p>
      <img class="project_image" src="./img/project_1.png" alt="">
    </div>
  </section>
</template>
<script>
  export default {
    name: "project_item",
    data() {
      return {
        colorArr: ['#324e5c', '#c25a75']
      }
    },
    props: {
      index: {
        type: Number,
        default: 0
      },
      margin_top: {
        type: String,
        default: '60px'
      }
    }
  }
</script>
<style scoped>
  .project_title {
    height: 50px;
    padding-left: 50px;
  }

  .project_step {
    border-radius: 10px;
    overflow: hidden;
  }

  .info_container {
    display: flex;
    justify-content: space-between;
    padding: 40px 40px 40px 60px;
    text-align: justify;
  }

  .info_text {
    width: 790px;
    padding-top: 14px;
    max-height: 126px;
    vertical-align: top;
    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
  }

  .project_image {
    right: 0px;
    top: 0px;
    height: 154px;

  }
</style>
