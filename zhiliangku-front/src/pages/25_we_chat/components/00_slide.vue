<template>
  <div class="swiper-slide slide-0 r"
       :style="{'background-image':url}">
    <mt-popup class="ftc"
              v-model="popupVisible"
              position="top">
      没有非本期学员的数据哦 ┗|｀O′|┛ 嗷~~
    </mt-popup>
    <div class="search_block a">
      <input v-model="value"
             class="search_input hc db"
             placeholder="请输入姓名全拼"
             type="search">
      <span @touchstart="try_search"
            class="search_button font1_36_f db ftc hc">查询</span>
    </div>
  </div>
</template>
<style>
.mint-popup {
  width: 100%;
  text-align: center;
  background-color: rgba(0, 0, 0, 0.8);
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  color: white;
  font: normal normal 300 0.32rem/0.8rem 'MicroSoft YaHei';
}
</style>

<script type="text/ecmascript-6">
import Vue from 'vue'
import {
  Indicator,
  Toast
} from 'mint-ui'
Vue.use(window.VueLazyload)
Vue.use(Indicator)
export default {
  data () {
    return {
      value: '',
      popupVisible: false,
      show_notice: false
    }
  },
  computed: {},
  watch: {
    popupVisible: function (n_v, o_v) {
      this.handle_timer(n_v, 'popupVisible')
    },
    show_notice: function (n_v, o_v) {
      this.handle_timer(n_v, 'show_notice')
    }
  },
  methods: {
    handle_timer (n_v, key) {
      let newkey = key + '_timer'
      if (n_v) {
        this[newkey] = setTimeout(() => {
          this[key] = false
        }, 2000);
      }
      else {
        this[newkey] && clearTimeout(this[newkey])
      }
    },
    try_search () {
      var name = this.handle_value()
      if (!name) return
      this.$get('/wechat/promotion/info?name=' + name).then(res => {
        if (!this.$is_empty(res.data.data)) {
          window.location.href = '/wechat/promotion?name=' + this.value
        } else {
          Toast({
            message: ' 没有非本期学员的数据哦!!!┗|｀O′|┛ 嗷~~',
            position: 'bottom',
            duration: 2000
          });
        }
      })
    },
    handle_value () {
      var name = this.value.split('').join('').toLowerCase()
      var exp = new RegExp(/^[a-zA-Z]+$/)
      if (!exp.test(name)) {
        Toast({
          message: ' 填写名字所对应的拼音……~(￣_,￣ )~',
          position: 'bottom',
          duration: 2000
        });

        return
      }
      return name
    }
  },
  created () { },
  components: {

  }
}

</script>

<style scoped lang="scss">
.search_block {
  width: 100%;
  top: 34.947%;
}

.search_input {
  box-sizing: border-box;
  width: 4.8rem;
  height: 0.8rem;
  outline: none;
  border: 1px solid #fecba0;
  font: normal normal 400 0.49rem/0.49rem 'MicroSoft YaHei';
  margin-bottom: 0.17rem;
  padding: 0 0.187rem;
}

.search_button {
  width: 4.8rem;
  height: 0.8rem;
  line-height: 0.8rem;
  background: #ffe0af;
}
</style>