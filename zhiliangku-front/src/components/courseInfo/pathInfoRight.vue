<template>
  <div class="path-info-right">
    <div class="pir-title-container">
      <div class="font20pl3a3c50 pir-title">{{mainData.name}}</div>
      <div class="font14prb2bbbf">{{mainData.courses_count}}门课程</div>
    </div>
    <div class="pir-main-content">
      <ul>
        <li v-for="(lidata,indexli) in mainData.pathstages"  :key="indexli" 
        class="tli tli1 relative clearfix ofhid">
          <div class="pirm-dote  zindex100 pirm-dot-border-grey" 
          :class="{
            'pirm-dote-solid-green':indexli<indexli1,
            'pirm-dote-border-green':indexli==indexli1
            }">
          </div>
          <div
          class="pirm-line-top  zindex10 pirm-line-grey"
          v-if="indexli"
          :class="{
          'pirm-line-green':indexli<=indexli1+1,
          }"
          >
          </div>
          <div class="pirm-line  zindex1 pirm-line-grey" 
          :class="{'pirm-line-start':indexli==0,
          'pirm-line-green':indexli<=indexli1,
          'pirm-line-end':indexli==mainData.pathstages.length-1,
          'pirm-line-end-expand':(indexli==indexli1)&&(indexli==mainData.pathstages.length-1)
          }"
          ></div>
          <div class="clearfix pirm-tags-container ">
            <div v-for="(span,indexspan) in lidata.coursecategorys" :key="indexspan" class="floatl">
              <span @click="changeActiveSpan(indexli,indexspan,span.id,lidata.id)" :class="{'pirm-selected':indexli1==indexli&&indexspan1==indexspan}"
                class="font16pl3a3c50 pirm-tag pointer">
                {{span.name}}
              </span>
              <img v-if="indexspan!=lidata.coursecategorys.length-1" class="pirm-icon" src="../../assets/img/icons/Search-magnifier.svg" alt="">
            </div>
          </div>
          <transition name="fade">
            <!-- <div v-if="indexli==indexli1" class="pirm-heightnone ofhid"> -->
              <container  :myStyle="{}" v-if="indexli==indexli1" class="pirm-heightnone ofhid">
              <hot-course v-for="(item,index) in courseData" :key="index" :mainData="item"
               :myStyle="hotCourseStyle" :index="index"
              ></hot-course>
              </container>
            <!-- </div> -->
          </transition>
        </li>
      </ul>
    </div>
    <!-- <button></button> -->
  </div>
</template>

<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App',
        indexli1: -1,
        indexspan1: -1,
        hotCourseStyle:{
            outerStyle:{width:'216px','margin-right':'32px'},
            imgStyle:{height:'148px'},
            num:3
        },
        content: '',
        courseData:{}
      }
    },
    methods: {
      changeActiveSpan(indexli, indexspan,spanid, liid) {
        this.indexli1 = indexli;
        this.indexspan1 = indexspan;
        this.$ajax.get('tracks/path/detail/info?'+'home_show=false'+'&category_id='+spanid).then(
          res=>{
            this.courseData=this.$fn.addString(this.$myConst.httpUrl,res.data.data,['course_img','avatar'])
          }
        )
      }
    },
    created() {
      
    },
    props:{
      mainData:Object
    }
  }

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.path-info-right{
  width:752px;
  float: left;
  margin-left:80px;
}
  .pir-title-container {
    margin-bottom: 40px;
  }

  .pir-title {
    margin-bottom: 24px;
  }

  .tli {
    padding: 16px 0;
  }

  .pirm-dote {
    position: absolute;
    height: 8px;
    width: 8px;
    border-radius: 100px;
    vertical-align: middle;
    top:34px;
  }
  .pirm-dot-border-grey {
    background: #FFFFFF;
    border: 2px solid #D5DADF;
  }
  .pirm-dote-border-green {
    background: #FFFFFF;
    border: 2px solid #66BB6A;
  }
  .pirm-dote-solid-green {
    background: #66BB6A;
    border: 2px solid #66BB6A;
  }

  .pirm-tags-container {
    padding: 12px 0px;
  }

  .pirm-line {
    position: absolute;
    left: 5px;
    top:0px;
    width: 2px;
    height: 100%;
  }
  .pirm-line-top{
    position: absolute;
    left: 5px;
    top:0px;
    width: 2px;
    height: 40px;
  }
  .pirm-line-start{
    top:40px;
  }
  .pirm-line-end{
    height:40px;
    top:0px;
  }
  .pirm-line-end-expand{
    height: 100%;
    top:0px;
  }
  .pirm-line-grey {
    background: #D5DADF
  }
  
  .pirm-line-green {
    background: #66BB6A;
  }

  .pirm-tag {
    margin: 0 19px;
    padding: 4px 8px;
  }

  .pirm-icon {
    height: 12px;
    width: 12px;
  }

  .pirm-selected {
    color: white;
    background: #23B8FF;
  }

  .pirm-heightnone {
    margin-left: 22px;
    transition: all 0.3s ease;
  }

  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s ease-out;
  }

  .fade-enter,
  .fade-leave-to {
    opacity: 0;
  }

</style>

