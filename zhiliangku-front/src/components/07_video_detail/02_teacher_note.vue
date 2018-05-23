<template>
  <div class="video-node-container">
    <el-scrollbar class="hc video-node-inner">
      <div v-html="mainData" class="hc video-node-content"></div>
    </el-scrollbar>
  </div>
</template>

<script>
  import Bus from '../../assets/js/02_bus'
  import Vue from 'vue'
  import {Scrollbar} from 'element-ui'

  Vue.use(Scrollbar)
  export default {
    name: 'student_note',
    data() {
      return {
        name: 'notes',
        mainData: '',
      }
    },
    methods: {
      getData() {
        this.$get('/tracks/video/detail/info')
      }
    },
    props: {},
    created() {
      console.log(this)
      Bus.$on('noteData', (obj) => {
        console.log(1231)
        console.log(obj)
        this.mainData = (obj + '').replace(/src="/g, 'src="' + this.$myConst.httpUrl);
      })
      //接下来的内容我不认为是一个合理的处置
      var note_data = this.$parent.$parent.video_detail_datas.notes
      if (note_data) {
        this.mainData = (note_data + '').replace(/src="/g, 'src="' + this.$myConst.httpUrl);
      }
    }
  }

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang='scss'>
  .ideo-node-inner {
    width: 700px;
    height: 440px;
    .el-scrollbar__wrap {
      overflow-y: scroll;
      overflow-x: hidden;
    }
  }
</style>

<style lang='scss' scoped>


  .video-node-content {
    width: 700px;
    min-height: 400px;
    // /* background:skyblue; */
  }

  .video-node-container {
    background: #fafafa;
    min-height: 70vh;
    margin-bottom: 30px;
    padding-top: 32px;
  }

</style>
