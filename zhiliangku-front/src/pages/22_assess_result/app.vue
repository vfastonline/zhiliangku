<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <div class="main_box mw hc">
        <component :is="isComponent" :main_data="main_data"></component>
      </div>
      <Message v-if="main_data.is_pass===0" :main_message="main_data"></Message>
      <div class="bottom_box mw hc ftc">
        <Button v-if="main_data.is_pass===1" class="bottom_button hc ftc">下一课程</Button>
        <Button v-if="main_data.is_pass===0" @click.native="re_write" class="bottom_button hc ftc">重新答题</Button>
        <Button v-if="main_data.is_pass===0" class="bottom_button hc ftc">重新学习</Button>
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

  .bottom_box {
    margin-top: 30px;
  }

  .bottom_button {
    width: 200px;
    height: 60px;
  }
</style>

<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import F from '../../components/01_header_footer/03_footer'
  import Success from '../../components/22_assess_result/02_success'
  import Failure from '../../components/22_assess_result/01_failure'
  import Button from '../../components/00_common/04_blue_button'
  import ImageBlock from '../../components/00_common/08_image_block'
  import Message from '../../components/22_assess_result/03_message'


  export default {
    data() {
      return {
        main_data: {}
      }
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      Success: Success,
      Failure: Failure,
      Button: Button,
      ImageBlock: ImageBlock,
      Message: Message
    },
    methods: {
      re_write(){
        window.location.href='/assess/info/?video_id='+this.$fn.funcUrl('video_id')
      },
      getResult() {
        let video_id = this.$fn.funcUrl("video_id");
        let obj = {
          'video_id': video_id
        }
        this.$post("/assess/result/info", obj).then(res => {
          if (!res.err) {
            this.main_data = res.data.data
          }

        })
      },

    },
    created() {
      this.getResult()
    },
    computed: {
      isComponent() {
        return  (this.main_data.is_pass===1) ? Success : Failure
      }
    }

  }
</script>
