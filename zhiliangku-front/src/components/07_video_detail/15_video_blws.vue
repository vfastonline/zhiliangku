<template>
  <div class="player_container">
    <div class="my_video" id="my_video"></div>
  </div>
</template>

<script>
  export default {
    name: "video_blws",
    data(){
      return {
        video_map:{
        }
      }
    },
    props:{
      main_data:{}
    },
    methods: {
      video() {
        var obj = {
          wrap: '#my_video',
          width: '850px',
          height: '525px',
          vid: this.main_data.vid,
        }
        var player = window.polyvPlayer(obj);
        console.log(player)
        this.video_map.player = player;
      },
    },
    mounted(){
      console.log(this.main_data)
      this.video()
    }
  }
</script>

<style scoped>
.player_container{
  width: 850px;
  height: 525px;
  margin-top: 16px;
}
</style>
