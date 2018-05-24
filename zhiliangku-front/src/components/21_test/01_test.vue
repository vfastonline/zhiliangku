<template>
  <div class="mw hc">
    <el-dialog title="成绩" :visible.sync="dialogVisible" width="30%">
      <span>本次得分为：{{mark.mark}}</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
    </el-dialog>

    <div class="test_container incenter">
      <div>
        <ul class="list">
          <li>1：创建一个文件名为aaa.txt的文件，并存放在tmp目录下</li>
          <li>2：将mp下所有文件打包为tmp.zip压缩包</li>
        </ul>
      </div>
      <div>
        <iframe :src="src" onload="" frameborder="0" width="1088px" height="400" scrolling='no'
                hspace="0"
                vspace="0"></iframe>
      </div>
      <div class="submit_container">
        <el-button type="primary" @click="submit()" size="medium">提交答案</el-button>
      </div>
    </div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang='scss'>
  .submit_container {
    text-align: right;
  }

  .test_container {
    margin-top: 32px;
    border: 2px solid #999;
    border-radius: 10px;
    padding: 24px
  }

  .list {
    li {
      height: 48px;
      font-size: 32px;
    }
    margin-bottom: 32px;
  }

</style>
<script>
  import Vue from 'vue'
  import {Button} from 'element-ui'

  Vue.use(Button)
  export default {
    name: 'HelloWorld',
    data() {
      return {
        mark: {mark: ''},
        dialogVisible: false,
        src:''
      }
    },
    props: {},
    methods: {
      jj() {
        console.log(111)
      },
      submit() {
        this.$post('/assess/result', {video_id:177}).then(res => {
          console.log(res);
          this.mark.mark = res.data.grade;
          this.dialogVisible = true;
        })
      }
    },
    created() {
      this.$get('/assess/construct?video_id=177').then(res=>{
        this.src='http://118.190.209.153:'+res.data.data.port+'/'
      })
    },
    mounted(){

    },
    components: {}
  }

</script>
