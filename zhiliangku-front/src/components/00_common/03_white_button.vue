<template>
  <el-button >
    <slot></slot>
  </el-button>
</template>

<script>
  import Vue from 'vue'
  import {Button} from 'element-ui'

  Vue.use(Button)
  export default {
    name: "grey_button",
    props: {s: {}}
  }
</script>

<style scoped>
  .el-button {
    display: inline-block;
    line-height: 1;
    white-space: nowrap;
    cursor: pointer;
    background: #ffffff;
    border: 1px solid #ffffff;
    color: #00bdd4;
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
    color: #00bdd4;
    border-color: #ffffff;
    background-color: #ffffff
  }

  .el-button:active {
    color: #00bdd4;
    border-color: #ffffff;
    outline: 0
  }

  .el-button::-moz-focus-inner {
    border: 0
  }
</style>
