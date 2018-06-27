<template>
  <span class="">
    {{animatedNumber}}
  </span>
</template>

<script>
export default {
  data () {
    return {
      tweenedNumber: 0
    }
  },
  props: { main_data: {} },
  computed: {
    animatedNumber: function () {
      return this.tweenedNumber.toFixed(0);
    }
  },
  watch: {
    main_data: {
      handler: function (newValue) {
        window.TweenLite.to(this.$data, 0.5, { tweenedNumber: newValue.value });
      },
      deep: true
    }
  },
  methods: {},
  created () { },
  components: {

  }
}
</script>

<style scoped lang="scss">
</style>
