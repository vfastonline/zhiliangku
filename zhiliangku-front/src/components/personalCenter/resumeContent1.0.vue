<template>
  <div class="myform">
    <div class="myform-title font20pl3a3c50">编辑我的优势</div>
    <div class="myform-body">
      <div class="item  the-input">
        <span class="tags">优势描述</span>
        <el-input v-model="value0" @input="word('value0')" :maxlength="maxwordnum" type="textarea"></el-input>
        <div class="word-indecator font14pl5A646E">{{wordnum}}/{{maxwordnum}}</div>
      </div>
    </div>
    <rcb @cancel="close" @submit="submit" :layer="['submit','cancel']"></rcb>
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
        wordnum: 0,
        maxwordnum: 300,
        url: '/personal_center/resume/update'
      }
    },
    props: {
      mainData: Object
    },
    methods: {
      word(key) {
        this.wordnum = (this[key] + '').length;
        console.log(this[key])
      },
      close() {
        this.$emit('close')
      },
      submit() {
        if(JSON.stringify(this.mianData)=='{}'){
          this.url='/personal_center/resume/add'
        }
        this.$post(this.url, {
          resume_type: 'resume',
          pk_id:this.mainData.id,
          resume_info_dict: {
            advantage: this.value0
          },
          custom_user_id: localStorage.uid
        }).then(res => {
          if(!res.data.err){
            Bus.$emit('refreshResume',res.data.data)
          }
          this.close();
          console.log(res)
        })
      }
    },
    created(){
       this.initForm(this, this.mainData, ['advantage' ], [
        'value0'
      ])
    },
    components: {
      rcb: rcb
    }
  }

</script>
<style lang="scss">
  @import "../../style/scss/components/resumeForm.scss";

</style>
