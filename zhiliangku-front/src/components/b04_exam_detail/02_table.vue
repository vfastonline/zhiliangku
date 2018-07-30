<template>
  <div class="mw hc examDetail__table--main">
    <detail_dialog></detail_dialog>
    <table class="my_table">
      <tr class="font1_22_3 date_title weight">
        <th class="column_01">日期</th>
        <th>07-12</th>
        <th>07-12</th>
        <th>07-12</th>
        <th>07-12</th>
        <th>07-12</th>
      </tr>
      <tr class="font1_22_3 tr_1">
        <th class="font1_22_3 weight column_01">姓名/考试性质</th>
        <td class="font1_22_3">日考</td>
        <td>日考</td>
        <td>日考</td>
        <td>日考</td>
        <td>日考</td>
      </tr>
      <tr>
        <td @click="j" class="cp font1_22_3 column_01">张三</td>
        <td class="font1_18_6">50</td>
        <td class="font1_18_6">50</td>
        <td class="font1_18_6">50</td>
        <td class="font1_18_6">50</td>
        <td class="font1_18_6">50</td>
      </tr>
    </table>
  </div>
</template>

<script>
  import detail_dialog from './03_detail_dialog'
  export default {
    name: "table",
    data() {
      return {
        tableData: [{
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1517 弄'
        }, {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1519 弄'
        }, {
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1516 弄'
        }]

      }
    },
    methods: {
      j() {
        console.log(arguments)
      }
    },
    components:{
      detail_dialog:detail_dialog
    }
  }
</script>

<style lang="scss">
  @import "../../assets/style/baseConstScss";

  .examDetail__table--main {
    margin-bottom: 70px;
    overflow: auto;
    .column_01{
      white-space: nowrap;
    }
    .date_title {
      background-color: $cy;
    }
    .tr_1 {
      background-color: #fef5de;
    }
    th, td {
      border: 1px solid #666;
      min-width: 105px;
      text-align: center;
      padding: 0 5px;
    }
    table {
      border: 2px solid #333;
    }
    .my_table {
      border-collapse: collapse;
    }
  }

</style>
