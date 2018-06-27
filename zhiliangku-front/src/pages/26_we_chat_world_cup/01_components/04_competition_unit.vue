<template>
  <div class="competition_container hc">
    <div class="country_container hc">
      <div class="country">
        <img class="country_flag" :src="$myConst.httpUrl+ main_data.country_a_flag" alt="">
        <div>{{main_data.country_a_name}}</div>
      </div>
      <img class="vs_icon" src="../img/04_vs.png" alt="">
      <div class="country">
        <img class="country_flag" :src="$myConst.httpUrl+main_data.country_b_flag" alt="">
        <div>{{main_data.country_b_name}}</div>
      </div>
    </div>
    <div class="resault_state hc">
      <div class="r country ">
        <mt-button class="button_state" @click="active_button('A')" :class="{'active_button':main_data.match_results=='A'}" type="default">胜</mt-button>
        <span v-show="main_data.match_results=='A'" class="stake_num ftc a">{{main_data.integral}}</span>
      </div>
      <div class="r country ">
        <mt-button class="button_state" @click="active_button('C')" :class="{'active_button':main_data.match_results=='C'}" type="default">平</mt-button>
        <span v-show="main_data.match_results=='C'" class="stake_num ftc a">{{main_data.integral}}</span>
      </div>
      <div class=" country r">
        <mt-button class="button_state" @click="active_button('B')" :class="{'active_button':main_data.match_results=='B'}" type="default">胜</mt-button>
        <span v-show="main_data.match_results=='B'" class="stake_num ftc a">{{main_data.integral}}</span>
      </div>
    </div>
  </div>
</template>

<script>
  import Bus from '../../../assets/js/02_bus'

  export default {
    data() {
      return {}
    },
    props: {
      main_data: {}
    },
    watch: {},
    methods: {
      add_stake(data) {
        if (data.id != this.main_data.id) return
        this.main_data.integral += data.num
      },
      active_button(tag) {

        this.main_data.match_results = tag
        if (this.main_data.match_results != tag) {
          Bus.$emit('add_mark', this.main_data.integral)
          this.main_data.integral = 0
        }
        if (tag) {
          let obj = {
            id: this.main_data.id
          }
          Bus.$emit('selected_button', obj)
        }
      },
      re_mark(a) {
        if (a) {
          this.main_data.integral = 0
          return
        }
        Bus.$emit('add_mark', this.main_data.integral)
        this.main_data.integral = 0
      }
    },
    created() {
      Bus.$on('Sweeten', this.add_stake)
      Bus.$on('clear_stake', this.re_mark)
    },
    components: {
    }
  }

</script>


<style scoped lang="scss">
  @import '../scss/_base';
  .button_state {
    width: 100%;
  }

  .active_button {
    background-color: red;
    color: white;
  }

  .stake_num {
    z-index: 9999;
    background-color: $yellow;
    height: 0.54rem;
    line-height: 0.54rem;
    min-width: 0.46rem;
    right: 0;
    top: 0;
    border-radius: 1rem;
    padding: 0 0.04rem;
    transform: translate(50%, -20%);
  }

  .resault_state {
    width: 4rem;
    display: flex;
    justify-content: space-between;
  }

  .country_container {
    width: 4rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .country {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
  }

  .country_flag {
    width: 0.5rem;
    height: 0.5rem;
    border-radius: 50%;
    margin: auto;
  }

  .competition_container {
    background-color: #f7f8fb;
    padding: 0.1rem;
    width: 4.9rem;
    margin-top: 0.08rem;
  }

  .country {
    width: 1.2rem;
  }

</style>
