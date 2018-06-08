<template>
  <div class="main_antainner">
    <div class="nav_bar mw hc">
        <span class="dib font1_20_6">
          <span class="dib tab_bar cp" @click="navToggle">最新</span>
          <span class="dib tab_bar cp"  @click="navToggle(1)">已读</span>
          <span class="dib tab_bar cp"  @click="navToggle(2)">未读</span>
        </span>
      <span class="font1_20_6 dib tab_bar_right cp" @click="flagAllMessage()">
          全部标记为已读
        </span>
    </div>
    <message v-for="item in main_data" :key="item.id" :main_data="item"></message>
  </div>
</template>

<script>
  import message from './02_message_unit'
  import Bus from '../../assets/js/02_bus'

  export default {
    name: "01_message_center",
    components: {
      message: message
    },
    data() {
      return {
        active: false
      }
    },
    props: {
      main_data: {}
    },
    created() {
      console.log(this.$props)
    },
    methods: {
      flagAllMessage() {
        var obj={
          whole: 1
        }
          this.$post("/notification/markasread",obj).then(res => {
            if (res.data.msg=="success") {
              this.main_data.forEach(el => {
                el.have_read=true
              })
            }
          })
      },
      navToggle(params) {
        if(params){
          this.active="true"
          var obj={
            have_read: params
          }
          Bus.$emit("additionEnter",obj)
        } 

      }
    },

  }
</script>

<style scoped>
  .nav_bar {
    display: flex;
    justify-content: space-between;
    padding:50px 0 30px;
  }
  .tab_bar {
    padding: 5px 30px;
    margin-right:20px;
  }
  .tab_bar_right {
    padding: 5px 40px 5px 0;
  }
  .main_antainner {
    min-hieght:75vh;
    background-color:#fafafa;
  }
  .active {
    background-color: #00bcd4;
  }
</style>
