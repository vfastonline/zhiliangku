<template>
  <div class="">
    <img class="image"
         :src="$myConst.httpUrl+main_data"
         alt="">
  </div>
</template>

<script>
export default {
  data () {
    return {

    }
  },
  props: {
    main_data: {}
  },
  methods: {},
  created () { },
  components: {

  }
}
</script>

<style scoped lang="scss">
.image {
  width: 100%;
  height: 100%;
  display: block;
}
</style>
