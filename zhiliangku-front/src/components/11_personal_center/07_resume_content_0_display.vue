<template>
  <div id="anchor0">
    <div class="rc-pi resumewidth hc">
      <div class="rc-pi-container1">
        <div class="rc-pi-content clearfix r">
          <el-upload class="rc-pic-img fl round" :action="orgnizeUrl()" :show-file-list="false"
                     :on-success="handleAvatarSuccess"
                     :before-upload="beforeAvatarUpload">
            <img class="rc-pic-img fl round" v-if="imgsrc" :src="imgsrc" alt="">
          </el-upload>
          <div class="rc-pic-word">
            <div class="rc-pic-word-0">
              <span class="font1_18_3 weight">{{mainData.name}}</span>
              <img class="resume-sex-icon" v-if="mainData.sex=='女'" src="./img/简历_性别女.svg" alt="">
              <img class="resume-sex-icon" v-if="mainData.sex=='男'" src="./img/简历_性别男.svg" alt="">
              <span class="font1_18_6">{{age()}}岁</span>
            </div>
            <div class="rc-pic-word-1">
              <span class="font1_18_6">{{mainData.status}}</span>
              <span class="font1_18_6">{{mainData.position}}</span>
              <span class="font1_18_6">{{mainData.company}}</span>
            </div>
          </div>
          <div @click="ifshowEditor" class="cp rc-pic-editor">
            <tag_0 class="tag_edit">
              <img class="vs icon_01" src="./img/编辑icon.png" alt="">
              <span class="font1_20_9">编辑</span>
            </tag_0>
          </div>
        </div>
      </div>
      <div class="rc-pi-container2">
        <tag_0>
          <img class="vs icon_01" src="./img/01_briefcase.svg" alt="">
          <span class="font1_20_6">{{mainData.years_of_service||'尚未填写'}}</span>
        </tag_0>
        <tag_0>
          <img class="vs icon_01" src="./img/简历_学士帽.svg" alt="">
          <span class="font1_20_6">{{mainData.education||'尚未填写'}}</span>
        </tag_0>
        <tag_0>
          <img class="vs icon_01" src="./img/简历_小人.svg" alt="">
          <span class="font1_20_6">{{mainData.status||'尚未填写'}}</span>
        </tag_0>
        <tag_0>
          <img class="vs icon_01" src="./img/简历_钱币.svg" alt="">
          <span class="font1_20_6">{{mainData.expect_salary||'尚未填写'}}</span>
        </tag_0>
      </div>
    </div>
    <el-dialog
      title="提示"
      :width="'970px'"
      :visible.sync="showeditor">
      <editor :mainData="mainData" :applyData="applyData" @close="editor"></editor>
    </el-dialog>
  </div>
</template>
<style>
</style>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
  import funcs from '../../assets/js/01_other/01_dispatch.js'
  import editor from './07_resume_content_0_modify'
  import tag_0 from './08_tag_0'
  import {Dialog} from 'element-ui'
  import Vue from 'vue'

  Vue.use(Dialog)

  export default {
    name: 'HelloWorld',
    data() {
      return {
        showeditor: false,
        imgsrc: '',
        actionUrl: ''
      }
    },
    watch: {
      mainData: function (value) {
        this.imgsrc = this.$myConst.httpUrl + this.mainData.avatar;
      },
      showeditor: function () {

      }
    },
    methods: {
      ifshowEditor() {

        if (!this.applyData.length) {
          funcs.showNotice(this, '尚未添加求职意向，请先完善求职意向信息,然后操作此项', 'info')
          return
        }
        this.showeditor = !this.showeditor;
      },
      editor() {
        this.showeditor = !this.showeditor;
      },
      orgnizeUrl() {
        var str = this.$myConst.httpUrl + '/customuser/change/avatar?custom_user_id=' + localStorage.uid +
          '&avatar_type=resume_avatar';
        return str
      },
      handleAvatarSuccess(res, file) {
        this.imgsrc = this.$myConst.httpUrl + res.avatar;
        // this.imgsrc = URL.createObjectURL(file.raw);
      },
      beforeAvatarUpload(file) {
        const isJPG = file.type === 'image/jpeg';
        const isLt2M = file.size / 1024 / 1024 < 2;

        if (!isJPG) {
          this.$message.error('上传头像图片只能是 JPG 格式!');
        }
        if (!isLt2M) {
          this.$message.error('上传头像图片大小不能超过 2MB!');
        }
        return isJPG && isLt2M;
      },
      age() {
        var year = new Date().getFullYear();
        if (this.mainData.birthday) {
          var brith = this.mainData.birthday.substr(0, 4)
          return year - brith;
        }
        return '未知'
      }
    },
    components: {
      editor: editor,
      tag_0: tag_0
    },
    props: {
      mainData: Object,
      applyData: Array,
    },
    created() {
      console.log(this.mainData)
    }
  }

</script>
<style scoped>

  .rc-pi {
    padding-bottom: 24px;
    margin-bottom: 48px;
  }

  .rc-pi-container1 {
    padding: 10px 0;
    border-bottom: 1px solid #e1e1e1;
  }

  .rc-pi-content {
  }

  .resume-sex-icon {
    margin: 0 38px;
  }

  .rc-pi-container2 {
    padding-top: 16px;
    padding-right: 15px;
    display: flex;
    justify-content: space-between;
  }

  .rc-pi-content {
    position: relative;
  }

  .rc-pic-img {
    height: 120px;
    width: 120px;
    border-radius: 50%;
  }

  .rc-pic-word {
    margin-left: 150px;
    padding-top: 28px;
  }

  .rc-pic-word-0 {
    margin-bottom: 22px;
  }

  .rc-pic-word-1 {
  }

  .rc-pic-editor {
    position: absolute;
    right: 0;
    bottom: 0;
    padding-right: 18px;
  }

</style>
