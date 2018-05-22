<template>
  <section :style="S" class="hc mw">
    <div class="project_image_container fl ftc"><img class="project_face_image  " :src="main_data.pathwel" alt="">
    </div>
    <div class="project_info">
      <h4 class="project_type font1_22_b4">精选项目{{main_data.id}}</h4>
      <h2 class="project_name font1_30_3">{{main_data.name}}</h2>
      <p class="project_introduce">{{main_data.desc}}</p>
      <!--<el-button> <span class="font1_26_ff project_button">查看详情</span></el-button>-->
      <a :href="link" target="_blank">
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
      },
      main_data:{
        required:true
      }
    },
    components: {
      Button: Button
    },
    data() {
      return {
        link: ''
      }
    },
    methods: {
      goLink() {
        this.link = "/tracks/projects/detail/?project_id="+ this.main_data.id
      }
    },
    created() {
      this.goLink()
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
