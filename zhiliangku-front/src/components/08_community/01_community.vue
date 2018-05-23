<template>
  <div class="mw hc community">
    <myNavBar class="navbar" @haveClick="tagChange" :mainData="navbarData"></myNavBar>
    <questionList v-if="allData.length" :mainData="allData"></questionList>
    <noData v-else></noData>
    <mypager @pagerGetData='manipulationData' :key="pagerkey" :url="url" :additionData="params"></mypager>
  </div>
</template>
<style scoped>
  .community {
    padding-top: 52px;
  }

  .navbar {
    margin-bottom: 56px;
  }

</style>
<script>
  import myNavBar from './02_nav_bar'
  import questionList from './03_question_list'
  import mypager from '../00_common/06_pager'
  import noData from './04_have_no_data'
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
        ]
      }
    },
    props: {},
    methods: {
      manipulationData(res) {
        this.$fn.addString(this.$myConst.httpUrl, res.data.data, 'custom_user_avatar')
        this.allData = res.data.data;
      },
      tagChange(item) {
        this.changeParams(item.id);
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
    },
    created() {},
    components: {
      myNavBar: myNavBar,
      questionList: questionList,
      mypager: mypager,
      noData: noData
    }
  }

</script>
