<template>
  <div class="resume-part-title  resumewidth hc">
    <slot></slot>
    <tag_0 class="cp" @click="handleClick">
      <img class="vs " src="./img/添加icon.png" alt="">
      <span class="font1_18_9">{{taglist.label}}</span>
    </tag_0>
  </div>
</template>
<style scoped>
  .resume-part-title {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    padding-top: 15px;
    padding-bottom: 10px;
    padding-right: 15px;
    border-bottom: 2px solid #eef0f2;
    margin-bottom: 12px;
  }

</style>
<script>
  import tag_0 from './08_tag_0'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        taglist:{}
      }
    },
    props: {
      tag: Object
    },
    methods: {
      handleClick(evt) {
        this.$emit(this.taglist.eventName)
      }
    },
    mounted() {
      if (!this.tag) {
        this.taglist.label = '添加';
        this.taglist.eventName = 'add'
      }
      if(this.tag){
        this.taglist=this.tag;
      }
    },
    components:{
      tag_0:tag_0
    }

  }

</script>
