<template>
  <div class="path-info-right">
    <div class="pir-title-container">
      <div class="font20pl3a3c50 pir-title">Linux运维工程师</div>
      <div class="font14prb2bbbf">22门课程</div>
    </div>
    <div class="pir-main-content">
      <ul>
        <li v-for="(lidata,indexli) in maindata" :key="indexli" class="tli tli1 relative clearfix ofhid">
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
          'pirm-line-end':indexli==maindata.length-1,
          'pirm-line-end-expand':(indexli==indexli1)&&(indexli==maindata.length-1)
          }"
          ></div>
          <div class="clearfix pirm-tags-container ">
            <div v-for="(span,indexspan) in lidata.spans" :key="indexspan" class="floatl">
              <span @click="changeActiveSpan(indexli,indexspan,span)" :class="{'pirm-selected':indexli1==indexli&&indexspan1==indexspan}"
                class="font16pl3a3c50 pirm-tag pointer">
                {{span}}
              </span>
              <img v-if="indexspan!=lidata.spans.length-1" class="pirm-icon" src="../../assets/img/icons/Search-magnifier.svg" alt="">
            </div>
          </div>
          <transition name="fade">
            <div v-if="indexli==indexli1" class="pirm-heightnone ofhid">
              {{content}}
            </div>
          </transition>
        </li>
      </ul>
    </div>
    <button></button>
  </div>
</template>
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
<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App',
        indexli1: -1,
        indexspan1: -1,
        maindata: [{
            spans: ['Linux基础']
          },
          {
            spans: ['网络管理', '软件安装', '权限管理', '服务管理']
          },
          {
            spans: ['shell基础', 'shell实战']
          },
          {
            spans: ['安全应用', '网络服务', '服务搭建']
          }
        ],
        content: ''
      }
    },
    methods: {
      changeActiveSpan(indexli, indexspan, span) {
        this.content = span;
        this.indexli1 = indexli;
        this.indexspan1 = indexspan;
      }
    },
    created() {
      function CallBack() {
        var arr = [],
          i = 0;
        this.add = function (func) {
          arr.push(func);
        }

        this.run = function (num) {
          var fun = function () {
            if (i < arr.length) {
              arr[i++](fun)
            }
          }
          fun();
        }
      }

      var aa = new CallBack()

      aa.add(function (next) {
        console.log('0');
        next();
      })

      aa.add(function (next) {
        setTimeout(function () {
          console.log('1');
          next();
        }, 3000);
      })
      aa.add(function (next) {
        console.log('2');
        next();
      })
      aa.add(function (next) {
        setTimeout(function () {
          console.log('3');
          next();
        }, 1000);
      })

      console.log(new Date())
      aa.run()
      console.log(aa)
    }
  }

</script>
