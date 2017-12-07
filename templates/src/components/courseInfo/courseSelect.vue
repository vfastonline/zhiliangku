<template>
  <div class="mainwidth incenter courseSelect">
      <div>
          <!-- 此处列表如何获取呢 -->
          <div class='cs-taglist'>
              <span class="cst-type floatl">方向：</span>
              <div class="clearfix cst-tagcontainer">
                  <ul class="cstt-tags">
                      <li class="font16pr3a3c50"><span>html/css</span></li>
                      <li class="font16pr3a3c50"><span>html/css</span></li>
                      <li class="font16pr3a3c50"><span>html/css</span></li>
                      <li class="font16pr3a3c50"><span>html/css</span></li>
                      <li class="font16pr3a3c50"><span>html/css</span></li>
                      <li class="font16pr3a3c50"><span>html/css</span></li>
                      <li class="font16pr3a3c50 "><span class="cstt-selected">html/css3</span></li>
                      <li class="font16pr3a3c50"><span>html/css</span></li>
                      <li class="font16pr3a3c50"><span>html/css</span></li>
                      <li class="font16pr3a3c50"><span>html/css</span></li>
                      <li class="font16pr3a3c50"><span>html/css</span></li>
                      <li class="font16pr3a3c50"><span>html/css</span></li>
                      <li class="font16pr3a3c50"><span>html/css</span></li>
                      <li class="font16pr3a3c50"><span>html/css</span></li>
                      <li class="font16pr3a3c50"><span>html/css</span></li>
                      <li class="font16pr3a3c50"><span>html/css</span></li>
                      <li class="font16pr3a3c50"><span>html/css</span></li>
                  </ul>
              </div>
          </div>
      </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
        url:'tracks/course/list'
    };
  },
  created(){
      this.$ajax.get('tracks/course/list').then(res=>{
          console.log(res)
      })
  }
};
</script>
<style scoped lang="scss">
.courseSelect {
  padding-top: 60px;
  padding-bottom: 40px;
  background: pink;
}
.cst-tagcontainer{
    margin-left:64px;
}
.cstt-tags li{
    display:inline-block;
    margin-bottom:16px;
    span{
        padding:4px 16px;
    }
}
.cstt-selected{
    background: #23B8FF;
    color:white;
}
</style>



