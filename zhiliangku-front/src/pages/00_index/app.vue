<template>
  <div>
    <div id="main">
      <MyHeader></MyHeader>
      <Carousal></Carousal>
      <IntroduceTitle :title="'Hello World ！'"></IntroduceTitle>
      <div class="introduce_block mw hc">
        <IntroduceStep class="step"></IntroduceStep>
        <IntroduceStep class="step"></IntroduceStep>
        <IntroduceStep class="step"></IntroduceStep>
      </div>
      <IntroduceTitle :title="'Hello World ！'"></IntroduceTitle>
      <p class="hc font1_22_6 mw ftc">
        这是第一行 <br>
        这是第二行
      </p>
      <div class="enterprise_block mw hc">
        <div class="characteristic_text">
          <div v-for="item in test1" :key="item" class="characteristic_step">
            <h4 class="font1_22_6 characteristic_title">hello world</h4>
            <p class="font2_16_9">hello world 123123123 sdfw fw wer qwe qweq qweq qweq qwe qweq </p>
          </div>
        </div>
        <img class="enterprise_image" src="./img/enterprise_need.png" alt="">
      </div>
      <IntroduceTitle :title="'Hello World ！'"></IntroduceTitle>
      <ProjectFace></ProjectFace>
      <ProjectFace></ProjectFace>
      <!--<JoinUs></JoinUs>-->
      <Joined></Joined>
    </div>
    <F></F>
  </div>
</template>
<style scoped lang='scss'>
  .introduce_block {
    display: flex;
  }

  .step {
    flex: 0 0 33.3%;
    max-width: 33.3%;
  }

  .enterprise_block {
    position: relative;
  }

  .characteristic_text {
    width: 300px;
  }

  .characteristic_title {
    margin: 50px 0 20px;
  }

  .enterprise_image {
    position: absolute;
    right: 0;
    top: 50%;
    transform: translate(0, -50%);
  }
</style>

<script>
  import MyHeader from '../../components/01_header_footer/01_header'
  import Carousal from '../../components/03_index/01_carouse'
  import IntroduceStep from '../../components/03_index/02_introduce_step'
  import IntroduceTitle from '../../components/03_index/03_introduce_title'
  import ProjectFace from '../../components/03_index/04_project_block'
  import JoinUs from '../../components/03_index/05_join_us'
  import Joined from '../../components/03_index/06_joined'
  import F from '../../components/01_header_footer/03_footer'

  export default {
    data() {
      return {
        test1: [1, 2, 3, 4]
      }
    },
    components: {
      MyHeader: MyHeader,
      Carousal: Carousal,
      IntroduceStep: IntroduceStep,
      IntroduceTitle: IntroduceTitle,
      ProjectFace: ProjectFace,
      JoinUs: JoinUs,
      Joined: Joined,
      F: F
    }
  }
</script>
