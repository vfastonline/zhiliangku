<template>
  <div>
    <videoCover @playvideo="sendMsg('openDialogVideo',mainData)" 
    v-lazy:background-image="videoCoverData.pathwel"
     ></videoCover>
    <dialogVideo :mainData="mainData[0]" ></dialogVideo>
    <img class="mainwidth incenter block progress_img" v-lazy="vidandImg.pathwel" alt="">
    <div class="career-path-list-subtitle mainwidth incenter font20pl3a3c50">选择你的职业</div>
    <container :myStyle="containerStyle">
      <interview-cover v-for="(item,index) in pathList" :layout="['course']" :mainData="item" :key="index" :myStyle="itemStyle"
        :index="index" :linker="'/tracks/path/detail/'"></interview-cover>
    </container>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .career-path-list-subtitle {
    padding: 80px 0px 32px;
  }

  .progress_img {
    margin-top: 48px;
    margin-bottom: 32px;
  }

</style>
<script>
  import videoCover from './13-pathListVideoCover.vue'
  import dialogVideo from './14-dialogVideo.vue'
  import Bus from '../../assets/js/bus'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App',
        containerStyle: {
          className: ['incenter', 'clearfix', 'mainwidth']
        },
        pathList: [],
        itemStyle: {
          className: ['floatl', 'rise'],
          outerStyle: {
            'margin-right': '33px',
            'margin-bottom': '32px'
          },
          num: 3
        },
        videoCoverData:{},
        vidandImg: {},
        mainData:{}
      }
    },
    methods: {
      sendMsg(str,data){
        console.log(1)
        Bus.$emit(str,data)
      },
      getData() {
        // 获取顶部部分
        this.$get('/slides/list?category=2').then(res => {
          this.$fn.addString(this.$myConst.httpUrl, res.data.data, 'pathwel')
          this.mainData=res.data.data;
          this.vidandImg = res.data.data[0];
          this.videoCoverData=res.data.data[1];
        })
        //获取路线列表内容
        this.$get('/tracks/path/list/info').then(res => {
          this.pathList = res.data.data
          this.$fn.addString(this.$myConst.httpUrl, res.data.data, 'path_img')
          this.$fn.exchangeArrayObjectKey(this.pathList, ['path_img', 'highest_salary', 'lowest_salary', 'name'], [
            'question_img', 'highest_monthly_salary', 'lowest_monthly_salary', 'position'
          ], true)
        })
      }
    },
    created() {
      this.getData();

    },
    components: {
      dialogVideo: dialogVideo,
      videoCover:videoCover
    }
  }

</script>
