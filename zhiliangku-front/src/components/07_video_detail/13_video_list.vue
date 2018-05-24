<template>
  <div class="a content_list ">
    <div ref="section_scroll" class="list_content">
      <div v-for="(item,index) in main_list.sections" :key="index">
        <div class="section_title font1_18_f vm">
          <img class="vm" v-if="item.unlock" src="./img/unlock.png" alt="">
          <img class="vm" v-if="!item.unlock" src="./img/onplay.png" alt="">
          <span class="vm">{{item.title}}</span>
        </div>
        <ul class="section_list">
          <li class="font1_14_f vm" :class="{active: (element.id==video_id) }" @click = "element.unlock && go_video_detail(element)"
              v-for="(element,index) in item.videos" :key="index">
            <img class="vm" v-if="(element.unlock)&&(element.id==video_id)" src="./img/onplay.png" alt="">
            <img class="vm" v-else-if="!element.unlock" src="./img/Shape.png" alt="">
            <img class="vm" v-else-if="element.unlock" src="./img/unlock.png" alt="">
            <span class="vm">{{element.name}}</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
  import Scrollbar from 'smooth-scrollbar'

  export default {
    data() {
      return {
      }
    },
    props: {
      main_list: {}
    },
    methods:{
      getPlayId() {
        this.course_id = this.$fn.funcUrl("course_id")
        this.video_id = this.$fn.funcUrl("video_id")
      },
      go_video_detail(item) {
        location.href="/tracks/video/detail/?course_id=" + this.course_id +"&video_id="+ item.id
      }
    },
    created(){
      this.getPlayId()
    },
    mounted() {
      //  注意此处要请求数据之后进行操作
      this.scroll = Scrollbar.init(this.$refs.section_scroll)
    }
  }
</script>
