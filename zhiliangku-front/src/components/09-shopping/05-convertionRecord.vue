<template>
  <div class="record_container mainwidth incenter rise">
    <div class="record_content">
        <div  v-lazy:background-image="mainData.images" class="img_container item">
        </div>
        <ul class="list1 item">
            <li class="font20pr5a646e">{{mainData.gtype_name}}</li>
            <li class="font20pl3a3c50">{{mainData.name}}</li>
            <li class="integral">{{mainData.integral}}积分</li>
        </ul>
        <ul class="list2 item">
            <li class="fontcenter"><el-button>立即使用</el-button></li>
            <li class="fontcenter"><el-button>再次使用</el-button></li>
            <li class="fontcenter"><span>剩余{{mainData.residue_stock}}</span></li>
        </ul>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.integral{
    font-size: 20px;
    font-family: "PingFangSC-Light"  ,"Microsoft YaHei" ;
    color: #E57373;
}
.list1{
    flex-grow: 1;
    /* background: salmon; */
}
.list1 li{
    margin-bottom:8px;
}
.list2{
    /* background: darkcyan; */
    min-width: 200px;
}
.list2 li{
    margin-bottom: 16px
}
.record_container{
    box-sizing: border-box;
    padding: 32px;
    padding-right:125px;
    margin-bottom: 32px;
    background: white;
}
.record_content{
    display: flex;
    flex-wrap: nowrap;
    justify-content: space-between;
}
.img_container{
    height: 150px;
    width: 150px;
    background-size: cover;
    background-position: center;
    margin-right: 64px;
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
      mainData:Object
  },
  methods:{

  },
  created(){

  },
  components:{
    
  }
}
</script>


