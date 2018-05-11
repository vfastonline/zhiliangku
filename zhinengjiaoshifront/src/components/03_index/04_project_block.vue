<template>
  <section :style="S" class="project_block mw hc">
    <div class="project_image_container fl ftc"><img class="project_face_image  " src="./img/project_face_1.png" alt="">
    </div>
    <div class="project_info">
      <h4 class="project_type font1_22_b_4">hello world !</h4>
      <h2 class="project_name font1_30_3">Hello World</h2>
      <p class="project_introduce">hello World</p>
      <!--<el-button> <span class="font1_26_ff project_button">查看详情</span></el-button>-->
      <a href="#">
        <Button>查看详情</Button>
      </a>
    </div>
  </section>
</template>

<script>
  import Button from '../00_common/01_prime_button'

  export default {
    name: "project_block",
    props: {
      S: {
        type: Object,
        default: function () {
          return {'margin-bottom': '60px'}
        }
      }
    },
    components: {
      Button: Button
    }
  }
</script>

<style scoped>
  .project_block {
    height: 350px;
    border-radius: 10px;
    overflow: hidden;
  }

  .project_image_container {
    background-color: #d4e2ff;
    width: 410px;
    height: 100%;
  }

  .project_face_image {
    margin-top: 50px;
  }

  .project_info {
    margin-left: 530px;
    margin-right: 100px;
    max-height: 350px;
    padding-top: 46px;
  }

  .project_type {
    margin-bottom: 25px;
  }

  .project_name {
    margin-bottom: 12px;
  }

  .project_introduce {
    height: 95px;
  }

  .project_button {
    padding: 0 28px;
  }
</style>
