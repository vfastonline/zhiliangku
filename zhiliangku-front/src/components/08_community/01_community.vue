<template>
  <div class="mw hc community">
    <myNavBar class="navbar" @haveClick="tagChange"  @searchClick="getSearch" :mainData="navbarData"></myNavBar>
    <questionList v-if="allData.length" :mainData="allData"></questionList>
    <noData v-else></noData>
    <mypager ref="pager" @pagerGetData='manipulationData' :url="url" :additionData="params"></mypager>
    <fixedButton class="fixedButton" text="我要提问" @click.native="dialogVisible=true">
        <!-- <img src="" alt="" style="background-color:red"> -->
        <span>？</span>
    </fixedButton>
    <el-dialog
      width='650px'
      :visible.sync="dialogVisible">
      <submitQuestion id="question_container" @close="dialogVisible=false" :where="'community'" @submit_success="over"></submitQuestion>
    </el-dialog>
  </div>
</template>
<style>
  .community .el-dialog__body{
    padding: 0px;
  }
  .community .el-dialog__header{
    display: none;
  }
</style>
<style scoped>
  .community {
    padding-top: 70px;
  }

  .navbar {
    margin-bottom: 30px;
    font-weight: bold;
  }
  .fixedButton {
    position:fixed;
    top:390px;
    left: 50%;
    margin-left: 600px;
  }

</style>
<script>
  import Vue from 'vue'
  import myNavBar from './02_nav_bar'
  import questionList from './03_question_list'
  import mypager from '../00_common/06_pager'
  import noData from './04_have_no_data'
  import fixedButton from './05_fixed_button'
  import {Dialog} from 'element-ui'
  import submitQuestion from '../07_video_detail/07_submit_question'
  Vue.use(Dialog)
  export default {
    name: 'community',
    data() {
      return {
        allData: {},
        url: '/community/faq/list/info',
        params: {},
        pagerkey: '',
        navbarData: [{
          id: 0,
          label: '最新'
        },
          {
            id: 1,
            label: '已解决'
          },
          {
            id: 2,
            label: '未解决'
          },
          {
            id: 3,
            label: '我的提问'
          },
          {
            id: 4,
            label: '我参与的'
          },
          {
            id: 5,
            label: '我关注的'
          },
        ],
        searchTag:{},
        dialogVisible: false
      }
    },
    props: {},
    methods: {
      manipulationData(res) {
        this.$fn.addString(this.$myConst.httpUrl, res.data.data, 'custom_user_avatar')
        this.allData = res.data.data;
        // console.log(this.allData);
      },
      tagChange(item) {
        this.changeParams(item.id);
      },

      getSearch(searchData) {
        if(searchData) {
          this.url="community/faq/list/info"
          this.$set(this.params,'title',searchData)
          // console.log(this.params)
        }

      },
      changeParams(id) {
        var func = {
          0: () => {
            this.params = {}
          },
          1: () => {
            this.params = {
              status: 1
            }
          },
          2: () => {
            this.params = {
              status: 0
            }
          },
          3: () => {
            this.params = {
              ask: 1
            }
          },
          4: () => {
            this.params = {
              participate: 1
            }
          },
          5: () => {
            this.params = {
              follow: 1
            }
          }
        }
        func[id]();
        this.params
      },
      over() {
        this.dialogVisible = false;
        this.$refs.pager.upData()
      },
    },
    created() {},
    components: {
      myNavBar: myNavBar,
      questionList: questionList,
      mypager: mypager,
      noData: noData,
      fixedButton:fixedButton,
      submitQuestion: submitQuestion
    }
  }

</script>
