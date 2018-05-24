<template>
  <div class="mw hc note_container ">
    <div class="ftr"><span class="dib font1_16_6 cp" @click="del_student_note(noteData)">删除</span></div>
    <p></p>
    <div class="ftr"><span class="dib font2_16_9" v-html="noteData.notes"></span></div>
    <div class="ftr note_time"><span class="dib font1_16_9 " >{{noteData.create_time}}</span>
    </div>
  </div>
</template>

<script>
  export default {
    name: "student_notes_li",
    props: {
      noteData: Object
    },
    methods: {
      del_student_note(item) {
        let video_id = this.$fn.funcUrl('video_id')
        let obj = {
          'custom_user_id': localStorage.uid,
          'video_id': video_id,
          'notes_id': item.id
        }
        this.$post('/tracks/student/del/notes/info', obj).then(res => {
          if (!res.err) {
            this.$emit('delete_note')
            this.$fn.showNotice(this, '您已成功删除该笔记', 'success')
          }
        })
      }
    },
    created() {

    }
  }
</script>

<style scoped>
  .note_container {
    padding: 20px 30px 20px 40px;
    box-sizing: border-box;
    margin-bottom: 20px;
    background-color: #fcfcfc;
    min-height: 140px;
  }

  .note_time {
    line-height: 50px;
  }

</style>
