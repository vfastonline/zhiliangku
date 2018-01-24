<template>
  <div class="interview-header-container ">
    <div class="mainwidth incenter relative interview-header">
      <div class="middle ii-header">
        <div class="fontcenter">
          <span class=" font36plffffff">{{mainData.position}}</span>
        </div>
        <div class="tags-container incenter">
          <div class="tag-c">
            <div class="fontcnenter">
              <span class="font14plffffff">题目数：</span>
            </div>
            <div class="fontcnenter">
              <span class="font18plffffff">{{mainData.amount}}</span>
              <span class="font14plffffff">道题</span>
            </div>
          </div>
          <div class="tag-c tag-s">
            <div class="fontcnenter">
              <span class="font14plffffff">测评时长：</span>
            </div>
            <div class="fontcnenter">
              <span class="font18plffffff">{{mainData.duration}}</span>
              <span class="font14plffffff">分钟</span>
            </div>
          </div>
          <div class="tag-c">
            <div class="fontcnenter">
              <span class="font14plffffff">试卷总分：</span>
            </div>
            <div class="fontcnenter">
              <span class="font18plffffff">{{mainData.score_sum}}</span>
              <span class="font14plffffff">分</span>
            </div>
          </div>
        </div>
        <div class="fontcenter"><el-button @click="go(mainData.id)">开始答卷</el-button></div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    },
    props: {
      mainData:Object
    },
    methods: {
      go(id){
        this.$fn.go('/interview_questions/examinationquestion/list/?enterprise_id='+id)
      }
    },
    created() {

    },
    components: {

    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .interview-header-container {
    background: skyblue;
  }

  .interview-header {
    height: 250px;
  }

  .tags-container {
    width: 360px;
    display: flex;
    justify-content: space-between;
    padding-top:24px;
    padding-bottom:36px;
  }

  .tag-s {
    padding: 0 40px;
    border-left: 2px solid #ffffff;
    border-right: 2px solid #ffffff;
  }

</style>