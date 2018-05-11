<template>
  <section class=" project_step r rose " :style="{'border':'1px solid'+colorArr[index]}">
    <div class="mock a">
      <img class="cc" src="./img/lock_icon.png" alt="">
    </div>
    <div class="project_title">
      <img class="vm" src="./img/01_book_tag.png" alt="">
      <span class="font1_18_f dib">时长：12小时</span>
      <span class="line2"></span>
    </div>
    <div class="project_info ftj">
      <span class="font1_22_3 dib vbt project_name">大数据</span>
      <CB class="vb">开发工具</CB>
      <span class="line2"></span>
    </div>
    <p class="project_text font2_14_9">
      123123sfasdfwefwadf2ef2e
      123123sfasdfwefwadf2ef2e
      123123sfasdfwefwadf2ef2e
      123123sfasdfwefwadf2ef2e
      123123sfasdfwefwadf2ef2e
      123123sfasdfwefwadf2ef2e
      123123sfasdfwefwadf2ef2e
      123123sfasdfwefwadf2ef2e
      123123sfasdfwefwadf2ef2e
      123123sfasdfwefwadf2ef2e
    </p>
    <div class="ftc">
      <BlueButton>查看详情</BlueButton>
    </div>
  </section>
</template>

<style scoped>
  .mock{
    height: 312px;
    width: 370px;
    background-color: rgba(153,153,153,.5);
  }
  .project_step {
    width: 370px;
    height: 312px;
    border-radius: 10px;
    overflow: hidden;
  }

  .project_title {
    text-align: justify;
    padding: 0 20px 0 30px;
    background: #647a90;
    height: 60px;
    line-height: 60px;
  }

  .line2 {
    width: 100%;
    display: inline-block;
  }

  .project_info {
    padding: 0 20px 0px 28px;
    line-height: 60px;
    height: 60px;
  }

  .project_name {
    line-height: 36px;
  }
  .project_text {
    padding: 5px 20px 0 30px;
    margin-bottom: 25px;
    height: 108px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 5;
    -webkit-box-orient: vertical;
  }
</style>
<script>
  import CB from '../00_common/07_dark_blue_button'
import BlueButton from '../00_common/04_blue_button'
  export default {
    name: "project_item",
    data() {
      return {
        colorArr: ['#324e5c', '#c25a75']
      }
    },
    props: {
      index: {
        type: Number,
        default: 0
      },
      margin_top: {
        type: String,
        default: '60px'
      }
    },
    components: {
      CB: CB,
      BlueButton:BlueButton
    }
  }
</script>
