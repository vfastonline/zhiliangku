<template>
  <div class="font1_18_6 map">
    <div>
      <span class="font1_18_6 ">请选择查询日期:</span>
      <el-date-picker
        @change="get_chart_data"
        class="set_value"
        v-model="time"
        format="yyyy-MM-dd"
        type="date"
        placeholder="选择日期">
      </el-date-picker>
    </div>
    <div class="chart_container">
      <div id="progress_chart" ref="a" style="width: 600px; height: 400px"></div>
      <div class="ftc">
        班级平均进度
        <span class="font1_18_p">{{main_data.average}}</span>
        较昨天提高
        <span class="font1_18_p">{{main_data.improve}}</span>
      </div>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue'
  import {DatePicker} from 'element-ui'

  Vue.use(require('vue-moment'))
  Vue.use(DatePicker)
  export default {
    name: "06_progress_chart",
    data() {
      return {
        main_data: {},
        time: new Date(),
        chart: '',
      }
    },
    methods: {
      get_chart_data(time) {
        let now = new Date()
        let p_time = time || now.getTime()
        this.$get('/backstage/get/learn/schedule/by/date?get_date=' + window.moment(p_time).format('YYYY-MM-DD')).then(res => {
          console.log(res.data.data)
          let data = res.data.data
          if (typeof (data) === 'string') {
            data = window.JSON.parse(res.data.data.replace(/'/g, "\""))
          }
          this.main_data = data
          this.build_chart(data)
        })
      },
      build_chart(data) {
        console.log(typeof (data))
        let option = {
          tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b}: {c} ({d}%)"
          },
          legend: {
            orient: 'vertical',
            x: 'left',
            data: ['未完成', '已完成', '超完成']
          },
          series: [
            {
              name: '日进度数据',
              type: 'pie',
              radius: ['40%', '80%'],
              avoidLabelOverlap: false,
              label: {
                normal: {
                  show: false,
                  position: 'center'
                },
                emphasis: {
                  show: true,
                  textStyle: {
                    fontSize: '30',
                    fontWeight: 'bold'
                  }
                }
              },
              labelLine: {
                normal: {
                  show: false
                }
              },
              data: [
                {value: data.compelete, name: '已完成'},
                {value: data.excess_complete, name: '超完成'},
                {value: data.undone, name: '未完成'},
              ]
            }
          ]
        }
        let arr = ['complete', 'excess_complete', 'undone']
        arr.forEach((el, index) => {
          option.series[0].data[index].value = data[el]
        })
        if (this.chart) {
          this.chart.setOption(option)
        } else {
          this.chart = window.echarts.init(this.$refs.a).setOption(option)

        }
      }
    },
    mounted() {
      this.get_chart_data()

    }
  }
</script>

<style scoped>
  .chart_container {
    width: 600px;
  }
</style>
