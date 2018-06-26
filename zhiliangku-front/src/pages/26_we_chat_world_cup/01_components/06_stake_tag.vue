<template>
  <span class="stake_tag dib vm">
    <span class="tag_inner dib ftc">{{num}}</span>
  </span>
</template>

<script>
export default {
  data () {
    return {

    }
  },
  props: {
    num: {}
  },
  methods: {},
  created () { },
  components: {

  }
}
</script>

<style scoped lang="scss">
.stake_tag_active {
  .tag_inner {
    height: 0.7rem;
    min-width: 0.7rem;
  }
}
.stake_tag {
  padding: 0.05rem;
  background-color: #f9b189;
  border-radius: 1rem;
}
.tag_inner {
  transition: all 0.5s;
  height: 0.5rem;
  min-width: 0.5rem;
  line-height: 0.5rem;
  color: white;
  background-color: #ff7f00;
  border-radius: 1rem;
}
</style>
