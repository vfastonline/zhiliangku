<template>
  <div class="medal_container ftc">
    <img v-if="main_data.pathwel" class="medal_img" :src="$myConst.httpUrl+main_data.pathwel" alt="">
    <div>
      <div class="font1_28_9 ftc">{{main_data.name}}</div>
      <div class="font1_16_9 ftc">{{main_data.create_time}}</div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "medal_unit",
    data() {
      return {}
    },
    props: {
      main_data: {}
    },
    created() {
      console.log(this.$props)
    }
  }
</script>

<style scoped>
  .medal_img {
    display: block;
    height: 138px;
    width: 118px;
    margin:0 auto 40px auto;
  }

  .medal_container {
    width: 230px;
    height: 240px;
    margin-bottom: 72px;
  }
</style>
