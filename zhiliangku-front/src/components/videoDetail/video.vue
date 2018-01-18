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
        vid: ''
      }
    },
    props: {

    },
    methods: {
      video(vid) {
        var obj = {
          wrap: '#e8888b74d1229efec6b4712e17cb6b7a_e',
          width: '100%',
          height: 585,
          vid: vid,
        }
        var player = polyvPlayer(obj);
      },
      liveVideo(id) {
        var player = polyvObject('#e8888b74d1229efec6b4712e17cb6b7a_e').livePlayer({
          width: '100%',
          height: 585,
          'uid': 'a582a3b650',
          'vid': id
        });
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
        debugger
        this.vid = vid;
        this.video(vid)
      })
    },
    mounted() {

    }

  }

</script>
