<template>
  <div>
    <unit></unit>
  </div>
</template>

<script>
  import unit from './09_learning_progress_unit'

  export default {
    name: "learning_progress",
    created(){
      console.log(this)
    },
    components: {
      unit: unit
    }
  }
</script>

<style scoped>

</style>
