<template>
  <div class="floatl path-info-left">
    <img class="pil-img" :src="mainData.path_img" alt="">
    <div class="pil-button-container relative">
        <span class="pilb-button font16pr23b8ff pointer ">参加课程</span>
    </div>
    <ul v-if="mainData.participate" class="pil-ul">
        <li class="pilu-li-1 font14pr3a3c50">路径介绍</li>
        <li class="pilu-li-2 font14pl5A646E">{{mainData.desc}}</li>
        <li class="pilu-li-3">
            <div class="pilu-tag">
                <div class="fontcenter pilu-tag-green"><span class="font20pm2a0000">{{mainData.learn_time_consum}}</span><span class="font14pm2a0000">分钟</span></div>
                <div class="fontcenter font14pl5A646E">学习耗时</div>
            </div>
            <div class="pilu-tag">
                <div class="fontcenter pilu-tag-green"><span class="font20pm2a0000">{{mainData.path_complete_schedule}}</span><span class="font14pm2a0000">%</span></div>
                <div class="fontcenter font14pl5A646E">路线完成进度</div>
            </div>
            <div class="pilu-tag">
                <div class="fontcenter pilu-tag-green"><span class="font20pm2a0000">
                    {{mainData.complete_number}}</span><span class="font14pm2a0000">/{{mainData.courses_count}}</span></div>
                <div class="fontcenter font14pl5A646E">完成节数</div>
            </div>
        </li>
    </ul>
  </div>
</template>
<script>
export default {
  data () {
    return {
      
    }
  },
  props:{
      mainData:Object
  }
}
</script>

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
    /* background:pink; */
    padding:8px 40px;
    border:2px solid #23B8FF;
}
.pilb-button-already{
    border: 2px solid #EEF0F2;
    color:#EEF0F2;
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

