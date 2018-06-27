<template>
  <div class="sild_02">
    <div class="block_title ftc">
      荣新大数据带你看透世界杯
    </div>
    <div class="button_container ftj sw r hc">
      <img class="user_icon a"
           :src="user_icon_url"
           alt="">
      <span class="score dib ">
        <span class="dib vm">积分：{{user_mark.value}}</span>
      </span>
      <div @touchstart="show_info"
           class="dib link_button ftc r">
        <span class="a big_data bid">大数据</span>
        <span class=" teach_win "> 教你赢 </span>
        <img class="route_ball"
             src="../img/18_ball.png"
             alt="">
      </div>
    </div>
    <div class="competition_content sw">
      <div class="tody_competition sw ftc">2018世界杯</div>
      <div ref="section_scroll"
           @touchmove="move"
           class="wrapper">
        <competition v-for="item in tournament"
                     :key="item.id"
                     :main_data="item"></competition>
      </div>
      <allocation_stake class="allocation_outer"
                        :tournament="tournament"
                        :user_mark="user_mark"></allocation_stake>
      <div class="ftc quick_mark_container">
        <img class=" quick_mark"
             src="../img/05_QuickMark.png"
             alt="">
        <span>加群送好礼</span>

      </div>
    </div>

    <div class="ftc bottom_log">
      <img class="dib vm"
           src="../img/19_logo.png"
           alt="">
    </div>
  </div>
</template>
<style lang="scss" scoped>
</style>

<script>
import competition from './04_competition_unit'
import allocation_stake from './05_allocation_stake'
import Scrollbar from 'smooth-scrollbar'
export default {
  data () {
    return {
      tournament: [],
      user_icon_url: ''
    }
  },
  props: {
    user_mark: {}
  },
  methods: {
    show_info () {
      this.$emit('show_info')
    },
    move (e) {
      e.stopPropagation();
    },
    get_tournament () {
      this.$get('/worldcup/tournament/info').then(res => {
        res.data.data.forEach(element => {
          element.integral = 0
          element.match_results = ''
          // this.get_history_stake()
        });
        this.tournament = res.data.data
        setTimeout(() => {
          this.scroll = Scrollbar.init(this.$refs.section_scroll)
        }, 200);
      })
    },
    // get_history_stake () {
    //   this.$get('/worldcup/get/user/betresult').then(res => {
    //     this.handle_data(this.tournament, res.data.data)
    //   })
    // },
    // handle_data (tournament, his_data) {
    //   tournament.forEach(el => {
    //     his_data.forEach(item => {
    //       if (el.id == item.id) {
    //         el.integral = item.integral
    //         el.match_results = item.match_results
    //       }
    //     })
    //   })
    // }
  },
  created () {
    this.get_tournament()
    setTimeout(() => {
      this.user_icon_url = this.$myConst.httpUrl + localStorage.avatar
    }, 20);
  },
  mounted () {
  },
  components: {
    competition: competition,
    allocation_stake: allocation_stake
  }
}
</script>

<style scoped lang="scss">
.allocation_outer {
  margin-bottom: 0.2rem;
}
.bottom_log {
  margin-bottom: 0.2rem;
}
@import '../scss/_base';
.route_ball {
  @keyframes rotating {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }

  animation: rotating 2s linear infinite;
}
.big_data {
  top: 0px;
  right: 100%;
  white-space: nowrap;
  padding: 0 0.1rem;
  border-radius: 1rem;
  border: 0.01rem solid white;
  background-color: $red;
  color: white;
  transform: translate(30%, 0);
}
.teach_win {
  font-size: 0.32rem;
  margin-right: 0.1rem;
}
.link_button {
  height: 0.8rem;
  padding: 0 0.2rem;
  min-width: 2.1rem;
  background: url('../img/09_yellow_button.png') no-repeat;
  background-size: 100% 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.button_container {
  margin: 0.2rem auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.wrapper {
  height: 3.5rem;
  display: block;
  margin-bottom: 0.15rem;
}
.user_icon {
  height: 0.9rem;
  width: 0.9rem;
  border-radius: 50%;
  top: 50%;
  left: 0;
  transform: translate(0, -50%);
}
.score {
  height: 0.72rem;
  line-height: 0.72rem;
  border-radius: 1rem;
  color: white;
  font-size: 0.22rem;
  padding-left: 1rem;
  padding-right: 0.1rem;
  background-image: url('../img/10_blue_button.png');
  background-size: 100% 100%;
}
.sild_02 {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}
.quick_mark {
  height: 1.6rem;
  width: 1.6rem;
}
.quick_mark_container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.competition_content {
  background-color: #fff;
  border-radius: 0.2rem;
  overflow: hidden;
}
.tody_competition {
  border-radius: 0.2rem;
  background-color: $yellow;
  color: $red;
}
.block_title {
  font-size: 0.36rem;
  font-weight: 500;
  color: white;
}
</style>
