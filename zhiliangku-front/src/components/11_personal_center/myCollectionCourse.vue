<template>
  <div>
    <courseli v-for="(item,index) in mainData" :key="index" :config="{tag:'已完成',buttonStr:'继续学习'}" :styleData="courseliData"
      :mainData="item" @clickButton="learn(item)"></courseli>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>


</style>
<script>
  import Vue from 'vue'
  import courseli from './courseLi'
  import func from '../../assets/js/01_other/01_dispatch'
  Vue.prototype.$func = func
  export default {
    name: 'HelloWorld',
    data() {
      return {
        courseliData: {
          imgStyle: {
            width: '160px',
            height: '90px'
          },
          boxStyle: {
            'margin-left': '232px'
          }
        },
        mainData: []
      }
    },
    methods: {
      learn(item) {
        var type = item.last_time_learn_type,
          courseId = item.last_course_id,
          videoId = item.last_time_learn_id,
        vid = item.vid;
        if (type != 4) {
          if (!vid) {
            this.$func.showNotice(this, '内容正在制作中，敬请期待', 'info');
            return
          }
        }
        this.$func.goCourse(type, courseId, videoId)
      },
    },
    created() {
      this.$get('/personal_center/course/mycollect?custom_user_id=' + localStorage.uid).then(res => {
        this.$fn.addString(this.$myConst.httpUrl, res.data.data, 'course_img')
        this.$fn.exchangeArrayObjectKey(res.data.data, 'course_name', 'company')
        this.$fn.exchangeArrayObjectKey(res.data.data, 'course_img', 'logo')
        this.mainData = res.data.data;
      })
    },
    components: {
      courseli: courseli,
    }
  }

</script>
