<template>
  <div>
    <div class="recently-learn-time">
      <div class="rlt-time-tag">
        <div class="font14pl5A646E">08月21日</div>
        <div class="font20pl3a3c50">2017</div>
      </div>
      <courseli :mainData="courseliData" @clickButton="jj()"></courseli>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.recently-learn-time{
    border-left: 2px solid #EEF0F2;
    padding-left:28px;
    position: relative;
    margin-left:-30px;
}
.recently-learn-time::before{
    content:'';
    display: block;
    height:12px;
    width:12px;
    box-sizing: border-box;
    background:white;
    border-radius: 50%;
    position: absolute;
    border: 2px solid #D5DADF;
    top:-6px;
    left:-7px;
}
.rlt-time-tag{
  width:70px;
  text-align:right;
  position:absolute;
  top:0px;
  left:-86px;
  transform: translate(0,-50%)

}
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
