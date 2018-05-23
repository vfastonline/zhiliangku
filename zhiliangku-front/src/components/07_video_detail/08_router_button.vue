<template>
  <div>
    <div class="mw vc-nav-bar hc ftj">
      <span class="dib ">
        <router-link :to="{name:'teacher_note'}"  class="font16pr3a3c50 cp vc-nav-tag">
          <GreyButton class="grey_button">讲师笔记</GreyButton><PrimeButton class="blue_button">讲师笔记</PrimeButton>
        </router-link>
        <router-link to="/student_note" class="font16pr3a3c50 cp vc-nav-tag">
          <GreyButton class="grey_button">学习笔记</GreyButton><PrimeButton class="blue_button">学习笔记</PrimeButton>
        </router-link>
        <router-link to="/FAQ" class="font16pr3a3c50 cp vc-nav-tag">
          <GreyButton class="grey_button">FAQ</GreyButton><PrimeButton class="blue_button">FAQ</PrimeButton>
        </router-link>
      </span>
      <span class="dib">
        <router-link to="/QA_interaction" class="font16pr3a3c50 cp vc-nav-tag">
          <GreyButton class="grey_button">问答互动</GreyButton><PrimeButton class="blue_button">互动问答</PrimeButton>
        </router-link>
      </span>
      <span class="line2"></span>
    </div>
    <router-view ></router-view>
  </div>
</template>
<script>
  import GreyButton from '../../components/00_common/02_grey_button'
  import PrimeButton from '../../components/00_common/01_prime_button'
  //我需要开发一个按钮组件了
  export default {
    name: 'HelloWorld',
    data() {
      return {
        name: 'videoContent',
        button_show_switch: [true],
        p:{a:123}
      }
    },
    props:{
      main_data:{}
    },
    components: {
      GreyButton: GreyButton,
      PrimeButton: PrimeButton
    }
  }
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
  .router-link-active {
  }
</style>
<style scoped lang="scss">
  .blue_button {
    display: none !important;
  }

  .router-link-active {
    color: #23B8FF;
    .grey_button {
      display: none;
    }
    .blue_button {
      display: inline-block !important;
    }
  }

  .vc-nav-bar {
    line-height: 70px;
    background: white;
  }

  .vc-nav-tag {
    margin: 0 40px;
  }
</style>
