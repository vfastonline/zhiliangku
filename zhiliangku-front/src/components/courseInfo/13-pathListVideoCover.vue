<template>
  <div class="relative path_list_video_cover">
    <div class="inmiddle plvc-inner-container">
      <div class="fontcenter font36plffffff">智量酷高薪就业班报名进行中</div>
      <div class="fontcenter img-container ">
        <img @click="handleClick" class="player-icon pointer" src="../../assets/img/icons/path+路线+课程_图标/player.svg" alt="">
      </div>
      <div class="fontcenter font16prb2bbbf">点击观看介绍视频</div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    },
    props: ['mainData'],
    methods: {
      handleClick() {
        this.$emit('playvideo')
      },
    
    },
    created() {
        
    },
    components: {

    }
  }

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .path_list_video_cover {
    width: 100%;
    height: 400px;
    background: rgba(0, 0, 0, .2);
    background-position: center;
    background-repeat: no-repeat;
    /* display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    justify-content: center;
    align-items: center */
  }

  .plvc-inner-container {
    padding-top: 114px;
  }

  .img-container {
    margin: 18px 0 24px;
  }

  .player-icon {
    height: 40px;
    width: 40px;
  }

</style>
