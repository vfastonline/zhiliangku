<template>
  <div class="myform">
    <div class="myform-title font20pl3a3c50">编辑工作经历</div>
    <div class="myform-body">
      <div class="item  the-input">
        <span class="tags">公司名称：</span>
        <el-input v-model="value0"></el-input>
      </div>
      <div class="item  the-input">
        <span class="tags">公司名称：</span>
        <el-input v-model="value1"></el-input>
      </div>
      <div class="item  the-input">
        <span class="tags">入职时间：</span>
        <el-date-picker v-model="value2" type="month" placeholder="选择月">
        </el-date-picker>
      </div>
      <div class="item  the-input">
        <span class="tags">离职时间：</span>
        <el-date-picker v-model="value3" type="month" placeholder="选择月">
        </el-date-picker>
      </div>
      <div class="myform-body">
        <div class="item  the-input">
          <span class="tags">工作内容：</span>
          <el-input v-model="value4"  type="textarea"></el-input>
          <div class="word-indecator font14pl5A646E">{{wordnum}}/{{maxwordnum}}</div>
        </div>
      </div>
    </div>
    <rcb @delete="deleteInfo" @cancel="close" @submit="submit" :layer="['delete','submit','cancel']"></rcb>
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
        wordnum: 0,
        maxwordnum: 1600,
        url:'/personal_center/resume/update',
      }
    },
    methods:{
      close(){
        this.$emit('close')
      },
      deleteInfo(){

      },
      submit(){
        if(!this.mainData.length){
          this.url='/personal_center/resume/add'
        }
        this.$post(this.url,{
          custom_user_id: localStorage.uid,
          resume_type: 'resume',
          resume_info_dict:{}
        }).then(res=>{
          console.log(res)
          Bus.$emit('refreshResume')
        })
      }
    },
    components:{
      rcb:rcb
    }
  }

</script>
<style lang="scss">
  @import "../../style/scss/components/resumeForm.scss";

</style>
