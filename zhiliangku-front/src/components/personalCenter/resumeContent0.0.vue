<template>
  <div class="myform">
    <div class="myform-title font20pl3a3c50">编辑个人信息</div>
    <div class="myform-body">
      <div class="item  the-input">
        <span class="tags">姓名：</span>
        <el-input v-model="value0"></el-input>
      </div>
      <div class="item  the-input">
        <span class="tags">生日：</span>
        <el-date-picker v-model="value1" type="month" placeholder="选择月">
        </el-date-picker>
      </div>
      <div class="item  the-input">
        <span class="tags">性别：</span>
        <el-select v-model="value2">
          <el-option v-for="(item,index) in sexoption" :key="index" :value="item" :label="item"></el-option>
        </el-select>
      </div>
      <div class="item  the-input">
        <span class="tags">工作年限：</span>
        <el-select v-model="value3">
          <el-option v-for="(item,index) in experienceoption" :key="index" :value="item" :label="item"></el-option>
        </el-select>
      </div>
      <div class="item  the-input">
        <span class="tags">最高学历：</span>
        <el-select v-model="value4">
          <el-option v-for="(item,index) in degreeoption" :key="index" :value="item" :label="item"></el-option>
        </el-select>
      </div>
      <div class="item  the-input">
        <span class="tags">求职状态：</span>
        <el-select v-model="value5">
          <el-option v-for="(item,index) in stateoption" :key="index" :value="item" :label="item"></el-option>
        </el-select>
      </div>
      <div class="item  the-input">
        <span class="tags">首要意向：</span>
        <el-select v-model="value6">
          <el-option v-for="(item,index) in intentoption" :key="index" :value="item" :label="item"></el-option>
        </el-select>
      </div>
    </div>
    <rcb @cancel="close" @submit="submitIfon" :layer="['submit','cancel']"></rcb>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
<script>
import Bus from '../../assets/js/bus'
  import rcb from './resumeContentButton'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        value0: '',
        value1: '',
        value2: '',
        value3: '',
        value4: '',
        value5: '',
        value6: '',
        sexoption: ['男', '女'],
        experienceoption: ['实习生', '1年', '2年', '3年', '4年', '5年', '6年', '7年', '8年', '9年', '10年', '10年以上'],
        degreeoption: ['中专及以下', '高中', '专科', '本科', '研究生', '博士'],
        stateoption: ['离职-随时到岗', '在职-暂不考虑', '在职-考虑机会', '在职-月内到岗'],
        intentoption: [''],
        url:'/personal_center/resume/update'
      }
    },
    props:{
      mainData:Object
    },
    methods: {
      close() {
        this.$emit('close')
      },
      submitIfon() {
        if(JSON.stringify(this.mainData)=="{}"){
          this.url='/personal_center/resume/add';
        }
        this.$post(this.url,{
          resume_type: 'resume',
          pk_id:this.mainData.id,
          resume_info_dict: {
            name: this.value0,
            sex: this.value2,
            years_of_service: this.value3,
            education: this.value4,
            status: this.value5,
            career_objective_id: this.value6,
          },
          custom_user_id: localStorage.uid
        }).then(res=>{
          if(!res.data.err){
            Bus.$emit('refreshResume')
          }
          this.close()
          console.log(res)
        })
      }
    },
    components: {
      rcb: rcb
    }
  }

</script>
<style lang="scss">
  @import "../../style/scss/components/resumeForm.scss";

</style>
