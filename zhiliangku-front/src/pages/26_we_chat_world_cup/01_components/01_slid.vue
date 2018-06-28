<template>
  <div class="first_block">
    <div class="titel_notice ftc">
      <img class="loudspeaker vm"
           src="../img/01_loudspeaker.png"
           alt="">
      <span class="dib vm">已下注</span>
      <span class="dib vm gamble_num">{{num}}</span>
      <span class="dib vm">次，等你来参加</span>
    </div>
    <div>
      <div class="block_title ftc">
        荣新大数据带你看透世界杯
      </div>
      <div class="banner_container ftc r sw">
        <img class="banner_img sw"
             src="../img/07_banner.png"
             alt="">
        <div class="button_container  sw a">
          <div>
          <user_icon></user_icon>
          <span class="score dib ">
            <span class="dib vm">积分：
              <num :main_data="user_mark"></num>
            </span>
          </span>
          </div>
          <span class="dib tips"
                type="primary">转发答题得10倍积分</span>
        </div>
      </div>
      <div class="question_container hc sw">
        <question_unit v-for="(item,index) in question"
                       :key="item.id"
                       :main_data="item"
                       :index="index+1"
                       @add_num="add_num">
        </question_unit>
      </div>
    </div>
    <div class="ftc rules r">
      <i class="up-arrow iconfont icon-double-arrow-up"></i>
      <span @click="rules_show">活动规则</span>
    </div>
  </div>
</template>
<script>
import question_unit from './02_question_unit'
import Bus from '../../../assets/js/02_bus'
import user_icon from './11_user_icon'
export default {
  data () {
    return {
      question: [],
      num: '',
      shear_state: 0,
      // user_icon_url: ''
    }
  },
  watch: {
    shear_state (nw) {
      console.log(1111)
    }
  },
  props: {
    main_data: {},
    user_mark: {},
    user_info: {}
  },
  methods: {
    rules_show () {
      this.$emit('show_rules')
    },
    add_num (v) {
      this.user_mark.value += v
    },
    get_question () {
      this.$get('/worldcup/topic/info').then(res => {
        this.question = res.data.data
      })
    },
    get_stak_num () {
      this.$get('/worldcup/get/bet/record/count').then(res => {
        this.num = res.data.data
      })
    },
    init_func () {
      this.get_question()
      this.get_stak_num()
    }
  },
  created () {
    this.init_func()
    Bus.$on('shear_success', () => {
      this.shear = 1
    })
    // setTimeout(() => {
    //   this.user_icon_url = this.$myConst.httpUrl + localStorage.avatar
    // }, 20);
  },
  components: {
    question_unit: question_unit,
    user_icon: user_icon
  }
}


</script>
<style scoped lang="scss">
@import '../scss/_base.scss';
.up-arrow {
  left: 50%;
  width: 0.64rem;
  height: 0.64rem;
  position: fixed;
  bottom: 0.64rem;
  transform: translate3d(-50%, 0, 0);
  // margin-left: -3.2rem;
  z-index: 999;
  background: none;
  border: none;
  padding: 0;
  animation: upArrowAni 2s infinite linear;
  i {
    width: 0.64rem;
    height: 0.64rem;
    text-align: center;
    line-height: 0.64rem;
    color: #fff;
    font-size: 0.4rem;
  }
}

@keyframes upArrowAni {
  0% {
    opacity: 0;
    transform: translate3d(-50%, 30%, 0);
  }
  30% {
    opacity: 1;
    transform: translate3d(-50%, -20%, 0);
  }
  60% {
    opacity: 0;
    transform: translate3d(-50%, -35%, 0);
  }
  100% {
    opacity: 0;
    transform: translate3d(-50%, -50%, 0);
  }
}
.score {
  height: 0.62rem;
  line-height: 0.62rem;
  padding: 0 0.06rem;
  border-radius: 1rem;
  color: white;
  font-size: 0.22rem;
  padding-left: 1rem;
  padding-right: 0.1rem;
  background: url('../img/10_blue_button.png');
  background-size: 100% 100%;
}
.banner_img {
  height: 3rem;
}
.banner_container {
  margin-bottom: 0.2rem;
}
.first_block {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.button_container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  bottom: 0rem;
}
.tips {
  height: 0.62rem;
  line-height: 0.62rem;
  padding: 0 0.06rem;
  color: white;
  font-size: 0.3rem;
  background-color: #fc5d5d;
}
.rules {
  font-size: 0.26rem;
  color: $yellow;
  margin-bottom: 0.2rem;
}
.question_container {
  background-color: $red;
  padding: 0.2rem;
  border-radius: 0.2rem;
  box-sizing: border-box;
  min-height: 5rem;
}
.block_title {
  font-size: 0.36rem;
  font-weight: 500;
  color: white;
}
.loudspeaker {
  height: 0.37rem;
  width: 0.37rem;
  margin-right: 0.1rem;
}
.titel_notice {
  background-color: $yellow;
  padding: 0.05rem;
}
.gamble_num {
  color: $red;
}
</style>
