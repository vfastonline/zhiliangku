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
  project_detail: {
    path: '02_project_detail',
    filename: 'tracks/projects/detail/index.html'
  },
  course_detail:{
    path:'03_course_detail',
    filename:'tracks/course/detail/index.html'
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
    console.log(1111)
    pageConf.dist.minify = {
      removeComments: true,
      collapseWhitespace: true,
      removeAttributeQuotes: true
    }
    pageConf.dist.chunksSortMode='dependency'
  }
  distArr.push(pageConf.dist)
})
// console.log(entryObj)
// console.log(...distArr)

module.exports = {
  Entry: entryObj,
  Dist: distArr
}