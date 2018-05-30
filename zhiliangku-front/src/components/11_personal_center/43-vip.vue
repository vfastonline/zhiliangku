<template>
  <div class="mw hc personnal-center-main clearfix">
    <div class="fontcenter  vip-state"><span>会员状态： </span> 你从<span>2018</span>年<span>10</span>月<span>4</span>日加入智量酷黄金会员</div>
    <div class="split-line"></div>
    <div class="tags-container">
      <div class="tag">
        <img src="" alt="">
        <span></span>
      </div>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.vip-state{
  margin-left: 32px;
}
.split-line{
  height: 2px;
  width:429px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom:32px;
}
.tags-container{
  width:914px;
  margin-left: auto;
  margin-right: auto;
  justify-content: space-between
}
.tag{
  width: 85px;
  justify-content: center
}
</style>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
    }
  },
  props:{

  },
  methods:{

  },
  created(){

  },
  components:{

  }
}
</script>


