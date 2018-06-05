<template>
  <div class="resume-part-title hc">
    <slot></slot>
    <tag_0 class="cp tag_edit" @click="handleClick">
      <img v-if="taglist.label == '添加'" class="vs " src="./img/添加icon.png" alt="">
      <img v-if="taglist.label == '编辑'" class="vs " src="./img/编辑icon.png" alt="">
      <span class="font1_20_9">{{taglist.label}}</span>
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
    border-bottom: 1px solid #e1e1e1;
    margin-bottom: 30px;
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
    created() {
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
