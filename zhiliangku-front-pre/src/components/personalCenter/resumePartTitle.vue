<template>
  <div class="resume-part-title resumewidth incenter">
    <slot></slot>
    <span class="pointer" @click="handleClick">
      <img class="imgmiddle imgr" src="../../assets/img/icons/个人中心和积分商城图标/简历_加号.svg" alt="">
      <span class="font18pl5A646E">{{taglist.label}}</span>
    </span>
  </div>
</template>
<style scoped>
  .resume-part-title {
    display: flex;
    justify-content: space-between;
    padding-top: 15px;
    padding-bottom: 15px;
    padding-right: 15px;
    border-bottom: 2px solid #eef0f2;
    margin-bottom: 12px;
  }

</style>
<script>
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
    }

  }

</script>
