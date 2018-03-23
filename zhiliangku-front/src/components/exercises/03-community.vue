<template>
  <div class="mainwidth incenter community">
    <myNavBar class="navbar" @haveClick="tagChange" :mainData="navbarData"></myNavBar>
    <questionList v-if="allData.length" :mainData="allData"></questionList>
    <noData v-else></noData>
    <mypager @pagerGetData='manipulationData' :key="pagerkey" :url="url" :addition="params"></mypager>
  </div>
</template>
< !-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
    .community {
      padding-top: 52px;
    }

    .navbar {
      margin-bottom: 56px;
    }

  </style>
  <script>
    import submitQuestion from '../videoDetail/submitQuestion.vue'
    import Bus from '../../assets/js/bus'
    import myNavBar from './04-navBar'
    import questionList from './05-questionList.vue'
    import mypager from './06-pager.vue'
    import noData from './07-haveNoData.vue'
    export default {
      name: 'HelloWorld',
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
          var uid = localStorage.uid;
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
                custom_user_id: uid
              }
            },
            4: () => {
              this.params = {
                participate_custom_user_id: uid
              }
            },
            5: () => {
              this.params = {
                follow_custom_user_id: uid
              }
            }
          }
          func[id]();
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
