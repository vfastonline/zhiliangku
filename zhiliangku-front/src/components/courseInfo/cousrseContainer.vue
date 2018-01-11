<template>
  <div class="" :style="mainData.containerStyle">
      <hot-course :mainData="mainData"></hot-course>
  </div>
</template>
<script>
export default {
  data(){
      return {
          
      }
  },
  props:{
      mainData:Object
  }
}
</script>

