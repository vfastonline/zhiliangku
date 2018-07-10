<template>
  <div>
    <div class="container_a">
      <el-select class="select_addition" v-model="value0" @change="get_data('course_data',value0)" placeholder="请选择项目">
        <el-option
          v-for="item in item_data"
          :key="item.id"
          :label="item.name"
          :value="item.id">
        </el-option>
      </el-select>
      <el-select class="select_addition" v-model="value1" :disabled="!value0" @change="get_data('section_data',value1)"
                 placeholder="请选择课程">
        <el-option
          v-for="item in course_data"
          :key="item.id"
          :label="item.name"
          :value="item.id">
        </el-option>
      </el-select>
      <el-select class="select_addition" v-model="value2" :disabled="!value1" @change="get_data('video_data',value2)"
                 placeholder="请选择章节">
        <el-option
          v-for="item in section_data"
          :key="item.id"
          :label="item.name"
          :value="item.id">
        </el-option>
      </el-select>
      <el-select class="select_addition" v-model="value3" :disabled="!value2" @change="get_right_name('video_data',value3,4)" placeholder="请选择节点">
        <el-option
          v-for="item in video_data"
          :key="item.id"
          :label="item.name"
          :value="item.id">
        </el-option>
      </el-select>
    </div>
    <div class="selected_progress font1_18_6">
      <span>已选择:</span>
      <span v-for="item in str_arr" :key="item" v-if="item">
        <span v-if="index!==0">&nbsp;-&nbsp;</span>
        <span>{{item}}</span>
      </span>
    </div>
    <div class="bottom_button_container">
      <div>
        <div class="yesterday_progress">
          <span class="font1_22_6 dib">昨日进度</span>
          <span class="font1_18_9 dib time_span">{{(new Date()-24*3600*1000) | moment('YYYY-MM-DD')}}(昨日)</span>
        </div>
        <p class="font1_18_6">{{yesterday_progress.yesterday_task_name||'暂无昨日信息'}}</p>
      </div>
      <Blue_button class="submit_button" @click="pre_submit"><span class="font1_26_f">提交</span></Blue_button>
    </div>
    <confirm v-if="show_confirm" @close="show_confirm=false" @confirm="submit"></confirm>
  </div>
</template>

<script>

  import Vue from 'vue'
  import {Select, Option} from 'element-ui'
  import Blue_button from '../00_common/04_blue_button'
  import confirm from './05_double_confirm'
  import Bus from '../../assets/js/02_bus'

  Vue.use(Select)
  Vue.use(Option)
  export default {
    name: "selected",
    data() {
      return {
        arr: ['item_data', 'course_data', 'section_data', 'video_data'],
        str_arr: [],
        item_data: [],
        course_data: [],
        section_data: [],
        video_data: [],
        value0: '',
        value1: '',
        value2: '',
        value3: '',
        yesterday_progress: {},
        show_confirm: false
      }
    },
    methods: {
      selected(index) {
        if (this['value' + index]) {
          return true
        }
      },
      pre_submit() {
        let verify = this.arr.every((el, index) => {
          if (this['value' + index]) return true
        })
        if (!verify) {
          this.$notify({
            type: 'error',
            message: '请选择今日任务',
            offset: 100,
            duration: 3000,
            position: 'bottom-right'
          })
          return
        }
        this.show_confirm = true
      },
      submit() {
        this.$post('/backstage/set/task/info', {video_id: this.value3}).then(res => {
          if (!res.err) {
            this.$notify({
              type: 'success',
              message: '已设置成功',
              offset: 100,
              duration: 3000,
              position: 'bottom-right'
            })
            Bus.$emit('submit_task_success')
          }
          this.show_confirm = false
        })
      },
      get_data(key, value) {
        if (!value) return
        let index = this.arr.indexOf(key) + 1
        this.change_child_data(key, value)
        this.$get('/backstage/set/task/info?info=' + index + '&pk_id=' + value).then(res => {
          this.handle_data(res.data.data)
          this[key] = res.data.data
          this['value' + index] = ''
        })
      },
      handle_data(data) {
        data.forEach(el => {
          if (el.title) {
            el.name = el.title
          }
        })

      },
      change_child_data(key, value) {
        let arr = this.arr
        let index_selected = arr.indexOf(key)
        //此处主要是做了数据清空
        arr.forEach((el, index) => {
          //如果是上级的那么不往下执行
          if (index < index_selected) return
          //index靠后的执行如下代码
          this[el] = ''
          this['value' + index] = ''
        })
        let pre_key = arr[index_selected - 1]
        this.get_right_name(pre_key,value,index_selected)
      },
      get_right_name(key,value,index) {
        this[key].forEach((el) => {
          if (el.id * 1 === value * 1) {
            this.str_arr.splice(index-1)
            this.str_arr.push(el.name)
          }
        })
      },
      get_init_data() {
        this.$get('/backstage/set/task/info?info=1').then(res => {
          this.item_data = res.data.data
        })
      },
      get_yesterday_progress() {
        this.$get('/backstage/get/yesterday/task/schedule').then(res => {
          this.yesterday_progress = res.data.data
        })
      }
    },
    created() {
      this.get_init_data()
      this.get_yesterday_progress()
    },
    components: {
      Blue_button: Blue_button,
      confirm: confirm
    }
  }
</script>

<style scoped>
  .yesterday_progress {
    margin-bottom: 10px;
  }

  .selected_progress {
    margin-bottom: 50px;
  }

  .time_span {
    margin-left: 20px;
    font-weight: 600;
  }

  .container_a {
    width: 320px;
  }

  .select_addition {
    width: 100%;
    margin-bottom: 20px;
  }

  .submit_button {
    width: 200px;
    height: 58px;
    flex: 0 0 auto;
  }

  .bottom_button_container {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
</style>
