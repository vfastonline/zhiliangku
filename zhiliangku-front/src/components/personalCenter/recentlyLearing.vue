<template>
  <div>
    <div v-for="(item,index) in mainData" :key="index" class="recently-learn-time">
      <div class="rlt-time-tag">
        <div class="font14pl5A646E">{{item.create_time}}</div>
        <div class="font20pl3a3c50">{{item.create_time_year}}</div>
      </div>
      <courseli :config="{tag:'已完成：'}" :styleData="courseliData" :mainData="item" @clickButton="jj()"></courseli>
    </div>
  </div>
</template>

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
          },
        },
          mainData: {}
      }
    },
    methods: {
      jj() {
        console.log(11111)
      }
    },
    created() {
      this.$get('/personal_center/course/learn_recently?custom_user_id=' + localStorage.uid).then(res => {
        this.$fn.addString(this.$myConst, res.data.data, 'course_img')
        this.$fn.exchangeArrayObjectKey(res.data.data, 'course_name', 'company')
        this.mainData = res.data.data;
        console.log(res)
      })
    },
    components: {
      courseli: courseli,
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .recently-learn-time {
    border-left: 2px solid #EEF0F2;
    padding-left: 28px;
    position: relative;
    margin-left: -30px;
  }

  .recently-learn-time::before {
    content: '';
    display: block;
    height: 12px;
    width: 12px;
    box-sizing: border-box;
    background: white;
    border-radius: 50%;
    position: absolute;
    border: 2px solid #D5DADF;
    top: -6px;
    left: -7px;
  }

  .rlt-time-tag {
    width: 70px;
    text-align: right;
    position: absolute;
    top: 0px;
    left: -86px;
    transform: translate(0, -50%)
  }

</style>
