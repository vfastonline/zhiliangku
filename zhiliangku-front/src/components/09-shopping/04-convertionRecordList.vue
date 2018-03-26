<template>
  <div class="container  incenter record_list">
    <convertionRecord v-for="(item,index) in mainData" :key="index"  :mainData="item"></convertionRecord>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .container {
    margin-top: 40px;
    min-height: 400px;
    background: #fafafa;
  }
</style>
<script>
  import convertionRecord from './05-convertionRecord'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        mainData: []
      }
    },
    props: {

    },
    methods: {
      getData() {
        this.$get('/integral/exchange/records?custom_user_id=' + localStorage.uid).
        then(res => {
          this.$fn.addString(this.$myConst.httpUrl, res.data.data, ['images'])
          this.mainData = res.data.data;
          console.log(res.data)
        })
      }
    },
    created() {
      this.getData()
      console.log(this)
    },
    components: {
      convertionRecord: convertionRecord
    }
  }

</script>
