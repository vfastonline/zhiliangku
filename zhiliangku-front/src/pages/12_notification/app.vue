<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <MessageCenter :main_data="main_data"></MessageCenter>
      <Pager class="hc" @pagerGetData="getMainData" :url="url" first-data="true" style="background-color: #fafafa;padding-bottom:80px;"></Pager>
    </div>
    <imgBlock :src="$myConst.httpUrl+'/media/image/static/project_list_01_top.png'"></imgBlock>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>

</style>

<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import F from '../../components/01_header_footer/03_footer'
  import  MessageCenter from '../../components/14_notification/01_message_center'
  import imgBlock from '../../components/00_common/08_image_block'
  import Pager from '../../components/00_common/06_pager'
  export default {
    data() {
      return {
        url: "/notification/list/info",
        main_data: ""
      }
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      MessageCenter:MessageCenter,
      imgBlock: imgBlock,
      Pager: Pager
    },
    methods: {
      getMainData(res){
        if(!res.err){
          this.main_data=res.data.data
        }
      }
    },
    created() {
      // this.$get("/notification/list/info").then(res => {
      //   console.log("res")
      // })
    }
  }
</script>
