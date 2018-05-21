<template>
  <section class="mw hc">
    <div>
    <NoteLi></NoteLi>
    </div>
    <Pager></Pager>
  </section>
</template>

<script>
  import NoteLi from './10_student_notes_li'
  import Pager from '../00_common/06_pager'
  export default {
    name: "student_notes",
    methods:{
      get_data(){

      }
    },
    components: {
      NoteLi: NoteLi,
      Pager:Pager
    },
    created(){
      this.get_data()
    }
  }
</script>

<style scoped>

</style>
