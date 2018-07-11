//js、html默认路径的前半段
const prePath = './src/pages/'
//js文件默认路径的后半段
const jsPath = '/main.js'
//html默认路径的后半段
const htmlPath = '/index.html'
//入口注意：path是对应的路径中段。filename:对应的是生成文件的路径，对应的是服务器上后端给出的路由。
const entry = {
  index: {
    path: '00_index',
    filename: 'index.html'
  },
  project_list: {
    path: '01_project_list',
    filename: 'tracks/projects/list/index.html'
  },
  project_detail: {
    path: '02_project_detail',
    filename: 'tracks/projects/detail/index.html'
  },
  course_detail: {
    path: '03_course_detail',
    filename: 'tracks/course/detail/index.html'
  },
  video_detail: {
    path: '04_video_detail',
    filename: 'tracks/video/detail/index.html'
  },
  community: {
    path: '05_community',
    filename: 'community/faq/list/index.html'
  },
  faq_detail: {
    path: '06_FAQ_detail',
    filename: 'community/faq/detail/index.html'
  },
  assess_result: {
    path: '22_assess_result',
    filename: 'assess/result/index.html'
  },
  exercise: {
    path: '08_exercise',
    filename: 'exercise/list/index.html',
  },
  personal_center: {
    path: '09_personal_center',
    filename: 'personal_center/page/index.html'
  },
  leader_board: {
    path: '10_leader_board',
    filename: 'employment/leaderboard/list/index.html'
  },
  finish_project_list: {
    path: '11_finish_project_list',
    filename: 'employment/finishprojectlistinfo/list/index.html'
  },
  error_404: {
    path: '23_404',
    filename: '404.html'
  },
  we_jl: {
    path: '24_jl',
    filename: 'wechat/promotion/jl/index.html'
  },
  we_chat: {
    path: '25_we_chat',
    filename: 'wechat/promotion/index.html'
  },
  we_chat_world_cup: {
    path: '26_we_chat_world_cup',
    filename: 'worldcup/topic/index.html'
  },
  notification: {
    path: '12_notification',
    filename: 'notification/index.html'
  },
  login: {
    path: '20_login',
    filename: 'login/index.html'
  },
  test: {
    path: '21_test',
    filename: 'assess/info/index.html'
  },
  test_page: {
    path: '30_test',
    filename: 'test/index.html'
  },
  back_stage: {
    path: 'b01_back_stage',
    filename: 'backstage/index/index.html'
  }
}
//下面的函数主要是处理了上面的entry的数据结构使得其能输出合理的数据结构，entryObj和distArr分别对应了开发和生产模式所需要的数据
let entryObj = {}
let distArr = []
Object
  .keys(entry)
  .forEach(el => {
    let pageConf = entry[el]
    let thisPath = pageConf.path
    pageConf.path = prePath + thisPath + jsPath
    pageConf.dist = {
      filename: pageConf.filename,
      template: prePath + thisPath + htmlPath,
      chunks: [
        'manifest', 'vendor', el + ''
      ],
      inject: true
    }
    entryObj[el] = pageConf.path
    if (process.env.NODE_ENV === 'production') {
      pageConf.dist.minify = {
        removeComments: true,
        collapseWhitespace: true,
        removeAttributeQuotes: true
      }
      pageConf.dist.chunksSortMode = 'dependency'
    }
    distArr.push(pageConf.dist)
  })
// console.log(entryObj) console.log(...distArr)
module.exports = {
  Entry: entryObj,
  Dist: distArr
}
