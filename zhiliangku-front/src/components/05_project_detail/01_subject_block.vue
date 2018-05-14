<template>
  <section class="subject_block rose">
    <p class="subject_name  ftc font1_22_ff">科目1</p>
    <p class="subject_introduce font1_16_6">
      大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术大数据技术</p>
    <ul class="subject_info">
      <li class="font1_18_9 subject_info_li_1"><span>时长：</span><span class="dib subject_time_value">365分钟</span> <span>完成</span><span>100%</span>
      </li>
      <li class="subject_info_li_2">
        <span class="dib">
          <img src="./img/user_icon.png" class="user_icon vm" alt="">
          <span class="dib vbo font1_18_6">李老师</span></span>
        <BlueButton class="func_button">继续学习</BlueButton>
        <span class="line2"></span></li>
    </ul>
  </section>
</template>
<style>
  .subject_introduce {
    padding: 20px 20px 0px 20px;
    margin-bottom: 10px;
    max-height: 72px;
    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    text-overflow: ellipsis;
  }
  .func_button{
    vertical-align: bottom;
  }
</style>
<script>
  import BlueButton from '../../components/00_common/04_blue_button'

  export default {
    name: "subject_block",
    data() {
      return {
        a: 1,
        b: 3
      }
    },
    props: {
      aaa: {}
    },
    components: {
      BlueButton: BlueButton
    },
    created() {
      if (this.aaa) {
        console.log(this.aaa)
      }
    }
  }
</script>

<style scoped lang="scss">
  .subject_block {
    width: 380px;
    -webkit-border-radius: 10px;
    -moz-border-radius: 10px;
    border-radius: 10px;
    overflow: hidden;
  }

  .subject_name {
    height: 60px;
    line-height: 60px;
    background-color: rgba(122, 155, 89, 0.3);
  }

  .subject_info {
    height: 110px;
    padding: 10px 20px 10px 20px;
  }

  .subject_time_value {
    margin-righr: 32px;
  }

  .user_icon {
    height: 60px;
    width: 60px;
    border-radius: 60px;
    margin-right: 10px;
  }

  .subject_info_li_1 {
    margin-bottom: 14px;
  }

  .subject_info_li_2 {
    text-align: justify;
  }

  .line2 {
    display: inline-block;
    width: 100%;
  }
</style>
