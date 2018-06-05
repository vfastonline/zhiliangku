<template>
  <div>
    <unit v-for="(item,index) in main_data" :key="index" :main_data="item[item.timeKey]"></unit>
  </div>
</template>

<script>
  import unit from './09_learning_progress_unit'

  export default {
    name: "learning_progress",
    data() {
      return {
        main_data: '',
      }
    },
    created(){
      this.$get("/personal_center/learning/progress").then(res=> {
        console.log( res.data.data)
        if(!res.err){
          res.data.data.forEach( el=>{
            //组装 时间 这个key
            var arr = Object.keys(el)
            el.timeKey=arr[0]
          })
          this.main_data = res.data.data

        }
      })
    },
    components: {
      unit: unit
    }
  }
</script>

<style scoped>

</style>
