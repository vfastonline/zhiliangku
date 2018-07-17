<template>
  <div class="player_container">
    <div class="my_video"
         id="my_video"></div>
  </div>
</template>

<script>
  export default {
    name: "video_blws",
    data() {
      return {
        video_map: {},
        start: false,
        timer:''
      }
    },
    watch:{
      //监听播放开始，然后开始采集数据。如果暂停则停止采集。
      start:function (nv) {
        if(nv){
          let that=this
          this.timer=setInterval(that.send_msg,5000)
          return
        }
        clearInterval(this.timer)
      }
    },
    props: {
      main_data: {}
    },
    methods: {
      //初始化播放器
      video() {
        let obj = {
          wrap: '#my_video',
          width: '850px',
          height: '525px',
          vid: this.main_data.vid,
        }
        let player = window.polyvPlayer(obj)
        this.video_map.player = player
        window.my_player = player
      },
      //想后台发送要收集的数据
      send_msg(state){
        let obj={},f=this.$fn.funcUrl,video=this.video_map.player
        obj.course_id= f('course_id')
        obj.video_id= f('video_id')
        obj.real_play_video_time=video.j2s_realPlayVideoTime()
        obj.duration=video.j2s_getDuration()
        obj.total_duration=5
        obj.status=0||state
        this.$post('/record/handle/watchrecord',obj).then(res=>{
        })
      }
    },
    mounted() {
      console.log(this.main_data)
      this.video()
    },
    created() {
      //下面这些函数均为监听播放器发生的事件。具体信息请参考保利威视帮助文档。
      window.s2j_onPlayStart = () => {
        this.start = true
      }
      window.s2j_onPlayOver = () => {
        this.start = false
      }
      window.s2j_onVideoPause = () => {
        this.start = false
      }
      window.s2j_onPlayOver=()=>{
        this.send_msg(1)
      }
    }
  }
</script>

<style scoped>
  .player_container {
    width: 850px;
    height: 525px;
    margin-top: 16px;
  }
</style>
