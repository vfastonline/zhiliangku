<template>
  <courseli :mainData="courseliData" @clickButton="jj()"></courseli>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>


</style>
<script>
  import courseli from './courseLi'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        courseliData: {
          job: '',
          imgStyle: {
            width: '160px',
            height: '90px'
          },
          boxStyle: {
            'margin-left': '232px'
          }
        }
      }
    },
    methods: {
      jj() {
        console.log(11111)
      }
    },
    components: {
      courseli: courseli,
    }
  }

</script>
