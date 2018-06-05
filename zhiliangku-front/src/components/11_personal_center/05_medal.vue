<template>
    <div>
      <div class="medal_title font1_34_6 ftc">已获得<span class="font1_34_b4">14</span>枚勋章</div>
      <medal_unit></medal_unit>
    </div>
</template>

<script>
  import medal_unit from './10_medal_unit'
    export default {
        name: "medal",
      components:{
          medal_unit:medal_unit
      }
    }
</script>

<style scoped>
.medal_title{
  margin-bottom: 70px;
}
</style>
