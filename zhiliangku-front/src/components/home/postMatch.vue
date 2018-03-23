<template>
  <div class="post-match ">
      <div class="font16pl3a3c50 pm-mymatch">我匹配的岗位</div>
      <div id="radarGraph" style="width:298px;height:272px;"></div>
      <div class="pm-font fontcenter font14pr424242">您目前还没有匹配的岗位，快来这里学习吧</div>
      <div class="pm-font blue fontcenter font14pr23b8ff"><span class="pointer" > 课程库</span></div>
      <div class="pm-font blue fontcenter font14pr23b8ff"><span class="pointer" > 职业路径</span></div>
  </div>
</template>
<script>
export default {
  name: "postMatch",
  data() {
    return {
    };
  },
  mounted() {
    var radarGraph = echarts.init(document.getElementById("radarGraph"));
    // console.log(radarGraph)
    var option = {
      radar: {
        name: {
          textStyle: {
            color: "#424242",
            fontsize: "14px",
            fontfamily: "PingFangSC-Regular",
            padding: [3, 5]
          }
        },
        axisLine: {
          lineStyle: {
            color: "#fff"
          }
        },
        splitLine: {
          show: false
        },
        splitArea: {
          show: true,
          areaStyle: {
            color: ["rgb(218,243,255)", "rgb(112,209,255)", "rgb(35,184,255)"],
            shadowColor: "'rgba(0, 0, 0, 0.1)'",
            shadowBlur: 4
          }
        },
        splitNumber: 3,
        indicator: [
          { name: "可靠", max: 6500 },
          { name: "表达", max: 16000 },
          { name: "团队", max: 30000 },
          { name: "自驱", max: 38000 },
          { name: "独立", max: 52000 },
          { name: "自律", max: 25000 }
        ]
      },
      series: [
        {
          name: "预算 vs 开销（Budget vs spending）",
          type: "radar",
          // areaStyle: {normal: {}},
          symbol:"circle",
          symbolSize:"9",
          itemStyle :{
            normal:{
              color:"white"
            }
          },
          data: [
            {
              value: [4300, 10000, 28000, 35000, 50000, 19000],
              areaStyle: {
                normal: {
                  color: "rgba(255, 255, 255, 0.5)"
                }
              },
              lineStyle: {
                normal: {
                  color:"white"
                }
              }
            }
          ]
        }
      ]
    };
    radarGraph.setOption(option);
  }
};
</script>
<style scoped lang="scss">
.post-match {
  //   background: #ffffff;
  // background: pink;
  width: 362px;
  height: 441px;
  line-height: 20px;
  box-sizing: border-box;
  padding: 32px;
  box-shadow: 0 2px 5px 5px rgba(0, 0, 0, 0.1);
  background:#ffffff;  
  .pm-mymatch{
    margin-bottom: 14px;
  }
  .pm-font {
    position: relative;
    height: 20px;
    padding: 4px 0px;
  }
}
</style>


