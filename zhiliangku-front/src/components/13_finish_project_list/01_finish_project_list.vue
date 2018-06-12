<template>
  <section class=" project_step r rose ">
    <!--<div class="mock a" v-if="main_data.is_lock">-->
    <!--&lt;!&ndash;<img class="cc" src="./img/lock_icon.png" alt="">&ndash;&gt;-->
    <!--</div>-->
    <div class="project_top" :style="{backgroundColor: top_color}">
      <div class="project_title">
        <span class="font1_28_f dib">{{main_data.name}} </span>
        <span class="line2"></span>
      </div>
      <div class="project_info">
        <div class="dib project_time ftc">
          <img class="vm" src="./img/item.png" alt="">
        </div>
        <span class="font1_18_f dib vbt project_createt_ime">{{main_data.update_time}} </span>
        <!--<span  class="tech_tag vb dib font1_18_f" ></span>-->
        <span class="line2"></span>
      </div>
    </div>
    <p class="project_text font2_16_9" v-html="main_data.desc"></p>
  </section>
</template>
<script>
  import CB from '../00_common/07_dark_blue_button'
  import BlueButton from '../00_common/04_blue_button'

  export default {
    name: "project_item",
    data() {
      return {
        link: ''
      }
    },
    props: {
      // index: {
      //   type: Number,
      //   default: 0
      // },
      // margin_top: {
      //   type: String,
      //   default: '60px'
      // },
      main_data: {
        // required: true
      },
      top_color: {}
    },
    components: {
      CB: CB,
      BlueButton: BlueButton
    },
    methods: {
      // organize_link() {
      //   this.link = "/tracks/projects/detail/?project_id=" + this.main_data.id
      // }
    },
    created() {
      // this.organize_link()
    }
  }
</script>
<style scoped>
  .project_step {
    width: 370px;
    height: 280px;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 0 18px rgba(0, 0, 0, 0.15);
  }

  .project_title {
    padding-left: 20px;
    font-weight: bold;
    height: 80px;
    line-height: 80px;
  }

  .line2 {
    width: 100%;
    display: inline-block;
  }

  .project_info {
    line-height: 50px;
    height: 50px;
    background-color: rgba(255, 255, 255, 0.3)
  }

  .project_time {
    height: 50px;
    line-height: 50px;
    width: 70px;
  }

  .project_text {
    margin: 16px 60px 36px 60px;
    height: 102px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    line-height: 26px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;

  }
</style>


