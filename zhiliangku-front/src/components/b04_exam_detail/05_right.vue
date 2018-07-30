<template>
  <div>
    <div id="main_chart" style="width:700px;height:380px"></div>
  </div>
</template>

<script>
  import Echart from 'echarts'

  export default {
    name: "the_right",
    data() {
      return {}
    },
    mounted() {
      let my_chart = Echart.init(document.getElementById('main_chart'))
      let option = {
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: [820, 932, 901, 934, 1290, 1330, 1320],
          type: 'line'
        }]
      }
      console.log(my_chart)
      my_chart.setOption(option)
    }
  }
</script>

<style scoped>

</style>
