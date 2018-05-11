<template>
  <footer class="footer">
    <p class="ftc">
      <span v-for="(item,index ) in tags" :key="index">
       <a class="font1_16_f" :href="item.link">{{item.text}}</a>
       <span v-if="index!==(tags.length-1)" class="footer_pointer "></span>
      </span>
    </p>
    <p class="ftc font1_16_f copy_right">
      copyright 2017 北京智量酷教育科技有限公司 京ICP备09076312号
    </p>
  </footer>
</template>

<script>
  export default {
    name: "f",
    data() {
      return {
        tags: [
          {text: '关于我们', link: '#'},
          {text: '加入我们', link: '#'},
          {text: '联系我们', link: '#'},
          {text: '讲师合作', link: '#'},
          {text: '帮助中心', link: '#'},
          {text: '友情链接', link: '#'},
          {text: '合作企业', link: '#'},
        ]
      }
    }
  }
</script>

<style scoped>
  .footer {
    width: 100%;
    height: 84px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding-top: 96px;
    padding-bottom: 60px;
    background: url("./img/footer_background.png") center center;
  }

  .footer_pointer {
    display: inline-block;
    background-color: #ffffff;
    height: 8px;
    width: 8px;
    margin: 0 12px;
    vertical-align: baseline;
    -webkit-border-radius: 10px;
    -moz-border-radius: 10px;
    border-radius: 10px;
  }
  .copy_right{
    opacity: .31;
  }
</style>
