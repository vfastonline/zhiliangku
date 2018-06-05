<template>
  <div class="myform">
    <div class="myform-title font1_30_6">编辑工作经历</div>
    <div class="myform-body">
      <div class="item  the-input">
        <span class="tags">公司名称：</span>
        <el-input v-model="value0"></el-input>
      </div>
      <div class="item  the-input">
        <span class="tags">职位名称：</span>
        <el-input v-model="value1"></el-input>
      </div>
      <div class="item  the-input">
        <span class="tags">入职时间：</span>
        <el-date-picker format="yyyy 年 MM 月 " value-format="yyyy-MM" v-model="value2" type="month" placeholder="选择月">
        </el-date-picker>
      </div>
      <div class="item  the-input">
        <span class="tags">离职时间：</span>
        <el-date-picker format="yyyy 年 MM 月 " value-format="yyyy-MM" v-model="value3" type="month" placeholder="选择月">
        </el-date-picker>
      </div>
      <div class="myform-body">
        <div class="item  the-input">
          <span class="tags">工作内容：</span>
          <el-input v-model="value4" @input="wordnum=value4.length" :maxlength="maxwordnum" type="textarea"></el-input>
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
        wordnum: 0,
        maxwordnum: 1600,
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
           resume_type: 'workexperience',
           pk_id:this.mainData[this.editorIndex].id
        }).then(res=>{
          this.last(res)
        })
      },
      orgnizeData() {
        var data = {
          custom_user_id: localStorage.uid,
          resume_type: 'workexperience',
          resume_info_dict: {
            "company": this.value0,
            "content": this.changebr(this.value4),
            "end_time": this.value3,
            "position": this.value1,
            "start_time": this.value2
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
        this.initForm(this, this.mainData[this.editorIndex], ['company', 'position',
          'start_time', 'end_time', 'content'
        ], [
          'value0', 'value1', 'value2', 'value3', 'value4'
        ])
        this.value4=this.changen(this.value4)
      }
      //  "workexperiences": [{
      //       "company": "智量酷",
      //       "id": 1,
      //       "content": "主要对智量酷网站做开发。",
      //       "custom_user_id": 31,
      //       "end_time": "至今",
      //       "position": "Python开发工程师",
      //       "start_time": "2017-11-2"
      //     }],
    },
    components: {
      rcb: rcb
    }
  }

</script>
<style lang="scss">
  @import "./style/01_resume_form.scss";

</style>
