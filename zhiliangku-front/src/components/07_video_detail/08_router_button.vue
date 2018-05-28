<template>
  <div>
    <div class="mw vc-nav-bar hc ftj">
      <span class="dib ">
        <router-link to="/teacher_note" class="font16pr3a3c50 cp vc-nav-tag">
          <GreyButton @click="router_click" class="grey_button">讲师笔记</GreyButton><PrimeButton
          class="blue_button">讲师笔记</PrimeButton>
        </router-link>
        <router-link to="/student_note" class="font16pr3a3c50 cp vc-nav-tag">
          <GreyButton @click="router_click('write_note')" class="grey_button">学习笔记</GreyButton><PrimeButton
          class="blue_button">学习笔记</PrimeButton>
        </router-link>
        <router-link to="/FAQ" class="font16pr3a3c50 cp vc-nav-tag">
          <GreyButton @click="router_click" class="grey_button">FAQ</GreyButton><PrimeButton
          class="blue_button">FAQ</PrimeButton>
        </router-link>
        <router-link to="/QA_interaction" class="font16pr3a3c50 cp vc-nav-tag">
          <GreyButton @click="router_click('QA_interaction')" class="grey_button">问答互动</GreyButton><PrimeButton
          class="blue_button">问答互动</PrimeButton>
        </router-link>
      </span>
      <span class="dib">
        <span v-if="button_switch.write_note" @click="open_rich_editor('write_note')" class="font1_24_3 dib cp write_note">记笔记</span>
        <span v-if="button_switch.QA_interaction" @click="open_rich_editor('submit_question')" class="font1_24_3 dib cp submit_question">提问</span>
      </span>
      <span class="line2"></span>
    </div>
    <router-view></router-view>
  </div>
</template>
<script>
  import GreyButton from '../../components/00_common/02_grey_button'
  import PrimeButton from '../../components/00_common/01_prime_button'
  import Bus from '../../assets/js/02_bus'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        name: 'videoContent',
        button_switch: {
          write_note: false,
          QA_interaction: false
        }
      }
    },
    props: {
      main_data: {}
    },
    watch: {
      '$route': function (to, from) {
        console.log(this.$route.path)
      }
    },
    methods: {
      open_rich_editor(e){
        Bus.$emit(e)
      },
      router_click(key) {
        if (!key) return
        for (var k in this.button_switch) {
          this.button_switch[k] = false
        }
        this.button_switch[key] = true
      },
      init_sub_tag() {
        const str = this.$route.path
        let obj = {student_note: 'write_note', QA_interaction: 'QA_interaction'}
        for (var k in obj) {
          if (('/' + k) === str) {
            this.button_switch[obj[k]] = true
          }
        }
      }
    },
    created() {
      this.init_sub_tag()
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
  .write_note, .submit_question {
    padding: 0 10px;
    margin-right: 40px;
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
    background: white;
    padding: 40px 0 40px;
  }
  .vc-nav-tag {
    margin: 0 20px;
  }
</style>
