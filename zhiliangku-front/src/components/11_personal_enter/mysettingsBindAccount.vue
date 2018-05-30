<template>
  <div class="settings-container incenter">
    <div class="setting-item relative">
      <div class="tag font14pl3a3c50">邮箱：</div>
      <div class="set-content">
        <div class="sc-info-li">
          <span class="font14pr424242">{{mainData.email}} </span>
        </div>
        <span @click="dialogsFormOpen('email','修改邮箱')"
         class="bind-button font14pr424242 pointer">{{mainData.emil?'更改':'绑定'}}</span>
      </div>
    </div>
    <div class="setting-item relative">
      <div class="tag font14pl3a3c50">手机号：</div>
      <div class="set-content">
        <div class="sc-info-li">
          <span class="font14pr424242">{{mainData.phone}} </span>
        </div>
        <span @click="dialogsFormOpen('phone','修改手机号')"
         class="bind-button font14pr424242 pointer">{{mainData.phone?'更改':'绑定'}}</span>
      </div>
    </div>
    <div class="setting-item relative">
      <div class="tag font14pl3a3c50">微信：</div>
      <div class="set-content">
        <div class="sc-info-li">
          <span v-if="mainData.weixin" class="font14pr424242"> 可用于直接登录，与内容分享</span>
          <span v-else class="font14pr424242">您已绑定微信</span>
        </div>
        <span @click="bindWeixin()" class="bind-button font14pr424242 pointer">{{mainData.weixin?'更改':'绑定'}}</span>
      </div>
    </div>
    <dialogs></dialogs>
    <dialogsForm  :needpassword="mainData.needpassword"></dialogsForm>
  </div>
</template>
<script>
  import Bus from '../../assets/js/bus'
  import rcb from './resumeContentButton'
  import dialogs from './dialogs'
  import dialogsForm from './dialogsForm'
  let Base64 = require('js-base64').Base64;
  export default {
    name: 'HelloWorld',
    data() {
      return {
        str1: '更改',
        str2: '更改',
        str3: '立即绑定',
        mainData:{},
        wxBase64Url:'',
        Base64:Base64
      }
    },
    methods:{
      bindWeixin(){
        window.location.href=this.wxBase64Url;
      },
      dialogsFormOpen(type,title){
        Bus.$emit('dialogsFormOpen',{type:type,title:title})
      },
      haveChangPhone(phone){
        this.mainData.phone=phone
      },
      getData(){
        this.$get('/personal_center/personal_settings/useraccount?custom_user_id='+localStorage.uid).then(res=>{
        this.mainData=res.data.data;
        
        this.mainData.needpassword=false;
        if(!this.mainData.phone&&!this.mainData.email){
          this.mainData.needpassword=true;
        }
        var arr=['phone','email','qq','weixin'];
        arr.forEach(ele=>{
          if(!this.mainData[ele]){
            this.mainData[ele]='暂未绑定'
          }
        })
      })
      }
    },
    created(){
      this.getData()
      Bus.$on('countDataChange',res=>{
        this.getData()
      })
      this.wxBase64Url =
        'https://open.weixin.qq.com/connect/qrconnect?appid=wx7c9efe7b17c8aef2&redirect_uri=http%3a%2f%2fwww.zhiliangku.com%2fcustomuser%2fweixin%2flogin&response_type=code&scope=snsapi_login&state=' +
        this.Base64.encode(window.location.href) + '#wechat_redirect';
    },
    components: {
      rcb: rcb,
      dialogs: dialogs,
      dialogsForm:dialogsForm
    }
  }
</script>
<style lang="scss">
  .sc-info-li {
    background: white;
    line-height: 42px;
    height: 42px;
    padding: 0 100px 0 32px;
  }

  .dialog-li {
    width: 570px;
  }

  .input-li {
    width: 473px;
    margin-left: 94px;
    .tags {
      position: absolute;
      width: 85px;
      top: 50%;
      text-align: right;
      left: -100px;
      transform: translate(0, -50%)
    }
  }

</style>
<style lang='scss' scoped>
  @import '../../style/scss/components/mysettings.scss';

</style>
