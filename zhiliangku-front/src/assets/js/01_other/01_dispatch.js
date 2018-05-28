module.exports = (function () {
  var func = {};
  func.goCourse = function (type, courseId, videoId) {
    switch (type * 1) {
      case 1:
       window.open('/tracks/video/detail/?course_id=' + courseId + '&video_id=' + videoId )
        break;
      case 2:
        window.open('/exercise/list/?video_id=' + videoId)
        break;
       
      case 3:
        window.open('/assess/info/?video_id=' + videoId)
        break;

      default:
        break;
    }
  }
  return func
})()
