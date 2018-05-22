<template>
  <div class="rich_text_container">
    <div class="marginbottom8">我来回答</div>
    <div class="rich1">
      <img class="user_icon" :src="userIcon" alt="">
      <quill-editor class="rich_textarea" v-model="content" :options="options" ref="myQuillEditor">
      </quill-editor>
      <el-button @click="sendAnwser()">发表回答</el-button>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .rich_textarea {
    margin-bottom: 10px;
    width: 664px;
    display: inline-block;
  }

  .user_icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    vertical-align: top;
  }

  .rich1 {
    text-align: right;
  }

  .rich_text_container {
    background: white;
    padding: 32px;
    box-sizing: border-box;
  }

</style>
<script>
  import Vue from 'vue'
  import VueQuillEditor from 'vue-quill-editor'
  import 'quill/dist/quill.core.css'
  import 'quill/dist/quill.snow.css'
  import 'quill/dist/quill.bubble.css'
  import Bus from '../../assets/js/02_bus'
  Vue.use(VueQuillEditor)
  export default {
    name: 'HelloWorld',
    data() {
      return {
        content: '&nbsp;',
        userIcon: "",
        options: {
          modules: {
            toolbar: ['bold', 'italic', 'underline',
              // 'image',
              'link', {
                'list': 'bullet'
              }, {
                'list': 'ordered'
              }, 'blockquote'
            ]
          }
        }
      }
    },
    props: {

    },
    methods: {
      sendAnwser() {
        this.$post('/community/add/faqanswer',this.organizeData() ).then(res => {
          if(!res.data.err){
            Bus.$emit('replyover');
            this.content='\0\0';
            this.$fn.showNotice(this,'您已成功提交答案','success')
          }
        })
      },
      organizeData() {
        var obj = {};
        obj.faq_id = this.$fn.funcUrl('id');
        if(!localStorage.uid){alert('uid异常')}
        obj.custom_user_id = localStorage.uid;
        obj.answer = this.content;
        return obj
      }
    },
    created() {
      this.userIcon = this.$myConst.httpUrl + localStorage.avatar;
    },
    components: {

    }
  }

</script>
