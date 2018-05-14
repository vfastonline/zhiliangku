<template>
  <div class="course_section_container">
    <div class="course_section ftj">
      <span class="fl"><img class="vm first_icon " src="./img/player.png" alt=""></span>
      <span class="dib ftj section_name fr">
          <span class="dib font1_24_3 lesson_name fl">第一章：test1</span>
          <span class="dib font1_18_9 lesson_info fr">
            <span class="dib timer">时长：356分钟</span>
            <span class="dib progress">完成：100%</span></span>
      </span>
    </div>
    <ul>
      <li class="section_li">
        <span class="fl"><img class="vm first_icon " src="./img/player.png" alt=""></span>
        <span class="dib ftj lesson_child fr">
          <span class="dib font1_18_6 lesson_name fl">第一章：test1</span>
          <span class="dib font1_18_9 lesson_info fr">
            <span class="dib timer">时长：356分钟</span>
            <span class="dib progress">完成：100%</span>
          </span>
      </span>
      </li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: "course_section"
  }
</script>

<style scoped>
  .course_section_container {
    margin-left: 110px;
    width: 990px;
  }

  .first_icon {

  }

  .course_section {
    width: 990px;
    margin-bottom: 20px;
    height: 40px;
    line-height: 40px;
  }

  .section_name {
    /*margin-bottom: 20px;*/
    height: 100%;
    width: 950px;
  }

  .lesson_info {
    margin-right: 53px;
  }

  .lesson_name {
    margin-left: 10px;
  }

  .lesson_child {
    width: 890px;
  }

  .section_li {
    width: 940px;
    margin-left: 50px;
    line-height: 30px;
    height: 30px;
    cursor: pointer;
  }

  .section_li:hover .lesson_child {
    background-color: #eeeeee;
  }

  .first_icon {

  }

  .timer {
    margin-right: 20px;
  }
</style>
