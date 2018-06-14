<template>
  <div class="swiper-slide slide-4"
       :style="{'background-image':url}">
    <div class="main_box a">
      <div class="text_1 ftc"
           v-html="main_data[5].remark">
      </div>
      <div class="text_1_e hc ftc"
           v-html="main_data[5].english">
      </div>
      <div class="button_block ftc r">
        <span class="dib r">
          <mt-button @click="thumb_up"
                     class="main_button  dib ftc"
                     type="primary">
            为我打call
          </mt-button>
          <span class="num dib a ftc">
            <span>{{num}}</span>
            <transition enter-active-class="animated fadeInUp">
              <span class="added a"
                    v-if="thumb_up_success">+1</span>
            </transition>
          </span>
        </span>
      </div>
      <Bottomimg class="life_photo"
                 :image_url="main_data.photo5"></Bottomimg>
      <div class="focus hc">
        <img class="focus_img db hc"
             src="../img/logo.png"
             alt="">
        <!-- <div class="focus_text ftc">点击关注</div> -->
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">
.added {
  bottom: 100%;
  margin-bottom: 0.1rem;
  margin-right: 0.1rem;
}
.num {
  border: 1px solid #ff6666;
  color: #ff6666;
  height: 0.5rem;
  line-height: 0.5rem;
  min-width: 0.5rem;
  border-radius: 1rem;
  font-size: 0.18rem;
  background-color: white;
  white-space: nowrap;
  right: 0;
  top: 0;
  transform: translate(40%, -35%);
}
.main_button {
  background-color: #ff8f75;
  border-radius: 1rem;
  font: 300 0.26rem/0.6rem 'MicroSoft YaHei';
  color: #ffffff;
  width: 2rem;
  height: 0.6rem;
}
.button_touching {
  background-color: #ff7454;
}
.button_block {
  margin-bottom: 2.11vh;
}
.main_box {
  bottom: 2.288732%;
  width: 100%;
}
.text_1 {
  font: 300 0.32rem/0.32rem 'MicroSoft YaHei';
  margin-bottom: 0.26rem;
}
.text_1_e {
  width: 4.94rem;
  font: 300 0.18rem/0.32rem 'MicroSoft YaHei';
  opacity: 0.5;
  margin-bottom: 0.35rem;
}
.life_photo {
  margin-bottom: 0.2rem;
}
.focus {
  width: 1.88rem;
}
.focus_img {
  width: 1.88rem;
}
.focus_text {
  font: 300 0.28rem/0.28rem 'MicroSoft YaHei';
}
</style>
<script>
import Bottomimg from './00_commen/02_bottom_img'
import { Button, Toast } from 'mint-ui'
import Vue from 'vue';
Vue.use(Button)
export default {
  data () {
    return {
      button_touching: false,
      num: '',
      thumb_up_success: false,
      thumbed: false
    }
  },
  props: {},
  methods: {
    thumb_up () {
      if (this.thumbed) {
        Toast({
          message: '已经赞过了(๑•̀ㅂ•́)و✧',
          duration: 3000
        })
        return
      }
      this.thumbed = true;
      this.$get('/wechat/thumbsup?name=' + this.main_data.pinyin).then(res => {
        if (res.data.msg === 'success') {
          Toast({
            message: '点赞成功，送你个么么哒',
            duration: 3000
          })
          this.thumb_up_success = true
          setTimeout(() => {
            this.thumb_up_success = false
          }, 1500);
          setTimeout(() => {
            this.num++
          }, 700);
        }
      })
    },
    get_num () {
      this.$get('/wechat/thumbsuptotal?name=' + this.main_data.pinyin).then(res => {
        this.num = res.data.total
      })
    }
  },
  created () {
    this.get_num()
  },
  components: {
    Bottomimg: Bottomimg
  }
}

</script>

