<template>
  <div class="mainwidth incenter">
    <ul>
      <li v-for="(lidata,indexli) in maindata" :key="indexli" class="tli tli1 ">
        <div class="clearfix">
          <div v-for="(span,indexspan) in lidata.spans" :key="indexspan" class="floatl">
            <span @click="changeActiveSpan(indexli,indexspan)" :class="{'red':indexli1==indexli&&indexspan1==indexspan}">
              {{span}}
            </span>
            <img src="../../assets/img/icons/Search-magnifier.svg" alt="">
          </div>
        </div>
          <div :class="{'heightnone':indexli==indexli1}" class="box">
            {{indexspan1}}
          </div>
      </li>
    </ul>
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
        maindata: [{
            spans: [1, 2, 3, 4]
          },
          {
            spans: [1, 2, 3]
          },
          {
            spans: [1, 2, 3, 4, 5]
          },
          {
              spans:[1,2,3,4,5,6,7]
          }
        ],
        show:false,
        h:false
      }
    },
    methods: {
      changeActiveSpan(indexli, indexspan) {
        this.indexli1 = indexli;
        this.indexspan1 = indexspan;
        console.log(indexli)
        console.log(indexspan)
      }
    }
  }
  
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.heihei{
    height:60px;
    background:skyblue;
    transition: all 0.5s ease 1s;
}
.display{
    height:0px;
}
.height{
    height:100px;
}
  .box {
    height:0px;
    background: pink;
    transition: all 0.3s ease;
    overflow: hidden;
  }
  .red {
    color: red;
  }
  .heightnone{
      height: 100px;
  }
</style>


