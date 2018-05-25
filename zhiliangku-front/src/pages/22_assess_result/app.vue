<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <div class="main_box mw hc">
        <Success :status=a></Success>
      </div>
      <Message></Message>
      <div class="bottom_button mw hc ftc">
        <Button class="hc ftc">查看详情</Button>
        <Button class="hc ftc">重新答题</Button>
        <Button class="hc ftc">重新学习</Button>
      </div>
      <ImageBlock :src="$myConst.httpUrl+'/media/image/static/project_list_02_bottom.png'"></ImageBlock>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>
  .main_box {
    /*min-height:70vh;*/
  }

  .bottom_button {
    margin-top: 30px;
  }
</style>

<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import F from '../../components/01_header_footer/03_footer'
  import Success from '../../components/22_assess_result/02_success'
  import Button from '../../components/00_common/04_blue_button'
  import ImageBlock from '../../components/00_common/08_image_block'
  import Message from '../../components/22_assess_result/03_message'


  export default {
    data() {
      return {
        status_arr: ['success', 'failure'],
        a: 0,//临时数据
        main_data: {}
      }
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      Success: Success,
      Button: Button,
      ImageBlock: ImageBlock,
      Message: Message
    },
    methods: {
      getResult() {
        let video_id = this.$fn.funcUrl("video_id");
        let obj = {
          'video_id': video_id
        }
        this.$post("/assess/result/info", obj).then(res => {
          // console.log("res.data")
          //请求数据 接口报错了。
          if (!res.err) {
            this.main_data = res.data
          }

        })
      }
    },
    created() {
      this.getResult()
    }

  }
</script>
