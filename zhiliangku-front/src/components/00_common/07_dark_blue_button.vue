<template>
  <el-button><slot></slot></el-button>
</template>

<script>
  import Vue from 'vue'
  import {Button} from 'element-ui'

  Vue.use(Button)
  export default {
    name: "blue_button",
  }
</script>

<style scoped>
  .el-button {
    display: inline-block;
    line-height: 1;
    white-space: nowrap;
    cursor: pointer;
    background: #647a90;
    border: 1px solid #647a90;
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
    padding: 3px 18px;
    font-size: 19px;
    border-radius: 10px
  }

  .el-button + .el-button {
    margin-left: 10px
  }

  .el-button:focus, .el-button:hover {
    color: #ffffff;
    border-color: #647a90;
    background-color: #647a90
  }

  .el-button:active {
    color: #ffffff;
    border-color: #647a90;
    outline: 0
  }

  .el-button::-moz-focus-inner {
    border: 0
  }
</style>
