<template>
  <div class="myform">
    <div class="myform-title font1_30_6">编辑教育经历</div>
    <div class="myform-body">
      <div class="item  the-input">
        <span class="tags">学校名称：</span>
        <el-input v-model="value0"></el-input>
      </div>
      <div class="item  the-input">
        <span class="tags">所学专业：</span>
        <el-input v-model="value1"></el-input>
      </div>
      <div class="item  the-input">
        <span class="tags">学历：</span>
        <el-input v-model="value2"></el-input>
      </div>
      <div class="item  the-input">
        <span class="tags">入学时间：</span>
        <el-date-picker format="yyyy 年 MM 月 " value-format="yyyy-MM" v-model="value3" type="month" placeholder="选择月">
        </el-date-picker>
      </div>
      <div class="item  the-input">
        <span class="tags">毕业时间：</span>
        <el-date-picker format="yyyy 年 MM 月 " value-format="yyyy-MM" v-model="value4" type="month" placeholder="选择月">
        </el-date-picker>
      </div>
      <div class="myform-body">
        <div class="item  the-input define">
          <span class="tags">在校经历：</span>
          <el-input v-model="value5"  type="textarea"></el-input>
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
import Bus from '../../assets/js/02_bus'
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
        wordnum: 0,
        maxwordnum: 300,
      }
    },
    props: {
      mainData: Array,
      url: String,
      editorIndex: Number
    },
    methods: {
      close() {
        this.$emit('close')
      },
      last(res){
         if (!res.data.err) {
            Bus.$emit('refreshResume', res.data.data)
          }
          this.close()
      },
      deleteInfo() {
        this.$post('/personal_center/resume/delete',{
          custom_user_id: localStorage.uid,
           resume_type: 'educationexperience',
           pk_id:this.mainData[this.editorIndex].id
        }).then(res=>{
          this.last(res)
        })
      },
      orgnizeData() {
        var data = {
          custom_user_id: localStorage.uid,
          resume_type: 'educationexperience',
          resume_info_dict: {
            "school": this.value0,
            "discipline": this.value1,
            "education": this.value2,
            "start_time": this.value3,
            "end_time": this.value4,
            "experience": this.changebr(this.value5),
          }
        }
        if (this.mainData[this.editorIndex]) {
          data.pk_id = this.mainData[this.editorIndex].id;
        }
        return data
      },
      submit() {
        this.$post(this.url, this.orgnizeData()).then(res => {
          console.log(res)
          this.last(res)
        })
      }
    },
    created() {
      if (this.editorIndex != -1) {
        this.initForm(this, this.mainData[this.editorIndex], ['school', 'discipline','education',
          'start_time', 'end_time', 'content'
        ], [
          'value0', 'value1', 'value2', 'value3', 'value4','value5'
        ])
        this.value5=this.changen(this.value5)
      }
      //  "educationexperiences": [{
      //       "discipline": "摄影",
      //       "school": "中国环境管理干部学院",
      //       "start_time": "2013",
      //       "experience": "没敢什么事。",
      //       "custom_user_id": 31,
      //       "end_time": "至今",
      //       "education": "大专",
      //       "id": 1
      //     }],
    },
    components:{
        rcb:rcb
    }
  }

</script>
<style lang="scss">
  @import "./style/01_resume_form.scss";

</style>
