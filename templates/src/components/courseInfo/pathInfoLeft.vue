<template>
  <div class="floatl path-info-left">
    <img class="pil-img" src="../../assets/img/user-icon.jpg" alt="">
    <div class="pil-button-container relative">
        <span class="pilb-button ">参加课程</span>
    </div>
    <ul class="pil-ul">
        <li class="pilu-li-1 font14pr3a3c50">路径介绍</li>
        <li class="pilu-li-2 font14pl5A646E">本计划专为立志修炼成萨里看到就发啦谁看得见佛来说降低房价偶爱金佛埃及覅哦阿里山的开发骄傲ijwe</li>
        <li class="pilu-li-3">
            <div class="pilu-tag">
                <div class="fontcenter pilu-tag-green"><span class="font20pm2a0000">30</span><span class="font14pm2a0000">分钟</span></div>
                <div class="fontcenter font14pl5A646E">学习耗时</div>
            </div>
            <div class="pilu-tag">
                <div class="fontcenter pilu-tag-green"><span class="font20pm2a0000">30</span><span class="font14pm2a0000">分钟</span></div>
                <div class="fontcenter font14pl5A646E">学习耗时</div>
            </div>
            <div class="pilu-tag">
                <div class="fontcenter pilu-tag-green"><span class="font20pm2a0000">30</span><span class="font14pm2a0000">分钟</span></div>
                <div class="fontcenter font14pl5A646E">学习耗时</div>
            </div>
            
        </li>
    </ul>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.path-info-left{
    width:320px;
}
.pil-img{
    height: 186px;
    width:320px;
}
.pil-button-container{
    height:102px;
    display: flex;
    justify-content: center;
    align-items: center
}
.pilb-button{
    background:pink;
    padding:8px 40px;
}
.pilu-li-1,.pilu-li-2{
    margin:16px 0;
}
.pilu-li-3{
    display: flex;
    justify-content: space-between;
    margin:32px 0;
}
.pilu-tag-green{
    padding:8px 0;
}
.pilu-tag{
    display: inline-block;
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


