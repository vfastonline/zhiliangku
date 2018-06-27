<template>
  <div class=" r">
    <div class="question_content">{{index}}、{{main_data.title}}</div>
    <div class="select_tag_container r">
      <span @touchstart="submit('A')">
        <span class="select_tag dib vm "
              :class="{'selected':tag_active==='A'}"></span>
        <span class="vm dib tag_text">是</span>
      </span>
      <span @touchstart="submit('B')">
        <span class="select_tag dib vm"
              :class="{'selected':tag_active==='B'}"></span>
        <span class="vm dib tag_text">不是</span>
      </span>
    </div>
    <div class="a notice_container">
      <img v-show="result==2"
           class="vm notice_tag "
           src="../img/02_anwser_wrong.png"
           alt="">
      <span v-show="result==1"
            class=" right dib vm  ftc">
        <span class="anwser_right dib  ">+{{10*shear_status}}</span>
      </span>
    </div>
  </div>
</template>

<script>
import Bus from '../../../assets/js/02_bus'
export default {
  data () {
    return {
      tag_active: '',
      result: '',
      shear_status: 1
    }
  },
  props: {
    main_data: {},
    index: {}
  },
  watch: {
    shear_status () {
      if (this.result == 1) {
        alert(3)
        this.$post('/worldcup/score', { integral: 90 }).then(res => {
          this.$emit('add_num', 90)
        })
      }
    }
  },
  methods: {
    submit (answer) {
      if (this.result) return
      this.tag_active = answer
      if (answer === this.main_data.right) {
        this.result = 1
        let mark = 10 * this.shear_status
        this.$post('/worldcup/score', { integral: mark }).then(res => {
          this.$emit('add_num', mark)
        })
      } else {
        this.result = 2
      }
    },
  },
  created () {
    Bus.$on('shear_success', () => {
      alert(2)
      this.shear_status = 10
    })
  },
  components: {

  }
}
</script>

<style scoped lang="scss">
.select_tag_container {
  padding: 0.1rem 1.2rem 0.1rem 0.5rem;
  width: 2.6rem;
  display: flex;
  justify-content: space-between;
}
.notice_container {
  right: 0;
  top: 0.45rem;
}
.tag_text {
  font-size: 0.24rem;
}
.question_content {
  font-size: 0.24rem;
  color: white;
}
.selected {
  background-color: #ffcc3b;
}
.select_tag {
  border: 0.02rem solid black;
  height: 0.2rem;
  width: 0.2rem;
  border-radius: 100px;
}
.notice_tag {
  height: 0.52rem;
  line-height: 0.52rem;
  width: 0.52rem;
  border-radius: 100px;
}
.right {
  background-color: #ffcc3b;
  border-radius: 100px;
  padding: 0.03rem 0.03rem;
}
.anwser_right {
  background-color: #ffcc3b;
  border-radius: 100px;
  color: #f33332;
  box-sizing: border-box;
  border: 0.02rem solid #f33332;
  min-width: 0.44rem;
  line-height: 0.42rem;
  height: 0.48rem;
  padding: 0.02rem;
}
</style>
