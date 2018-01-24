<template>
  <div class="mainwidth incenter pathInfo">
    <path-info-left :mainData="allData"></path-info-left>
    <path-info-right :mainData="allData"></path-info-right>
  </div>
</template>
<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        allData: {}
      }
    },
    methods: {
      getData() {
        this.$get(this.orgnizeUrl()).then(res => {
          this.$fn.addObjString(this.$myConst.httpUrl, res.data.data, ['path_img'])
          this.allData = res.data.data;
          console.log(res)
        })
      },
      orgnizeUrl() {
        var str = '/tracks/path/detail/info?path_id=' + this.$fn.getSearchKey('path_id');
        if (localStorage.uid) {
          str += "&custom_user_id=" + localStorage.uid;
        }
        return str
      }
    },
    created() {
      this.getData()
    }
  }

</script>
<style scoped>
  .pathInfo {
    padding-top: 60px;
  }

</style>
