<template>
  <div class="myform">
    <div class="myform-title font20pl3a3c50">编辑项目经验</div>
    <div class="myform-body">
      <div class="item  the-input">
        <span class="tags">项目名称：</span>
        <el-input v-model="value0"></el-input>
      </div>
      <div class="item  the-input">
        <span class="tags">项目角色：</span>
        <el-input v-model="value1"></el-input>
      </div>
      <div class="item  the-input">
        <span class="tags">项目URL：</span>
        <el-input v-model="value2"></el-input>
      </div>
      <div class="item  the-input">
        <span class="tags">开始时间：</span>
        <el-date-picker v-model="value3" type="month" placeholder="选择月">
        </el-date-picker>
      </div>
      <div class="item  the-input">
        <span class="tags">结束时间：</span>
        <el-date-picker v-model="value4" type="month" placeholder="选择月">
        </el-date-picker>
      </div>
        <div class="item  the-input">
          <span class="tags">项目描述：</span>
          <el-input v-model="value5"  type="textarea"></el-input>
          <div class="word-indecator font14pl5A646E">{{wordnum0}}/{{maxwordnum0}}</div>
        </div>
        <div class="item  the-input">
          <span class="tags">项目业绩：</span>
          <el-input v-model="value5"  type="textarea"></el-input>
          <div class="word-indecator font14pl5A646E">{{wordnum1}}/{{maxwordnum1}}</div>
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
        value5:'',
        wordnum0: 0,
        maxwordnum0: 300,
        wordnum1: 0,
        maxwordnum1: 300,
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
