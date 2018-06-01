<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <personalInfo></personalInfo>
      <layout></layout>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>
#main{
  background-color: #f8fafc;
}
</style>

<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import F from '../../components/01_header_footer/03_footer'
  import personalInfo from '../../components/11_personal_center/01_user_info.vue'
  import layout from '../../components/11_personal_center/03_layout'
  export default {
    name: 'personal_center',
    data() {
      return {}
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      personalInfo: personalInfo,
      layout:layout
    }
  }
</script>
