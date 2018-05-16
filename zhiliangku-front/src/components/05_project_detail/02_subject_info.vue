<template>
  <section class="subject_list mw hc">
    <div class="project_title font1_32_f">项1</div>
    <p class="project_text">
      112 sdfahd oiasjdf asdhfhu sdfhuais sdhfu sdhu chuaid hvuai sdhuiw weuhfia asdhfiuasd asdhufia ddshuif schuaiw
      112 sdfahd oiasjdf asdhfhu sdfhuais sdhfu sdhu chuaid hvuai sdhuiw weuhfia asdhfiuasd asdhufia ddshuif schuaiw
      112 sdfahd oiasjdf asdhfhu sdfhuais sdhfu sdhu chuaid hvuai sdhuiw weuhfia asdhfiuasd asdhufia ddshuif schuaiw
    </p>
    <span v-if="show_id === 1" class="dib font1_24_f tag">拆分课程</span>
    <span v-if="show_id === 2" class="dib font1_24_f tag course"  >课程详情</span>
  </section>
</template>
<style scoped>
  .subject_list {
    margin-top: 70px;
  }

  .project_title {
    padding-left: 70px;
    height: 60px;
    line-height: 60px;
    background-color: #324e5c;
    -webkit-border-radius: 10px;
    -moz-border-radius: 10px;
    border-radius: 10px;
  }

  .project_text {
    padding: 20px 300px 40px 110px;
  }

  .tag {
    line-height: 40px;
    padding: 0 48px;
    background-color: #324e5c;
    border-radius: 10px;
    margin-bottom: 40px;
  }
  .course{
    margin-left: 110px;
  }
</style>
<script>
  export default {
    name: "subject_list",
    data() {
      return {
        arr: [1,2],

      }
    },
    props:{
      show_id:{default:1}
    },
    components: {
    },
    created() {
      console.log(this.show_id)
    }
  }
</script>

