<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <ImageBlock :src="$myConst.httpUrl+'/media/image/static/project_list_01_top.png'"
                  :style="{'height':'300px','margin-bottom':'76px'}"></ImageBlock>
      <LeaderboardResult></LeaderboardResult>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>

</style>
<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import ImageBlock from '../../components/00_common/08_image_block'
  import F from '../../components/01_header_footer/03_footer'
  import LeaderboardResult from '../../components/12_leader_board/01_leaderboard_result'
  export default {
    data() {
      return {}
    },
    components: {
      MyHeader: MyHeader,
      F: F,
      ImageBlock: ImageBlock,
      LeaderboardResult: LeaderboardResult,
    }
  }
</script>
