<template>
  <div class="mianwidth incenter videoModule">
    <div class="videoModule" id="e8888b74d1229efec6b4712e17cb6b7a_e">
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
  export default {
    data() {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    },
    props: {
      vid: String
    },
    methods: {
      video(vid) {
        console.log(vid)
        var obj={
          wrap: '#e8888b74d1229efec6b4712e17cb6b7a_e',
          width: '100%',
          height: 585,
          vid: vid,
        }
        var player = polyvPlayer(obj);
      }
    },
    created(){
      this.$on('vid',function(vid){
        this.vid=vid;
        this.video(vid)
      })
    },
    mounted() {
      
    }

  }

</script>
