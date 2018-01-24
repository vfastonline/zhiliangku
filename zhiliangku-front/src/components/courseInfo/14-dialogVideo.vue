<template>
  <div class="path-list-dialog-video">
    <el-dialog @open="openPlayer()" @close="closePlayer()"  :visible.sync="centerDialogVisible" width="80%">
      <div v-if="showPlayer" id="e8888b74d1229efec6b4712e17cb6b7a_e">
      </div>
    </el-dialog>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>


</style>
<script>
  import Bus from '../../assets/js/bus'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        centerDialogVisible: false,
        mainData: {},
        zhiliangkuplayer:'',
        showPlayer:false
      }
    },
    props: {
      mainData:Object
    },
    methods: {
      openPlayer(){
        this.showPlayer=true;
      },
      closePlayer(){
        this.showPlayer=false;
        this.zhiliangkuplayer=false;
      },
       video(vid) {
         if(this.zhiliangkuplayer){return}
         var element=document.querySelector('#e8888b74d1229efec6b4712e17cb6b7a_e');
         if(!element){return}
        var obj = {
          wrap: '#e8888b74d1229efec6b4712e17cb6b7a_e',
          width: '100%',
          height: window.innerHeight - 200,
          vid: vid,
        }
        var zhiliangkuplayer = polyvPlayer(obj);
        this.zhiliangkuplayer = zhiliangkuplayer;
      },
    },
    updated(){
      this.video(this.mainData.vid)
    },
    created() {
      Bus.$on('openDialogVideo', (res) => {
        this.centerDialogVisible = true;
      })
      console.log(this.mainData)
    },
    mounted(){
    },
    components: {}

  }

</script>
