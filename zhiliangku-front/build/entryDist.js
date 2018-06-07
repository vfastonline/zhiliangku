const prePath = './src/pages/'
const jsPath = '/main.js'
const htmlPath = '/index.html'
const entry = {
  index: {
    path: '00_index',
    filename: 'index.html'
  },
  project_list: {
    path: '01_project_list',
    filename: 'tracks/projects/list/index.html'
  },
  video_detail:{
    path:'04_video_detail',
    filename:'tracks/video/detail/index.html'
  },
  community:{
    path:'05_community',
    filename:'community/faq/list/index.html'
  },
  faq_detail:{
    path:'06_FAQ_detail',
    filename:'community/faq/detail/index.html'
  },
  login:{
    path:'20_login',
    filename:'login/index.html'
  },
  test:{
    path:'21_test',
    filename:'assess/info/index.html'
  },
  assess_result:{
    path:'22_assess_result',
    filename:'assess/result/index.html'
  },
  exercise:{
    path:'08_exercise',
    filename: 'exercise/list/index.html',
  },
  personal_center:{
    path:'09_personal_center',
    filename:'personal_center/page/index.html'
  },
  leader_board:{
    path:'10_leader_board',
    filename:'employment/leaderboard/list/index.html'
  },
  finish_project_list:{
    path:'11_finish_project_list',
    filename:'employment/finishprojectlistinfo/list/index.html'
  },
  error_404:{
    path:'23_404',
    filename:'404.html'
  },
  we_chat:{
    path:'24_we_chat',
    filename:'wechat/promotion/index.html'
  }
}
var entryObj = {}
var distArr = []
Object.keys(entry).forEach(el => {
  var pageConf = entry[el]
  var thisPath = pageConf.path
  pageConf.path = prePath + thisPath + jsPath
  pageConf.dist = {
    filename: pageConf.filename,
    template: prePath + thisPath + htmlPath,
    chunks: ['manifest', 'vendor', el + ''],
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
// console.log(entryObj)
// console.log(...distArr)

module.exports = {
  Entry: entryObj,
  Dist: distArr
}
