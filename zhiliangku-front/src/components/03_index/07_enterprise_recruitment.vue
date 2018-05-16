<template>
  <div class="enterprise_block mw hc r">
    <div class="characteristic_text">
      <div v-for="(item,index) in main_data" :key="index" v-if="index>0" class="characteristic_step">
        <h4 class="font1_22_6 characteristic_title">{{item.title}}</h4>
        <p class="font2_16_9">{{item.desc}}</p>
      </div>
    </div>
    <img class="enterprise_image" v-if="main_data[0]" :src="main_data[0].pathwel"  alt="">
  </div>
</template>

<script>
    export default {
        name: "enterprise_recruitment",
      data(){
          return{

          }
      },
      props:{
          main_data:{type:Array}
      }
    }
</script>

<style scoped>
  .enterprise_block {
    min-height: 600px;
  }

  .characteristic_text {
    width: 300px;
  }

  .characteristic_title {
    margin: 50px 0 20px;
  }

  .enterprise_image {
    position: absolute;
    right: 0;
    top: 50%;
    transform: translate(0, -50%);
  }
</style>
