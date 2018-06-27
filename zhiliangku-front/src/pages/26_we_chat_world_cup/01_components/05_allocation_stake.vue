<template>
  <div class="allocation_stake hc sw ftc">
    <mt-button @touchstart.native="clear"
               type="default">清空</mt-button>
    <div class="tag_container">
      <stake_tag @touchstart.native="add_Sweeten(item)"
                 v-for="(item,index) in tag_value"
                 :key="item"
                 :class="{stake_tag_active:active_index==index}"
                 :num="item"></stake_tag>
    </div>
    <mt-button @touchstart.native="bet"
               type="primary">确定</mt-button>
  </div>
</template>

<script>
import stake_tag from './06_stake_tag'
import Bus from '../../../assets/js/02_bus'
import { Toast } from 'mint-ui';
export default {
  data () {
    return {
      tag_value: [20, 50, 100, 200],
      id: '',
      active_index: ''
    }
  },
  props: {
    user_mark: {},
    tournament: {},
    aready: false
  },
  methods: {
    clear () {
      this.id = ''
      Bus.$emit('clear_stake', this.aready)
    },
    add_Sweeten (num) {
      if (!this.id) {
        Toast({
          message: '请预测比赛结果然后投注',
          position: 'bottom',
          duration: 3000
        })
        return
      }
      if (num > this.user_mark.value) {
        Toast({
          message: '剩余积分不足',
          position: 'bottom',
          duration: 3000
        })
        return
      }
      this.active_index = this.tag_value.indexOf(num)
      this.user_mark.value -= num
      Bus.$emit('Sweeten', { id: this.id, num: num })
    },
    selected (el) {
      this.id = el.id
    },
    bet () {
      if (this.aready) {
        Toast({
          message: '请勿重复下注',
          position: 'bottom',
          duration: 3000
        })
        return
      }
      if (!this.id) {
        Toast({
          message: '尚未分配积分',
          position: 'bottom',
          duration: 3000
        })
        return
      }
      let bet_info = []
      this.tournament.forEach(element => {
        if (!element.integral) return
        let obj = { integral: element.integral, tournament_id: element.id, country: element.match_results }
        bet_info.push(obj)
      });
      if (!bet_info.length) return
      this.$post('/worldcup/bet', { bet_info: bet_info }).then(res => {
        if (!res.data.err) {
          Toast({
            message: '下注成功',
            position: 'bottom',
            duration: 3000
          })
          this.aready = true
        }
      })

    }
  },
  created () {
    Bus.$on('selected_button', this.selected)
    Bus.$on('add_mark', el => {
      this.user_mark.value += el
    })
  },
  components: {
    stake_tag: stake_tag
  }
}
</script>

<style scoped lang="scss">
.tag_container {
  width: 3rem;
  display: flex;
  justify-content: space-around;
  align-items: center;
}
.allocation_stake {
  height: 0.7rem;
  margin-bottom: 0.1rem;
  width: 5.4rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
