<template>
  <div class="myform">
    <div class="myform-title font1_30_6">编辑求职意向</div>
    <div class="myform-body">
      <div class="item  the-input">
        <span class="tags">期望职位：</span>
        <el-input v-model="value0"></el-input>
      </div>
      <div class="item  the-input">
        <span class="tags">工作方式：</span>
        <el-input v-model="value1"></el-input>
      </div>
      <div class="item  the-input">
        <span class="tags">城市：</span>
        <el-input v-model="value2"></el-input>
      </div>
      <div class="item  the-input">
        <span class="tags">薪资：</span>
        <el-select v-model="value3">
          <el-option v-for="(item,index) in salaryoption" :key="index" :value="item" :label="item"></el-option>
        </el-select>
      </div>
      <div class="item  the-input">
        <span class="tags">行业：</span>
        <el-select v-model="value4">
          <el-option v-for="(item,index) in professionoption" :key="index" :value="item" :label="item"></el-option>
        </el-select>
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
        salaryoption: ['2k以下', '2k-5k', '5k-10k', '10k-15k', '15k-25k', '25k-50k', '50k以上'],
        professionoption: ["健康医疗", "生活服务", "旅游", "金金融", "信息安全", "广告营销", "数据服务", "智能硬件", "文化娱乐", "网络招聘", "分类信息", "电子商务",
          "移动互联网", "企业服务", "社交网络", "教育培训", "O2O", "游戏", "互联网", "媒体", "IT软件", "通信", "公关会展", "房地产/建筑", "汽车", "供应链/物流",
          "咨询/翻译/法律律", "采购/贸易易", "非互联网行行业"
        ],
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
           resume_type: 'careerobjective',
           pk_id:this.mainData[this.editorIndex].id
        }).then(res=>{
          this.last(res)
        })
      },
      submit() {
        var obj=this.mainData[this.editorIndex];
        var data={
          custom_user_id: localStorage.uid,
          resume_type: 'careerobjective',
          resume_info_dict: {
            position: this.value0,
            expect_salary: this.value3,
            city: this.value2,
            industry: this.value4,
            way:this.value1
          }
        };
        if(obj){data.pk_id=obj.id}
        this.$post(this.url,data ).then(res => {
          console.log(res)
         this.last(res)
        })
      },
    },
    created() {
      console.log(this.editorIndex)
      if (this.editorIndex != -1) {
        this.initForm(this, this.mainData[this.editorIndex], ['position', 'expect_salary', 'city', 'industy','way'], [
          'value0', 'value3', 'value2', 'value4','value1'
        ])
      }

      // "careerobjectives": [{
      //       "city": "深圳",
      //       "expect_salary_low": 1,
      //       "expect_salary_high": 2,
      //       "industry": "教育",
      //       "custom_user_id": 31,
      //       "position": "前端开发",
      //       "id": 1
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
