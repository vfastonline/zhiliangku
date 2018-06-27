<template>
  <div class="">
    <img class="user_icon a"
         :src="user_icon_url"
         alt="">
    <span class="score dib ">
      <span class="dib vm">积分：{{user_mark.value}}</span>
    </span>
  </div>
</template>

<script>
export default {
  data () {
    return {

    }
  },
  props: {},
  methods: {},
  created () { },
  components: {

  }
}
</script>

<style scoped lang="scss">
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
  padding: 0 0.06rem;
  border-radius: 1rem;
  color: white;
  font-size: 0.22rem;
  padding-left: 1rem;
  padding-right: 0.1rem;
  background: url('../img/10_blue_button.png');
  background-size: 100% 100%;
}
</style>
