<template>
  <div class="mainwidth rise qc-container">
      <div class="clearfix">
          <img class="floatl qc-user-icon" src="../../assets/img/user-icon.jpg" alt="">
          <div class=" qc-text-container">
              <div class="marginbottom8 "><span class="font14pl7c7e8c qctc-tag">Kevin</span><span class="font14pl7c7e8c qctc-tag">2017-12-12提问</span></div>
              <div class="font20pr3a3c50 clearfix marginbottom8">
                  <div class="floatl qctc-qustion-content">aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaassssssssssssssssssssssssssssssssssssssssssssssssssssssssssss</div>
                  <div class="floatr">
                      <span class="font16pl3a3c50">5回答</span>
                      <span class="font16pl3a3c50">2 &nbsp; 次浏览</span>
                  </div>
               </div>
               <div>
                   <div class="font14pr23b8ff">悬赏 3 积分</div>
               </div>
          </div>
      </div>
  </div>
</template>
<style scoped>
.qc-container{
    box-sizing: border-box;
    padding:24px 32px 38px 32px;
    background: white;
}
.qc-user-icon{
    width:64px;
    height: 64px;
    border-radius: 50%;
}
.qc-text-container{
    margin-left:80px;
}
.qctc-tag{
    margin-right:16px;
}
.qctc-qustion-content{
    max-width:845px;
}
</style>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>


