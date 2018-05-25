<template>
  <div id="app">
    <project-header></project-header>
    <test></test>
    <image_block :src="$myConst.httpUrl+'/media/image/static/project_list_02_bottom.png'"
                 :S="{'height':'340px'}"></image_block>
  </div>
</template>
<script>
  import projectHeader from '../../components/01_header_footer/01_header'
  import test from '../../components/21_test/01_test'
  import image_block from '../../components/00_common/08_image_block'

  export default {
    name: 'app',
    data() {
      return {}
    },
    methods: {
      jj() {
        console.log(111)
      }
    },
    created() {
      // console.log(this)
    },
    components: {
      projectHeader: projectHeader,
      test: test,
      image_block: image_block
    }
  }

</script>
<style lang="scss">
  .aq-width {
    width: 780px;
  }

  .question-title {
    margin-bottom: 16px;
  }

  .question-icon {
    height: 40px;
    width: 40px;
    margin-right: 32px;
  }

  .qestion-owner-name {
    margin-right: 16px;
  }

  .info {
    margin-bottom: 18px;
  }

  .scan {
    position: absolute;
    top: 50%;
    right: 0%;
    transform: translate(0, -50%);
  }

  .font16fbc02d {
    font-family: 'PingFangSC-Regular', 'Microsoft YaHei';
    font-size: 16px;
    color: #fbc02d;
  }
</style>

