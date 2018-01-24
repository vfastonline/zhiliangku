<template>
  <div class="match-rate-part-container rise">
    <courseli :config="{tag:'匹配度：',buttonStr:'查看详情'}" @clickButton="lookInfo()" :mainData="courseData"></courseli>
    <div v-if="show" class="mrpc-additional-list">
      <div class="marginbottom24">
        <span class="font16pl3a3c50 inlineblock mrpc-salary">{{otherData.treatment_range}}</span>
        <span class="font14pr424242">{{otherData.company_info}}</span>
      </div>
      <ul>
        <li v-for="(item,index) in otherData.claim_list" :key="index" class="marginbottom24 textellipsis">
          <img v-if="item.checked==false" class="mrpc-conform" src="../../assets/img/icons/个人中心和积分商城图标/勾选框_空选.svg" alt="">
          <img v-if="item.checked==true" class="mrpc-conform textellipsis" src="../../assets/img/icons/个人中心和积分商城图标/勾选框_选中.svg" alt="">
          <span class="textellipsis">{{item.matches}}</span>
        </li>
      </ul>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
  import courseli from './courseLi'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        show: false,
        courseData: {
          job: true
        },
        otherData: {
          "company_info": "移动互联网，游戏/上市公司/北京/全职",
          "treatment_range": "6K-8k",
          "claim_list": [{
              "matches": "1-3年工作经验",
              "checked": 1
            },
            {
              "matches": "本科及一上",
              "checked": 1
            }
          ]
        }
      }
    },
    props: {
      mainData: Object
    },
    methods: {
      getData() {
        this.$get('/personal_center/job/post/match/detail?custom_user_id=' + localStorage.uid +
          '&post_id=' + this.mainData.post_id).then(res => {
          this.otherData = res.data.data;
          this.show=!this.show
        })
      },
      lookInfo() {
        this.getData()
      }
    },
    created() {
      this.courseData = this.mainData;
      this.courseData.job = true;
    },
    components: {
      courseli: courseli
    }
  }

</script>
<style>
  .match-rate-part-container,
  .match-rate-part-inner {
    padding: 16px 24px;
    background: white;
  }

  .match-rate-part-inner {
    height: 100px;
  }

  .mrpc-company-logo {
    height: 100px;
    width: 100px;
  }

  .mrpc-match-rate {
    margin-right: 32px;
  }

  .mrpc-company-info {
    margin-left: 130px;
  }

  .mrpc-progress .el-progress-bar__inner {
    border-radius: 0px
  }

  .mrpc-progress .el-progress-bar__outer {
    border-radius: 0;
  }

  .mrpc-company-line2 {
    /* line-height: 38px; */
    height: 40px;
  }

  .mrpc-job-name,
  .mrpc-progress {
    width: 340px;
  }

  .mrpc-salary {
    margin-right: 24px;
  }

  .mrpc-conform {
    vertical-align: middle;
    margin-right: 21px;
  }

</style>
