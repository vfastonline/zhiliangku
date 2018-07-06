<template>
  <div class="rose confirm_container a ">
    <div class="title font1_30_6 ftc">
      今日任务将发布，确定提交？
    </div>
    <div class="ftc">
      <GreyButton @click="$emit('close')" class="button"><span class="font1_28_f">取消</span></GreyButton>
      <BlueButton @click="$emit('confirm')" class="button"><span class="font1_28_f">确定</span></BlueButton>
    </div>
  </div>
</template>

<script>
  import GreyButton from '../00_common/02_grey_button'
  import BlueButton from '../00_common/04_blue_button'
  export default {
    name: 'double_confirm',
    data() {
      return {}
    },
    components:{
      GreyButton:GreyButton,
      BlueButton:BlueButton
    },
    created(){
    }
  }
</script>

<style scoped>
  .button{
    width: 200px;
    height: 60px;
    padding: 0!important;
  }
  .button + .button{
    margin-left: 20px;
  }
  .title {
    margin-bottom: 25px;
  }

  .confirm_container {
    background-color: white;
    width: 700px;
    height: 220px;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
</style>
