<template>
  <div>
    <div v-for="(item,index) in mainData" :key="index" class="recently-learn-time">
      <div class="rlt-time-tag">
        <div class="font14pl5A646E">{{item.create_time}}</div>
        <div class="font20pl3a3c50">{{item.create_time_year}}</div>
      </div>
      <courseli :config="{tag:'已完成：',buttonStr:'继续学习'}" :styleData="courseliData" :mainData="item" @clickButton="learn(item)"></courseli>
    </div>
  </div>
</template>
<script>
  import courseli from './courseLi'
  import func from '../../assets/js/commen/func'
  Vue.prototype.$func = func;
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
      learn(item) {
        var type = item.last_type,
          courseId = item.last_course_id,
          videoId = item.last_video_id,
          vid=item.vid;
          if(type!=4){
            if(!vid){
              this.$func.showNotice(this,'内容正在制作中，敬请期待','info');
              return
            }
          }
        this.$func.goCourse(type, courseId, videoId)
      },
      getData() {
        this.$get('/personal_center/course/learn_recently?custom_user_id=' + localStorage.uid).then(res => {
          this.$fn.addString(this.$myConst.httpUrl, res.data.data, 'course_img')
          this.$fn.exchangeArrayObjectKey(res.data.data, 'course_name', 'company')
          this.$fn.exchangeArrayObjectKey(res.data.data, 'course_img', 'logo')
          this.mainData = res.data.data;
          console.log(res)
        })
      }
    },
    created() {
      this.getData(0)
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
