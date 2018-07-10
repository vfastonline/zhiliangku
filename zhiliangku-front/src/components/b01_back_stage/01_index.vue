<template>
  <div class="mw hc index_block">
    <!--这个bug很奇怪啊，内容自动居中了，这是为什么，也没有写样式啊.调查之后发现是上面的盒子浮动子元素卡住了本行内容-->
    <div class="buttons ">
      <span class="font1_30_3 dib">日常管理数据</span>
      <GreyButton class="tag_button" @click="pre_day"><span class="font1_30_f">上一日</span></GreyButton>
      <div class="dib r">
        <BlueButton class="tag_button" @click="show_dialog_func"><span class="font1_30_f">发布任务</span></BlueButton>
        <div v-show="dote" class="red_dot a"></div>
      </div>
    </div>
    <dialog_index></dialog_index>
    <chart></chart>

  </div>
</template>

<script>
  import GreyButton from '../00_common/02_grey_button'
  import BlueButton from '../00_common/04_blue_button'
  import dialog_index from './04_set_task_select_container'
  import chart from './06_progress_chart'
  import Bus from '../../assets/js/02_bus'

  export default {
    name: "01_index",
    data() {
      return {
        show_dialog: false,
        dote: false,
      }
    },
    methods: {
      show_dialog_func() {
        if(!this.dote){
          this.$notify({
            type: 'warning',
            message: '禁止重复设置任务',
            offset: 100,
            duration: 3000,
            position: 'bottom-right'
          })
        }
        if (this.dote) {
          Bus.$emit('dialog_open')
        }
      },
      pre_day() {
        Bus.$emit('pre_day')
      },
      if_have_task(){
        this.$get('/backstage/get/has/today/learn/task').then(res=>{
          if(!res.data.data){
            this.dote=true
          }
        })
      }
    },
    components: {
      GreyButton: GreyButton,
      BlueButton: BlueButton,
      dialog_index: dialog_index,
      chart: chart
    },
    created() {
      Bus.$emit('submit_task_success', () => {
        this.dote = false
      })
      this.if_have_task()
    }
  }
</script>

<style scoped lang="scss">
  .red_dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background-color: red;
    right: -4px;
    top: -4px;
  }

  .map {
    margin-top: 20px;
  }

  .buttons {
    .tag_button {
      height: 52px;
      width: 162px;
      padding: 0;
      margin-left: 20px !important;
    }
  }

  .index_block {
    margin-top: 30px;
    margin-bottom: 12px;
  }

</style>
