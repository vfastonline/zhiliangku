<template>
  <div>
    <el-dialog :width="'650px'" :title="dialogTitle" :visible.sync="show">
      <div v-if="dialogType=='email'" class="email-container hc">
        <div><img class="hc block" src="./img/绿对勾.svg" alt=""></div>
        <div class="fontcenter">已向
        <span class="font16pr23b8ff">{{str}}</span>发送邮件</div>
        <div class="fontcenter"><span class="font16pl3a3c50"> 请登录邮箱点击确认链接完成验证</span></div>
        <div class="fontcenter">
          <el-button @click="goEmailHome(str)">去验证</el-button>
          <el-button @click="close()">以后再说</el-button>
        </div>
      </div>
      <div v-if="dialogType=='phone'" class="email-container hc">
        <div><img class="hc block" src="./img/绿对勾.svg" alt=""></div>
        <div class="fontcenter"><span>成功将手机号修改为{{str}}</span></div>
        <div class="fontcenter">
          <el-button @click="close()">完成</el-button>
        </div>
      </div>
    </el-dialog>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .email-container {
    width: 300px;
  }

</style>
<script>
  import brc from './resumeContentButton'
  import Bus from '../../assets/js/02_bus'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        show: false,
        str: '',
        dialogTitle: '',
        dialogType: ''
      }
    },
    props: {

    },
    methods:{
      close(){
        this.show=false
      },
       goEmailHome(email) {
        var hash = {
          'qq.com': 'http://mail.qq.com',
          'gmail.com': 'http://mail.google.com',
          'sina.com': 'http://mail.sina.com.cn',
          '163.com': 'http://mail.163.com',
          '126.com': 'http://mail.126.com',
          'yeah.net': 'http://www.yeah.net/',
          'sohu.com': 'http://mail.sohu.com/',
          'tom.com': 'http://mail.tom.com/',
          'sogou.com': 'http://mail.sogou.com/',
          '139.com': 'http://mail.10086.cn/',
          'hotmail.com': 'http://www.hotmail.com',
          'live.com': 'http://login.live.com/',
          'live.cn': 'http://login.live.cn/',
          'live.com.cn': 'http://login.live.com.cn',
          '189.com': 'http://webmail16.189.cn/webmail/',
          'yahoo.com.cn': 'http://mail.cn.yahoo.com/',
          'yahoo.cn': 'http://mail.cn.yahoo.com/',
          'eyou.com': 'http://www.eyou.com/',
          '21cn.com': 'http://mail.21cn.com/',
          '188.com': 'http://www.188.com/',
          'foxmail.coom': 'http://www.foxmail.com'
        };
        console.log(email)
        if (hash[email.split('@')[1]]) {
          window.open(hash[email.split('@')[1]])
          return
        } else {
          console.log('未知邮箱')
        }
      }
    },
    created() {
      Bus.$on('openDialogs',(res)=>{
        this.show=true;
        this.dialogType=res.type;
        this.dialogTitle=res.title;
        this.str=res.data
      } )
      Bus.$on('closeDialogs',(res)=>{
        this.show=false;
      })
    },
    components: {
      brc: brc
    }
  }

</script>
