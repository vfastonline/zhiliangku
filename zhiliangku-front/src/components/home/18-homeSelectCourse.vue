<template>
 
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->

<script>
import container from '../courseInfo/container.vue'
export default {
  name: 'HelloWorld',
  data () {
    return {
        tagsArr:['前端开发','后端开发','人工智能','云计算&大数据','运维'],
        activeIndex:0,
    }
  },
  props:{

  },
  methods:{

  },
  created(){

  },
  components:{
    container:container
  }
}
</script>


