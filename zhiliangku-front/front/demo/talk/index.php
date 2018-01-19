<?php
$ts = time();
$sign = md5($ts."polyvsign");
$token = file_get_contents("http://api.live.polyv.net/watchtoken/gettoken?ts=".$ts."&sign=".$sign);
$token = trim(preg_replace('/\s\s+/', ' ', $token)); //登录taken
$roomId = "118206";  //房间号
$userId = rand(1000000,10000000);  //自定义用户id
$pic = 'http://livestatic.videocc.net/assets/wimages/missing_face.png';
?>
<!DOCTYPE html>
<html>
 <head>
 <meta charset="utf-8">
 <title>talk</title>
 <style media="screen">
 * {
 box-sizing: border-box;
 }
 html {
 font-family: "microsoft yahei";
 }
 .wrap {
 width: 850px;
 margin: 0 auto;
 position: relative;
 }

 .wrap>div:nth-child(1) {
 margin-right: 120px;
 }

 .wrap>div:nth-child(2){
 width: 100px;
 position: absolute;
 right: 0;
 top: 0;
 }

 .talk-logo img {
 width: 50px;
 height: 50px;
 border-radius: 25px;
 }

 .ibox {
 overflow: auto;
 display: flex;
 justify-content: space-between;
 }

 .ibox>* {
 float: left;
 }

 input {
 display: inline-block;
 height: 35px;
 padding: 5px;
 border-radius: 4px;
 outline: none;
 flex-grow: 1;
 border: 1px solid #d5d5d5;

 }

 .sendbtn {
 display: inline-block;
 border: 1px solid #e5e5e5;
 font-size: 14px;
 height: 35px;
 line-height: 35px;
 color: #fff;
 border-radius: 4px;
 padding: 0 30px;
 background: #14a2f4;
 margin-left: 15px;
 cursor: pointer;
 }

 h2 {
 text-align: right;
 font-weight: 500;
 }

 li {
 margin: 10px;
 border-bottom: 1px solid #e5e5e5;
 padding-bottom: 10px;
 }

 li>div {
 display: inline-block;
 margin-left: 20px;
 }
 li img {
 vertical-align: middle;
 }

 .nickname,.time {
 font-size: 12px;
 color: #666;
 }
 .owner {
 color: blue !important;
 }

 .userwrap {
 font-size: 14px;
 }

 .userwrap img {
 width: 50px;
 height: 50px;
 border-radius: 25px;
 }

 .emotions {
 margin-top: 20px;
 margin-bottom: 50px;
 }

 .emotions img {
 width: 30px;
 height: 30px;
 cursor: pointer;
 }
 .emotionimg {
 width: 30px;
 height: 30px;
 }
 </style>
 <script src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-2.2.4.min.js"></script>
    <script src="http://livestatic.videocc.net/assets/wjs/dist/socket.io.min.js "></script> <!-- 必须引入socketio -->
    <script src="emotions.js"></script> <!-- 表情列表，可根据需要设定表情 -->
    <script type="text/javascript">
      var chatHost = 'http://chat.polyv.net:80',  //socket连接地址
          chatHost2 = "http://apichat.polyv.net:80",  //获取聊天内容地址
          chatToken = '<?php echo $token ?>',
          roomId = '<?php echo $roomId ?>',
          userId = '<?php echo $userId ?>',
          nickname = 'polyv-test',   //自定义用户名
          pic = '<?php echo $pic ?>';
      // 若需要使用https，请使用下面的地址
      // chatHost = 'https://chat.polyv.net:443';
      // chatHost2 = 'https://apichat.polyv.net';
    </script>
 </head>
 <body>
 <div class="wrap">
 <div>
 <div>
 <h1>聊天室Demo</h1>
 <hr>
 <h2>信息</h2>
 <ol class="talk" id="talk"></ol>
 </div>
 <hr>
 <div class="ibox">
 <input type="text" name="name" id="send">
 <span class="sendbtn" id="sendBtn">发送</span>
 </div>
 <div class="emotions" id="emotions">

 </div>
 </div>
 <div class="userwrap"></div>
 </div>

 <script type="text/javascript">
 var socket = null;
 $talk = $('#talk');
 function prettyTime(time){ //转换时间格式
 var now = new Date(time),
 year = now.getFullYear(),
 month = now.getMonth() + 1,
 date = now.getDate(),
 hours = now.getHours(),
 minutes = now.getMinutes();
 if(minutes < 10) {
 minutes = '0' + minutes;
 }
 return year + '/' + month + '/' + date + ' ' + hours + ':' + minutes;
 }
function formatEmotions (_html) { //表情转换：表情以'[微笑]'的形式发送和接受，可以根据需要自定义表情形式
        var $emotions = $('#emotions');
            if (_html) {
                var _of =- 1;
                while ((_of = _html.indexOf("["))!=-1) {
                    var _oe = _html.indexOf("]", _of + 1);
                    if (_oe==-1)
                        break;
                    var begin = _html.substring(0, _of);
                    var end = _html.substring(_oe + 1);
                    var valstr = _html.substring(_of + 1, _oe);
                    if (valstr) {
                        var urlstr = $emotions.find("[title='"+ valstr +"']").attr('src');
                        if (urlstr) {
                          valstr = '<img src="' + urlstr + '" class="emotionimg">';
                        }else{
                          break;
                        }
                    }else{
                      break;
                    }
                    _html = begin + valstr + end;
                }
            }
            return _html;
        };
function addList(data) {
        var content = data.content || data.values[0];
        content = formatEmotions(content);
        var pic = data.user.pic;
        var logo = $('<div class="talk-logo"><img src=' + pic + '><div/>');
        var nick = $('<div class="nickname">' + data.user.nick + '</div>');
        var time = $('<div class="time">' + prettyTime(data.time) + ' | </div>');
        var values = $('<div>' + content + '</div>');
        var list = $('<li />');
        if(data.user.userId === userId) {  //当前用户
          nick.addClass('owner');
        }
        list.append(logo,nick,time,values);
        $talk.append(list);
      }
function getHistoryContent(start,end) {  //获取过往的聊天内容
        var startIndex = start || 0,
            endIndex = end || startIndex + 9;
        var url = chatHost2 + '/front/history?roomId=' + roomId + '&start=' + startIndex + '&end=' + endIndex;
        $.ajax({
          url: url,
          type: 'get',
          dataType: 'jsonp'
        })
        .done(function(data) {
          $(data.reverse()).each(function(index, el) {
            addList(this);  //生成dom添加到页面
          });
        });
      }
      getHistoryContent(); 
function getOnlineUserList(){  //获取当前用户列表
        $.ajax({
              url: chatHost2 + '/front/listUsers',
              dataType: 'jsonp',
              data: {
                roomId: roomId,
                page: 1,
                len: 100 //获取用户数目
              },
              success: function(users) {
                var t = '<p>当前用户数：' + users.count + '<p>';
                $(users.userlist).each(function(){
                  var pic = this.pic;
                  t += '<img src="'+ pic +'" title="' + this.nick + '" /><br>';
                })
                $('.userwrap').html(t);
              }
          });
      }
setInterval(getOnlineUserList, 20000);  //每20秒刷新一次  

//连接socket
      var  supportsWebSockets = 'WebSocket' in window || 'MozWebSocket' in window;
      if(supportsWebSockets)
      {
        socket = io.connect(chatHost, {
          'query': 'token=' + chatToken,
          'transports' : ['websocket']
        });
      }
      else
      {
        socket = io.connect(chatHost, {
          'query': 'token=' + chatToken,
          'transports' : ['polling']
        });
      } 

socket.on('connect', function() {
        //连接服务器成功
        console.info('success');
        getOnlineUserList();
        socket.emit('message', JSON.stringify({ //用户登录
          'EVENT': 'LOGIN',
          'values': [nickname, pic, userId], //昵称、头像地址、用户id
          'roomId': roomId
        }));
      });
      socket.on('message',function(message){  //接收信息事件
        var data = JSON.parse(message);
        console.log(data);
        if (data && data.EVENT) { //根据返回的不同事件类型作相应处理
          switch (data.EVENT) {
            case 'CLOSEROOM': // room closed
              break;
            case 'GONGGAO': //系统公告
                break;
            case 'SPEAK': // 用户发言
              addList(data);  //将用户发言生成dom添加到页面
              break;
            case 'REWARD': //奖励信息
                break;
            case 'QUESTION':
                break;
            case 'CLOSE_QUESTION':
                break;
            case 'ANSWER':
                 break;
            case 'ERROR': // 出错了
              break;
            case 'KICK': // 用户被踢
              break;
            case 'REMOVE_HISTORY': //清空聊天记录
              $talk.empty();
              break;
            case 'CLOSE_DANMU'://关闭弹幕
              break;
            default:
              break;
          }
        }
      });
      function sendMsg() {
        var $that = $('#send');
        var value = $that.val().trim();
        if(value == "") {
          alert('内容为空');
          return;
        }
        var temp_user = {
          "nick": nickname,
          "pic": pic,
          "userId": userId
        }
        var obj = {
          'user': temp_user,
          'time': new Date().getTime(),
          'content': value
        }
        addList(obj);
        var data = JSON.stringify({
          'EVENT': 'SPEAK',
          'values': [value],
          'roomId': roomId
        });
        socket.emit('message', data); //发送消息
        $that.val('');
      }
      $('#send').on('keypress',function(e){
        if(e.which === 13) {
          sendMsg();
        }
      });
      $('#sendBtn').on('click',function(){
        sendMsg();
      });      
function setEmotions() {
        var t = '';
        $(emotionslist).each(function(){
          t += '<img src="'+ this.url +'" title="' + this.title + '" />';
        });
        $('#emotions').html(t);
      }
      setEmotions();      
$('#emotions').on('click','img',function(){ //选择表情
        var $that = $(this),
            title = $that.attr("title");
            value = $('#send').val() + '[' + title + ']'
        $('#send').val(value);
      });

    </script>
  </body>
</html>