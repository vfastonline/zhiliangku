<template>
  <div class=" incenter ">
    <div id="e8888b74d1229efec6b4712e17cb6b7a_e">
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .videoModule {
    background: red;
    width: 1152px;
  }

</style>
<script>
  import Bus from '../../assets/js/bus'
  export default {
    data() {
      return {
        height: '',
        vidObj: {
          player: "",
          state: false,
          timer:''
        },
        liveIdObj:{
          id:''
        }
      }
    },
    props: {

    },
    methods: {
      video(vid) {
        var obj = {
          wrap: '#e8888b74d1229efec6b4712e17cb6b7a_e',
          width: '100%',
          height: window.innerHeight - 70,
          vid: vid,
        }
        var player = polyvPlayer(obj);
        this.vidObj.player = player;
      },
      postInfo() {
       this.vidObj.timer= setInterval(() => {
          console.log('hello')
          this.postMsg()
        }, 10*1000)

      },
      postMsg(){
        this.$post('/record/handle/watchrecord', this.orgnizeVidData()).then(res => {
            console.log(res)
          })
      },
      orgnizeVidData() {
        var obj = {
          custom_user_id: localStorage.uid,
          course_id: this.$fn.funcUrl('course_id'),
          video_id: this.$fn.funcUrl('video_id'),
          real_play_video_time: this.getRealPlayVideoTime(),
          duration: this.getDuration()
        }
        if (this.vidObj.state) {
          obj.status = 1
        }
        return obj
      },
      getRealPlayVideoTime() {
        return this.vidObj.player.j2s_getCurrentTime()
      },
      getDuration() {
        return this.vidObj.player.j2s_getDuration()
      },
      initVidEvent() {

      },
      startVid() {
        this.postInfo()
      },
      // 以下是直播
      liveVideo(id) {
        this.liveIdObj.id=id;
        var player = polyvObject('#e8888b74d1229efec6b4712e17cb6b7a_e').livePlayer({
          width: '100%',
          height: window.innerHeight - 70,
          'uid': 'a582a3b650',
          'vid': id
        });
      },
      initLiveVideo(){
        var time= Math.floor( new Date()/1000);
        var sign=md5(time+'polyvsign');
        var token=this.$get('http://api.live.polyv.net/watchtoken/gettoken?ts='+time+'&sign='+sign).then(res=>{
          console.log(res)
          this.createdLiveVideo()
        })
      
      },
      createdLiveVideo(){
         var chatHost = 'http://chat.polyv.net:80',  //socket连接地址
          chatHost2 = "http://apichat.polyv.net:80",  //获取聊天内容地址
          chatToken = token,
          roomId = liveIdObj.id,
          userId = Math.random(0,1000*10000),
          nickname = 'polyv-test',   //自定义用户名
          pic = 'http://livestatic.videocc.net/assets/wimages/missing_face.png';
      }
    },
    created() {
      this.$on('vid', function (vid) {
        this.video(vid)
      })
      this.$on('liveid', function (id) {
        this.liveVideo(id)
      })
      Bus.$on('vid', (vid) => {
        this.vid = vid;
        this.video(vid)
      })
    },
    mounted() {
      window.s2j_onPlayStart=()=>{
        this.startVid();
      }
      window.s2j_onPlayOver=()=>{
        this.vidObj.state=1;
        this.postMsg();
        clearInterval(this.vidObj.timer)
      }
    }

  }

</script>
