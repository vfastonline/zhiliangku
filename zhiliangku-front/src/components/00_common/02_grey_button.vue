<template>
  <el-button @click.native="handle_click" :style="S" ><slot></slot></el-button>
</template>

<script>
  import Vue from 'vue'
  import {Button} from 'element-ui'

  Vue.use(Button)
  export default {
    name: "grey_button",
    methods:{
      handle_click(e){
        this.$emit('click',e)
      }
    },
    props:{
      S:{}
    }
  }
</script>

<style scoped>
  .el-button {
    display: inline-block;
    line-height: 1;
    white-space: nowrap;
    cursor: pointer;
    background: #a3abb6;
    border: 1px solid #a3abb6;
    color: #ffffff;
    -webkit-appearance: none;
    text-align: center;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    outline: 0;
    margin: 0;
    -webkit-transition: .1s;
    transition: .1s;
    font-weight: 300;
    -moz-user-select: none;
    -webkit-user-select: none;
    -ms-user-select: none;
    padding: 12px 48px;
    font-size: 26px;
    border-radius: 10px
  }

  .el-button + .el-button {
    margin-left: 0px
  }

  .el-button:focus, .el-button:hover {
    color: #ffffff;
    border-color: #a3abb6;
    background-color: #a3abb6
  }

  .el-button:active {
    color: #ffffff;
    border-color: #a3abb6;
    outline: 0
  }

  .el-button::-moz-focus-inner {
    border: 0
  }
</style>
