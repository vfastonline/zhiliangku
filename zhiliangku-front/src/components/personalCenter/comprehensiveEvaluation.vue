<template>
  <div>
    <div class="font14pl5A646E">总评分高于<span class="font20pl3a3c50">26%</span>的用户（各项素质评分基于你的习题作答情况、简历内容、学习行为得出、仅供参考)</div>
    <div class="ce-echart-container">
    <div id="delicacyradarGraph" style="width:298px;height:272px;"></div>
    <ul class="ce-info-list">
      <li class="font14pl5A646E"><span class="font20pl3a3c50">70%</span> - <span>{{tagsarr[0]}}</span></li>
    </ul>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.ce-echart-container{
  margin-top:24px;
  position: relative;
}
.delicacyradarGraph{
  margin-left:100px;
}
.ce-info-list{
  position: absolute;
  top:24px;
  right:265px;
}
</style>
<script>
export default {
  data () {
    return {
      tagsarr:['可靠','表达','团队','自驱','独立','自律'],
      mainData:[],
      values:[]
    }
  },
  methods:{
    initEcharts(){
      var delicacyradarGraph = this.$echarts.init(document.getElementById("delicacyradarGraph"));
    // console.log(delicacyradarGraph)
    var mainData=this.mainData;
    console.log(mainData)
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
          { name: "可靠", max: 1 },
          { name: "表达", max: 1 },
          { name: "团队", max: 1 },
          { name: "自驱", max: 1 },
          { name: "独立", max: 1 },
          { name: "自律", max: 1 }
        ]
      },
      series: [
        {
          type: "radar",
          // areaStyle: {normal: {}},
          symbol:"circle",
          symbolSize:"1",
          itemStyle :{
            normal:{
              color:"white"
            }
          },
          data: [
            {
              value: mainData,
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
    delicacyradarGraph.setOption(option);
    }
  },
  created(){
    this.$get('/personal_center/job/overallqualityscore?custom_user_id='+localStorage.uid).then(res=>{
      this.mainData=res.data.data
      this.initEcharts()
    })
  },
  mounted() {
    
  }
}
</script>


