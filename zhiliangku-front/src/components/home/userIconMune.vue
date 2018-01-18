<template>
  <div class="uim-container floatr">
  <div class="uim-username pointer"><span><a href="/personal_center/page/#/occupational/matchingRate">{{nickname}}</a></span></div>
  <div class="uim-select pointer"><span >我的课程</span></div>
  <div class="uim-select pointer"><span ><a href="/personal_center/page/#/mySettings/baseInfo">个人设置</a></span></div>
  <div class="uim-select pointer"><span >积分兑换</span></div>
  <div class="uim-select pointer"><span @click="logout()">退出登录</span></div>
  <!--<div @click="logout()">退出登录</div>-->
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.uim-container{
    /*padding:24px 0 9px 0;*/
    position: absolute;
    top:70px;
    right:0px;
    width:229px;
    line-height: 32px;
    background:white;
}

.uim-container .uim-username{
  width:230px;
  height:70px;
  line-height:70px;
  font-family:'PingFangSC-Light';
  font-size:16px;
}
.uim-container .uim-username span{
  margin-left:32px;
}



.uim-container .uim-select{
  width:239px;
  height:40px;
}


.uim-container .uim-select span{
  width:24px;
  height:22px;
  line-height:22px;
  margin:9px 133px 9px 32px;
  font-family: 'PingFangSC-Light';
  font-size:16px;
}
.uim-container .uim-select span:hover{
  color:#23B8FF;
}
</style>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      nickname:""
    }
  },
  created(){
    this.nickname=localStorage.nickname;
  },
  methods:{
      logout(){
        this.$post('/customuser/logout').then(res=>{
          if(!res.data.err){
              this.$parent.$emit('logout')
          }
        })
      },
  }
}
</script>


