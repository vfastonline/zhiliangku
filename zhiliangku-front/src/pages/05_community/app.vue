<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <community></community>
      <FooterImage :src="$myConst.httpUrl+'/media/image/static/project_list_02_bottom.png'"></FooterImage>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>

</style>

<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import F from '../../components/01_header_footer/03_footer'
  import community from '../../components/08_community/01_community'
  import FooterImage from '../../components/00_common/08_image_block'
  export default {
    data() {
      return {}
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      community:community,
      FooterImage: FooterImage
    }
  }
</script>
