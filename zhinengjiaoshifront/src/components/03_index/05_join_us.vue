<template>
    <section class="join_us" >
      <a href="#"><WhiteButton>加入我们</WhiteButton></a>
      <a href="#"><WhiteButton>用户手册</WhiteButton></a>
    </section>
</template>

<script>
  import WhiteButton from '../../components/00_common/03_white_button'
    export default {
        name: "join_us",
      components:{
        WhiteButton:WhiteButton
      }
    }
</script>

<style scoped>
.join_us{
  margin-top: 180px;
  height: 150px;
  padding: 52px 0;
  background: url("./img/wave.png") center center;
  background-size: cover;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
</style>
