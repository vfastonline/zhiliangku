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
        <el-date-picker format="yyyy 年 MM 月 " value-format="yyyy-MM" v-model="value3" type="month" placeholder="选择月">
        </el-date-picker>
      </div>
      <div class="item  the-input">
        <span class="tags">结束时间：</span>
        <el-date-picker format="yyyy 年 MM 月 " value-format="yyyy-MM" v-model="value4" type="month" placeholder="选择月">
        </el-date-picker>
      </div>
      <div class="item  the-input">
        <span class="tags">项目描述：</span>
        <el-input v-model="value5" @input="wordnum0=value5.length" :maxlength="maxwordnum0" type="textarea"></el-input>
        <div class="word-indecator font14pl5A646E">{{wordnum0}}/{{maxwordnum0}}</div>
      </div>
      <div class="item  the-input">
        <span class="tags">项目业绩：</span>
        <el-input v-model="value6" @input="wordnum1=value6.length" :maxlength="maxwordnum1"  type="textarea"></el-input>
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
        value5: '',
        value6:'',
        wordnum0: 0,
        maxwordnum0: 300,
        wordnum1: 0,
        maxwordnum1: 300,
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
           resume_type: 'projectexperience',
           pk_id:this.mainData[this.editorIndex].id
        }).then(res=>{
          this.last(res)
        })
      },
      orgnizeData() {
        var data = {
          custom_user_id: localStorage.uid,
          resume_type: 'projectexperience',
          resume_info_dict: {
            "name": this.value0,
            "role": this.value1,
            "url": this.value2,
            "start_time": this.value3,
            "end_time": this.value4,
            "description": this.changebr(this.value5),
            'performance': this.changebr(this.value6)
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
        this.initForm(this, this.mainData[this.editorIndex], ['name', 'role','url',
          'start_time', 'end_time', 'description','performance'
        ], [
          'value0', 'value1', 'value2', 'value3', 'value4','value5','value6'
        ])
      }
      ['value5','value6'].forEach(el=>{
        this[el]=this.changen(el)
      })
    },
    components: {
      rcb: rcb
    }
  }

</script>
<style lang="scss">
  @import "./style/01_resume_form.scss";
</style>
