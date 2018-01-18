<template>
  <div @click="go()" class="hotCourse floatl pointer" :style="outerStyle">
    <div  class="hc-imgContainer" :style="imgStyle">
      <img class="hcic-img" :src="mainData.course_img" alt="" :style="imgStyle">
      <div class="hcic-tag textellipsis">
        <el-button v-for="(item,index) in mainData.tech" v-if="index<2" :key="item" :style="buttonStyle">{{item}}</el-button>
      </div>
    </div>
    <ul class="hc-info" :style="barStyle">
      <li class="hci-li font14pl2C343B textellipsis">{{mainData.name}}</li>
      <li class="hci-li textellipsis">
        <img :src="mainData.avatar" alt="">
        <span class="font14prb2bbbf hcil-teachername">{{mainData.lecturer}}</span>
      </li>
    </ul>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        buttonStyle: {
          'height': '24px',
          'background': 'rgba(0,0,0,0.40)',
          'color': 'white',
          'border-radius': '12px',
          'padding': '0 16px',
          'border': 'none',
          'margin-right': '0px'
        },
        imgStyle: {},
        barStyle: {},
        outerStyle: {},
        myStyleData:{}
      };
    },
    methods:{
      go(){
        var url='/tracks/course/detail/?course_id='+this.mainData.id;
        if(localStorage.uid){
          url='/tracks/course/detail/?course_id='+this.mainData.id+"&custom_user_id="+localStorage.uid;
        }
        window.location.href=url;
      }
    },
    props: {
      mainData: Object,
      myStyle: Object,
      index: Number,
    },
    created() {
      
      // 此处是为了实现index是特定num倍数的时候没有margin-right
       this.myStyleData=this.deepCopy(this.myStyle);
        if (this.myStyle) {
        if (this.myStyle.num) {
          if (!((this.index + 1) % this.myStyle.num)) {
            if (this.myStyle['outerStyle']['margin-right']) {
              this.myStyleData[['outerStyle']]['margin-right']='0';
            }
          }
        }
      }
      this.$fn.initStyle(this.$vueself(), 'myStyleData', ['imgStyle', 'barStyle', 'outerStyle'])
      // console.log(this)
    }
  };

</script>

<style lang="scss">
  .hotCourse {
    transition: box-shadow 0.3s ease;
    margin-bottom: 6px;
    z-index: 1;
  }

  .hotCourse:hover {
    box-shadow: 0 0 10px 5px rgba(99, 117, 138, 0.10);
    z-index: 2;
  }

  .hc-imgContainer,
  .hcic-img {
    // width: 276px;
    width:100%;
    height: 153px;
    position: relative;
  }

  .hcic-tag {
    // width: 276px;
    box-sizing: border-box;
    height: 24px;
    padding-left: 8px;
    position: absolute;
    left: 0px;
    bottom: 7px;
    button {
      margin-right: 8px;
    }
  }

  // .hc-info {
  //   width: 276px;
  //   height: 80px;
  // }

  .hci-li {
    height: 40px;
    line-height: 40px;
    margin-left: 16px;
    img {
      width: 32px;
      height: 32px;
      border-radius: 16px;
      vertical-align: middle;
    }
  }

</style>
