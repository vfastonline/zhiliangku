<template>
  <div class="bottom_img ">
    <img class="student_img dib hc"
         :src="$myConst.httpUrl+image_url"
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
  },
  methods: {},
  created () { },
  components: {

  }
}
</script>

<style scoped lang="scss">
.bottom_img {
  margin-left: 50%;
  transform: translate(-50%, 0);
  width: 5.2rem;
  height: 36.1vh;
  z-index: -1;
  overflow: hidden;
  background-color: #7d95ca;
  border-radius: 0.2rem;
  box-sizing: border-box;
  padding: 0.2rem;
}
.student_img {
  width: 100%;
  height: 100%;
  border-radius: 0.1rem;
}
</style>
