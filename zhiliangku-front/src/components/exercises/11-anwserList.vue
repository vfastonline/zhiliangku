<template>
  <div class="aq-width incenter anwser-list">
      <anwser></anwser>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.anwser-list{
    background: white;
}
</style>
<script>
import anwser from './10-anwser'
export default {
  name: 'HelloWorld',
  data () {
    return {
    }
  },
  props:{

  },
  methods:{

  },
  created(){

  },
  components:{
    anwser:anwser
  }
}
</script>


