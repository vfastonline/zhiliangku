<template>
  <div class="allocation_stake hc ftc">
    <mt-button @touchstart.native="clear"
               type="primary">清空</mt-button>
    <stake_tag @touchstart.native="add_Sweeten(item)"
               v-for="item in tag_value"
               :key="item"
               :num="item"></stake_tag>
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
      id: ''
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
      Bus.$emit('clear_stake')
    },
    add_Sweeten (num) {
      if (!this.id) return
      if (num > this.user_mark.value) return
      this.user_mark.value -= num
      Bus.$emit('Sweeten', { id: this.id, num: num })
    },
    selected (el) {
      this.id = el.id
    },
    bet () {
      if (this.aready) return
      if (!this.id) return
      let bet_info = []
      this.tournament.forEach(element => {
        if (!element.integral) return
        let obj = { integral: element.integral, tournament_id: element.id, country: element.match_results }
        bet_info.push(obj)
      });
      if (!bet_info.length) return
      this.$post('/worldcup/bet', { bet_info: bet_info }).then(res => {
        Toast({
          message: 'Upload Complete',
          position: 'bottom',
          duration: 5000
        })
        this.aready = true
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
.allocation_stake {
  width: 5.4rem;
}
</style>
