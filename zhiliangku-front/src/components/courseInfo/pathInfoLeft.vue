<template>
  <div class="floatl path-info-left">
    <img class="pil-img" v-lazy="mainData.path_img" alt="">
    <div class="pil-button-container relative">
      <span v-if="!mainData.participate" class="pilb-button font16pr23b8ff pointer " @click="partin()">参加该路径</span>
      <span v-else class="pilb-button-already font16pr23b8ff  ">已参加该路径</span>
    </div>
    <ul v-if="mainData.participate" class="pil-ul">
      <li class="pilu-li-1 font14pr3a3c50">路径介绍</li>
      <li class="pilu-li-2 font14pl5A646E">{{mainData.desc}}</li>
      <li class="pilu-li-3">
        <div class="pilu-tag">
          <div class="fontcenter pilu-tag-green">
            <span class="font20pm2a0000">{{mainData.learn_time_consum.split('分')[0]|info}}</span>
            <!-- <span v-if="mainData.learn_time_consum" class="font14pm2a0000">分钟</span> -->
          </div>
          <div class="fontcenter font14pl5A646E">学习耗时</div>
        </div>
        <div class="pilu-tag">
          <div class="fontcenter pilu-tag-green">
            <span class="font20pm2a0000">{{mainData.path_complete_schedule|info}}</span>
            <span v-if="mainData.path_complete_schedule" class="font14pm2a0000">%</span>
          </div>
          <div class="fontcenter font14pl5A646E">路线完成进度</div>
        </div>
        <div class="pilu-tag">
          <div class="fontcenter pilu-tag-green">
            <span v-if="mainData.courses_count" class="font20pm2a0000">
              {{mainData.complete_number}}</span>
              <span v-else class="font20pm2a0000">
              暂无信息</span>
            <span v-if="mainData.courses_count" class="font14pm2a0000">/{{mainData.courses_count}}</span>
          </div>
          <div class="fontcenter font14pl5A646E">完成节数</div>
        </div>
      </li>
    </ul>
  </div>
</template>
<script>
  import VueLazyLoad from 'vue-lazyload'
  Vue.use(VueLazyLoad, {})
  export default {
    data() {
      return {

      }
    },
    props: {
      mainData: Object
    },
    filters: {
      info(value) {
        if(value==='0')return value;
        if (value) return value;
        return '暂无信息'
      },

    },
    methods: {
      partin() {
        if (this.mainData.participate) {
          return
        }
        this.$post('/tracks/participate/path', this.orgnaizData()).then(res => {
          this.mainData.participate = true;
        })
      },
      orgnaizData() {
        var obj = {};
        obj.path_id = this.mainData.id;
        if (localStorage.uid) {
          obj.custom_user_id = localStorage.uid;
        }
        return obj
      }
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .path-info-left {
    width: 320px;
  }

  .pil-img {
    height: 186px;
    width: 320px;
  }

  .pil-button-container {
    height: 102px;
    display: flex;
    justify-content: center;
    align-items: center
  }

  .pilb-button {
    /* background:pink; */
    padding: 8px 40px;
    border: 2px solid #23B8FF;
  }

  .pilb-button-already {
    padding: 8px 40px;
    border: 2px solid #EEF0F2;
    color: #EEF0F2;
  }

  .pilu-li-1,
  .pilu-li-2 {
    margin: 16px 0;
  }

  .pilu-li-3 {
    display: flex;
    justify-content: space-between;
    margin: 32px 0;
  }

  .pilu-tag-green {
    padding: 8px 0;
  }

  .pilu-tag {
    display: inline-block;
  }

</style>
