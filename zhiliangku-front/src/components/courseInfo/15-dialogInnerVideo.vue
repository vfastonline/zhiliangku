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
// 把这部分拆开呢，是很违心的事情，也是比较失败的一部分。我想着复用，但是可惜的是那样会导致代码太乱。抽象能力很重要
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
    },
    created() {
      Bus.$on('vid', (vid) => {
        this.vid = vid;
        this.video(vid)
      })
    },
    mounted() {
    }

  }

</script>
