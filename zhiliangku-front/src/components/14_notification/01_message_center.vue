<template>
  <div class="main_antainner">
    <div class="mw hc">
      <div class="nav_bar mw">
        <span class="dib font1_20_6">
          <span v-for="(item,index) in tabArr" :key="item.name" class="dib tab_bar cp" :class="{'active': item.active}"
                @click="navToggle(item,index)">{{item.name}}</span>
        </span>
        <span class="font1_20_6 dib tab_bar_right cp" @click="flagAllMessage()">
          全部标记为已读
        </span>
      </div>
      <message v-for="item in main_data" :key="item.id" :main_data="item"></message>
      <div v-if="!main_data.length" class="mw ftc hc">
        <p class="font1_20_9">暂无消息</p>
      </div>
    </div>
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
    // 此处代码结构不合理，感觉被江舟坑了，页码组件干嘛不和nav放在父级呢，这样子不伦不类的。
    data() {
      return {
        isFlag: false,
        tabArr: [
          {active: true, name: "最新", have_read: "0"},
          {active: false, name: "已读", have_read: "2"},
          {active: false, name: "未读", have_read: "1"},
        ]
      }
    },
    props: {
      main_data: {}
    },
    created() {
    },
    methods: {
      flagAllMessage() {
        var obj = {
          whole: 1
        }
        if (!this.isFlag) {
          this.$post("/notification/markasread", obj).then(res => {
            if (!res.data.err) {
              this.isFlag = true;
              this.main_data.forEach(el => {
                el.have_read = true
              })
              this.$fn.showNotice(this, '您已操作成功', 'success')
            }
          })
        } else {
          this.$fn.showNotice(this, '请求正在路上~')
        }
      },
      navToggle(item, index) {
        this.isActive(index);
        if (item.have_read) {
          var obj = {
            have_read: item.have_read
          }
          Bus.$emit("additionEnter", obj)
        }
      },
      isActive(index) {
        this.tabArr.forEach(el => {
          el.active = false
        })
        this.tabArr[index].active = true
      }
    },

  }
</script>

<style scoped>
  .nav_bar {
    display: flex;
    justify-content: space-between;
    padding: 50px 0 30px;
  }

  .tab_bar {
    padding: 5px 30px;
    margin-right: 20px;
  }

  .tab_bar_right {
    padding: 5px 40px 5px 0;
  }

  .main_antainner {
    min-height: 75vh;
    background-color: #fafafa;
  }

  .active {
    background-color: #00bcd4;
    color: #ffffff;
  }
</style>
