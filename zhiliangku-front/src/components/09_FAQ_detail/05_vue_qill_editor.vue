<template>
  <div class="rich_text_container">
    <div class="rich_content">
      <img class="user_icon" :src="userIcon" alt="">
      <quill-editor class="rich_textarea" v-model="content" :options="options" ref="myQuillEditor">
      </quill-editor>
    </div>
    <div class="ftr">
      <BlueButton @click="sendAnwser()">发表回答</BlueButton>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .rich_content{
    display: flex;
    justify-content: space-between;
    align-items: start;
  }
  .rich_textarea {
    margin-bottom: 10px;
    width: 750px;
    display: inline-block;
    background-color: white;
  }

  .user_icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    vertical-align: top;
  }

  .rich_text_container {
    background: white;
    box-sizing: border-box;
    border-radius: 10px;
  }

</style>
<script>
  import Vue from 'vue'
  import VueQuillEditor from 'vue-quill-editor'
  import 'quill/dist/quill.core.css'
  import 'quill/dist/quill.snow.css'
  import 'quill/dist/quill.bubble.css'
  import Bus from '../../assets/js/02_bus'
  import BlueButton from '../00_common/04_blue_button'

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
    props: {},
    methods: {
      sendAnwser() {
        this.$post('/community/add/faqanswer', this.organizeData()).then(res => {
          if (!res.data.err) {
            Bus.$emit('replyover');
            this.content = '\0\0';
            this.$fn.showNotice(this, '您已成功提交答案', 'success')
          }
        })
      },
      organizeData() {
        var obj = {};
        obj.faq_id = this.$fn.funcUrl('faq_id');
        if (!localStorage.uid) {
          alert('uid异常')
        }
        obj.custom_user_id = localStorage.uid;
        obj.answer = this.content;
        return obj
      }
    },
    created() {
      this.userIcon = this.$myConst.httpUrl + localStorage.avatar;
    },
    components: {
      BlueButton:BlueButton
    }
  }

</script>
