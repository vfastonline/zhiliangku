<template>
  <section class="mw hc student_note r">
    <NoteEditor v-if="editor_switch" @close="editor_switch=false" @up_data="init_params" class="editor a"></NoteEditor>
    <div class="student_note_content">
      <NoteLi v-for="(item,index) in student_note_datas" :key="item.id"
              @delete_note="delete_note(index)"
              :noteData="item"></NoteLi>
    </div>
    <Pager @pagerGetData="mainPagerData" :url="url" :additionData="params"></Pager>
  </section>
</template>

<script>
  import Vue from 'vue'
  import VueQuillEditor from 'vue-quill-editor'
  import NoteLi from './10_student_notes_unit'
  import Pager from '../00_common/06_pager'
  import Bus from '../../assets/js/02_bus'
  import 'quill/dist/quill.core.css'
  import 'quill/dist/quill.snow.css'
  import 'quill/dist/quill.bubble.css'
  import NoteEditor from './12_note_editor'

  Vue.use(VueQuillEditor)
  export default {
    name: "student_notes",
    data() {
      return {
        main_data: '',
        student_note_datas: '',
        url: '/tracks/student/notes/list/info',
        params: '',
        editor_switch: false
      }
    },
    methods: {
      delete_note(index) {
        this.student_note_datas.splice(index, 1)
        this.init_params()
      },
      mainPagerData(res) {
        this.student_note_datas = res.data.data
      },
      show_editor() {
        this.editor_switch = true
      },
      init_params() {
        this.params = {
          'custom_user_id': localStorage.uid,
          'video_id': this.$fn.funcUrl('video_id')
        }
      }
    }
    ,
    created() {
      Bus.$on('write_note', this.show_editor)
      this.init_params()
    }
    ,
    components: {
      NoteLi: NoteLi,
      Pager: Pager,
      NoteEditor: NoteEditor
    }
  }
</script>
<style>
  .editor {
    left: 50%;
    top: 58px;
    transform: translate(-50%);
  }
</style>
<style scoped>
  .student_note {
    min-height: 70vh;
    margin-bottom: 30px;
  }

  .student_note_content {
    min-height: 64vh;
  }
</style>
