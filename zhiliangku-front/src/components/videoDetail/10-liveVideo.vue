<template>
  <div class=" incenter" :style="{height:height+'px'}">
    <!-- <object type="application/x-shockwave-Flash" width="600" height="100">
      <param value="opaque" name="wmode"></param>
      <embed wmode="opaque" type="application/x-shockwave-Flash"></embed>
    </object> -->
    <!-- 解释一下id是有脚本进行绑定的所以不能改变 -->
    <div class="video-box">
      <object v-if="showVideo"  type="application/x-shockwave-flash" data="http://player.polyv.net/live/player.swf" 
      :id="liveIdObj.id" width="100%" :height="height"
        class="polyvFlashObject">
        <param name="allowScriptAccess" value="always">
        <param name="allowFullScreen" value="true">
        <param name="quality" value="high">
        <param name="bgcolor" value="#ffffff">
        <param name="wmode" value="transparent">
        <param name="flashvars" :value="'is_barrage=on&amp;vid='+liveIdObj.id +'&amp;uid=a582a3b650&amp;useFastDns=off&amp;'">
      </object>
    </div>
    <!-- <div class=" video-box " id="e8888b74d1229efec6b4712e17cb6b7a_e"></div> -->
    <div v-if="showchat" class="wrap " :style="{height:height+'px'}">
      <div>
        <div class="text-container" :style="{height:height-48+'px'}">
          <ol class="talk" id="talk"></ol>
        </div>
        <!-- <div class="toolbar"><i class="icon pointer iconfont icon-biaoqing1"></i></div> -->
        <div class="ibox">
          <el-input @focus="jj" name="name" id="send"></el-input>
          <el-button class="sendbtn" id="sendBtn" type="primary">发送</el-button>
        </div>
        <!-- <div  class="emotions" id="emotions"> -->
      </div>
    </div>
    <div class="userwrap"></div>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
  .toolbar {
    .icon {
      margin-left: 15px;
      font-size: 20px;
    }
  }

  .ibox {
    .el-input {
      margin-left: 15px;
    }
  }

</style>
<style>
  @import "//at.alicdn.com/t/font_483463_1t9ycpancbjiqkt9.css";

</style>

<script>
  window.j2s_setBarrage = function () {
    return true;
  }
  // as
  window.s2j_broadcastBarrageMsg = function (e) {
    var str = '[{"msg":"' + e + '","fontSize":"24","fontColor":"0xCCCC00","fontMode":"roll"}]';
    player.j2s_addBarrageMessage(str);
  };
  import Bus from '../../assets/js/bus'
  import emotionslist from '../../assets/js/03-emotions'
  export default {
    data() {
      return {
        height: '',
        liveIdObj: {
          id: ''
        },
        showchat: true,
        showVideo:false,
      }
    },
    props: {

    },
    methods: {
      jj(event) {
        console.log(event)
        if (localStorage.nickname) return;
        event.target.blur();
        Bus.$emit('noActive', 'loginActive')
      },
      // 请求频道信息
      // 以下是直播
      liveVideo(id) {
        this.liveIdObj.id = id;
        this.showVideo=true;
        debugger
        // 精髓。。。
        Vue.nextTick(function(){
          this;
          debugger
          window.player = polyvObject('#e8888b74d1229efec6b4712e17cb6b7a_e').livePlayer({
          width: '100%',
          // height: window.innerHeight - 70,
          height: window.innerHeight,
          'flashvars': {
            "is_barrage": "on"
          },
          'uid': 'a582a3b650',
          'vid': id,
          'wmode': "opaque",
        });
        })       
      },
      initLiveVideo() {
        var time = Math.floor(new Date() / 1000);
        var sign = md5(time + 'polyvsign');
        var token = this.$get('http://api.live.polyv.net/watchtoken/gettoken?ts=' + time + '&sign=' + sign).then(res => {
          this.liveIdObj.token = token;
          console.log(res)
        })

      },
      createdLiveVideo() {

      },
      getchanlle() {

      },
      main(obj) {
        this.showchat = true;
        var that=this;
        var chatHost = 'http://chat.polyv.net:80', //socket连接地址
          chatHost2 = "http://apichat.polyv.net:80", //获取聊天内容地址
          chatToken = this.liveIdObj.token,
          roomId = this.liveIdObj.id,
          userId = Math.random(0, 1000 * 10000) * 1000 * 10000,
          nickname = localStorage.nickname || '游客', //自定义用户名
          // pic = this.$myConst.httpUrl +  localStorage.avatar || '/media/custom_user_avatar/defaultUserIcon.png';
          pic = '//livestatic.videocc.net/v_102/assets/wimages/missing_face.png';
        var $ = window.$;
        console.log($('#talk'))
        var socket = null;
        var $talk = $('#talk');

        function prettyTime(time) { //转换时间格式
          var now = new Date(time),
            year = now.getFullYear(),
            month = now.getMonth() + 1,
            date = now.getDate(),
            hours = now.getHours(),
            minutes = now.getMinutes();
          if (minutes < 10) {
            minutes = '0' + minutes;
          }
          return year + '/' + month + '/' + date + ' ' + hours + ':' + minutes;
        }

        function formatEmotions(_html) { //表情转换：表情以'[微笑]'的形式发送和接受，可以根据需要自定义表情形式
          var $emotions = $('#emotions');
          if (_html) {
            var _of = -1;
            while ((_of = _html.indexOf("[")) != -1) {
              var _oe = _html.indexOf("]", _of + 1);
              if (_oe == -1)
                break;
              var begin = _html.substring(0, _of);
              var end = _html.substring(_oe + 1);
              var valstr = _html.substring(_of + 1, _oe);
              if (valstr) {
                var urlstr = $emotions.find("[title='" + valstr + "']").attr('src');
                if (urlstr) {
                  valstr = '<img src="' + urlstr + '" class="emotionimg">';
                } else {
                  break;
                }
              } else {
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
          var logo = $('<div class="talk-logo"><img class="chat-user-icon" src=' + pic + '><div/>');
          var nick = $('<div class="nickname">' + data.user.nick + '</div>');
          var time = $('<div class="time">' + prettyTime(data.time) + ' </div>');
          var values = $('<div class="content-msg"></div>');
          values.text(content)
          var list = $('<li />');
          if (data.user.userId === userId) { //当前用户
            nick.addClass('owner');
          }
          list.append(logo, nick, time, values);
          $talk.append(list);
          // 接下来两行代码是为了每次有新消息到来之后使得滚动条在最下方
          var container = $('.text-container')[0];
          container.scrollTop = container.scrollHeight;
        }

        function getHistoryContent(start, end) { //获取过往的聊天内容
          var startIndex = start || 0,
            endIndex = end || startIndex + 9;
          var url = chatHost2 + '/front/history?roomId=' + roomId + '&start=' + startIndex + '&end=' + endIndex;
          $.ajax({
              url: url,
              type: 'get',
              dataType: 'jsonp'
            })
            .done(function (data) {
              $(data.reverse()).each(function (index, el) {
                addList(this); //生成dom添加到页面
              });
            });
        }
        getHistoryContent();

        function getOnlineUserList() { //获取当前用户列表
          $.ajax({
            url: chatHost2 + '/front/listUsers',
            dataType: 'jsonp',
            data: {
              roomId: roomId,
              page: 1,
              len: 100 //获取用户数目
            },
            success: function (users) {
              var t = '<p>当前用户数：' + users.count + '<p>';
              $(users.userlist).each(function () {
                var pic = this.pic;
                t += '<img src="' + pic + '" title="' + this.nick + '" /><br>';
              })
              $('.userwrap').html(t);
            }
          });
        }
        //每20秒刷新一次  
        // setInterval(getOnlineUserList, 20000); 
        //连接socket
        var supportsWebSockets = 'WebSocket' in window || 'MozWebSocket' in window;
        if (supportsWebSockets) {
          socket = io.connect(chatHost, {
            'query': 'token=' + chatToken,
            'transports': ['websocket']
          });
        } else {
          socket = io.connect(chatHost, {
            'query': 'token=' + chatToken,
            'transports': ['polling']
          });
        }
        socket.on('connect', function () {
          //连接服务器成功
          console.info('success');
          // getOnlineUserList();
          socket.emit('message', JSON.stringify({ //用户登录
            'EVENT': 'LOGIN',
            'values': [localStorage.nickname || '游客', pic, userId], //昵称、头像地址、用户id
            'roomId': roomId
          }));
        });
        socket.on('message', function (message) { //接收信息事件
          var data = JSON.parse(message);
          console.log(data);
          if (data && data.EVENT) { //根据返回的不同事件类型作相应处理
            switch (data.EVENT) {
              case 'CLOSEROOM': // room closed
                break;
              case 'GONGGAO': //系统公告
                break;
              case 'SPEAK': // 用户发言
                addList(data); //将用户发言生成dom添加到页面
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
              case 'CLOSE_DANMU': //关闭弹幕
                break;
              default:
                break;
            }
          }
        });

        function sendMsg() {
          if(!that.$fn.getCookie('token')){
            Bus.$emit('noActive', 'loginActive')
            return
          }
          var $that = $('#send');
          var value = $that.val().trim();
          if (value == "") {
            alert('内容为空');
            return;
          }
          var str = '[{"msg":"' + value + '","fontSize":"16","fontColor":"0xffffff","fontMode":"roll"}]';
          player.j2s_addBarrageMessage(str);
          var temp_user = {
            "nick": localStorage.nickname || '游客',
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
        $('#send').on('keypress', function (e) {
          if (e.which === 13) {
            sendMsg();
          }
        });
        $('#sendBtn').on('click', function () {
          sendMsg();
        });
        // 设置表情库
        function setEmotions() {
          var t = '';
          $(emotionslist).each(function () {
            t += '<img src="' + this.url + '" title="' + this.title + '" />';
          });
          $('#emotions').html(t);
        }
        setEmotions();
        $('#emotions').on('click', 'img', function () { //选择表情
          var $that = $(this),
            title = $that.attr("title");
          var value = $('#send').val() + '[' + title + ']'
          $('#send').val(value);
        });
      }
    },
    created() {

      this.height = window.innerHeight;
      // this.initLiveVideo()
    },
    mounted() {
      Bus.$on('haveLogin', () => {
        window.location.reload()
      })
      this.$on('liveid', function (id) {
        this.liveVideo(id);
        this.main();
      })
      Bus.$on('liveid', (id) => {
        this.liveVideo(id);
        this.main();
      })

    }
  }

</script>

<style>
  .videoModule {
    background: red;
    width: 1152px;
  }

  .video-box {
    float: left;
    position: relative;
    width: 80%;
    z-index: 1
  }

  .chat-box {
    margin-left: 80%;
    background: blue
  }

  .wrap {
    margin-left: 80%;
    width: 20%;
    position: relative;
    /* background: rgb(51, 55, 66) */
  }

  .chat-user-icon {
    width: 20px;
    height: 20px;
    border-radius: 50%;
  }

  .talk-logo img {
    width: 20px;
    height: 20px;
    border-radius: 25px;
  }

  .content-msg {
    display: block;
  }

  .ibox {
    height: 47px;
    display: flex;
    justify-content: space-between;
  }

  /* .ibox>* {
    float: left;
  } */

  .text-container {
    overflow-y: scroll;
  }

  input {
    display: inline-block;
    outline: none;
    /* flex-grow: 1; */
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

  .nickname,
  .time {
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
