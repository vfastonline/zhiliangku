<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <imgBox :src="$myConst.httpUrl+'/media/image/static/index_01_tree_wave.png'"></imgBox>
      <community></community>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>
  #main .footer_image {
    height:300px;
  }
</style>

<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import F from '../../components/01_header_footer/03_footer'
  import community from '../../components/08_community/01_community'
  import imgBox from '../../components/00_common/08_image_block'
  export default {
    data() {
      return {}
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      community:community,
      imgBox: imgBox
    }
  }
</script>
