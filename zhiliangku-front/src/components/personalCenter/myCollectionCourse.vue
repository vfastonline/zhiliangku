<template>
  <div>
    <courseli v-for="(item,index) in mainData" 
    :key="index" :config="{tag:'已完成'}" :styleData="courseliData" :mainData="item"
      @clickButton="jj()"></courseli>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>


</style>
<script>
  import courseli from './courseLi'
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
      jj() {
        console.log(11111)
      }
    },
    created() {
      this.$get('/personal_center/course/mypath?custom_user_id=' + localStorage.uid).then(res => {
        this.$fn.addString(this.$myConst, res.data.data, 'course_img')
        this.$fn.exchangeArrayObjectKey(res.data.data, 'course_name', 'company')
        this.mainData = res.data.data;
      })
    },
    components: {
      courseli: courseli,
    }
  }

</script>
