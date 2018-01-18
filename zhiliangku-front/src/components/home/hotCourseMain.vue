<template>
  <div v-if="mainData">
    <subtitle :msg="mainData.msg"></subtitle>
    <div class="hcm-content">
      <div class="hcmc-c incenter">
        <hot-course :myStyle="{'num':4,'outerStyle':{'width':'276px','margin-right':'16px'}}" v-for="(item,index) in hotCourseData"
          :index="index" :key="item.id" :mainData="item"></hot-course>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        hotCourseData: {},
      }
    },
    props: {
      mainData: Object
    },
    methods: {
      orgnizeUrl() {
        var url = '/tracks/index_course/list';
        if (this.mainData.type) {
          url += '?' + this.mainData.type+'=1'
        }
        return url
      },
    },
    created() {
      this.$get(this.orgnizeUrl()).then(res => {
        // console.log(res)
        this.hotCourseData = this.$fn.addString(this.$myConst.httpUrl, res.data.data, ['course_img', 'avatar'])
        // console.log(this.hotCourseData)
      })
      console.log(this.mainData)
    }
  }

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .hcm-content {
    width: 100%;
    position: relative;
  }

  .hcmc-c {
    /* position: relative;
  left: 0px;
  right: 0px; */
    /* margin:auto; */
    display: flex;
    width: 1152px;
    height: 490px;
    padding-bottom: 32px;
    justify-content: space-between;
    flex-wrap: wrap;
  }

</style>
