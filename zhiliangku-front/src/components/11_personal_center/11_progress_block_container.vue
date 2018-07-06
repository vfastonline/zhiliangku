<template>
  <div class="border_style_block r">
    <div class="float_tag a">
      <span class="font1_20_3 dib vm">
        <span v-if="main_data.year_tag" class="font1_24_6">
          {{main_data.year}}<br>
        </span>
        <span>{{main_data.month_day}}</span>
      </span>
      <span class="tag_dot dib vm"></span>
    </div>
    <slot></slot>
  </div>
</template>

<script>
  export default {
    name: "progress_block_container",
    data() {
      return {
        str: ''
      }
    },
    props: {
      main_data: {
        required: true,
        default: {time: '今天'}
      }
    },
    watch: {
      main_data(n, old) {
        console.log(n + '' + old)
      }
    }
  }
</script>

<style scoped>
  .border_style_block {
    border-left: 2px solid #999;
    padding-left: 76px;
    margin-left: 32px;
  }

  .float_tag {
    right: 100%;
    top: 0;
    transform: translate(8px, -50%);
    z-index: 1;
    white-space: nowrap;
    display: flex;
    justify-content: right;
    align-items: center;
  }

  .tag_dot {
    margin-left: 14px;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    z-index: 10;
    border: 2px solid #999;
    background-color: white;
  }
</style>
