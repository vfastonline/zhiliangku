<template>
  <div class=" incenter" :style="{height:height+'px'}">
    <!-- 播放器s -->
    <div class="video-box">
      <object v-if="showVideo" type="application/x-shockwave-flash" data="http://player.polyv.net/live/player.swf" :id="liveIdObj.id"
        width="100%" :height="height" class="polyvFlashObject">
        <param name="allowScriptAccess" value="always">
        <param name="allowFullScreen" value="true">
        <param name="bgcolor" value="#ffffff">
        <param name="wmode" value="transparent">
        <embed wmode="opaque" type="application/x-shockwave-Flash">
        <param name="flashvars" :value="'is_barrage=on&amp;vid='+liveIdObj.id +'&amp;uid=a582a3b650&amp;useFastDns=off&amp;'">
      </object>
    </div>
    <!-- 播放器e -->
    <!-- 聊天室s -->
    <div v-if="showchat" class="wrap " :style="{height:height+'px'}">
      <div>
        <div class="button-nav">
          <div class="chatButton " :class="{'activeButton':showChatRoom}">
            <!-- <img src="" alt=""> -->
            <span class="pointer button-item" @click="showChatRoom=true">
              <i class="iconfont  icon-msnui-bubble buttonIcon imgmiddle"></i> 聊天室</span>
          </div>
          <div class="onlinePeople " :class="{'activeButton':!showChatRoom}">
            <span class="pointer button-item" @click="showChatRoom=false">
              <i class="iconfont  icon-yonghu1 buttonIcon imgmiddle"></i> {{baseParam.number}}人在观看</span>
          </div>
        </div>
        <div class="text-container " :style="{height:height-211+'px'}">
          <ol v-if="showChatRoom" class="talk" id="talk">
            <li v-for="(item,index) in chatMsgList" :key="index">
              <!-- <div class="talk-logo">
                <img class="chat-user-icon" :src="item.imgsrc" alt="">
              </div> -->
              <div class="nickname " :class="{'owner':item.selfMsg}">{{item.nickname}}</div>
              <!-- <div class="time">{{prettyTime(item.time)}}</div> -->
              <div class="content-msg font14prffffff">{{item.content}}</div>
            </li>
          </ol>
          <ul class="userlist_container" v-else>
            <li v-for="item in baseParam.userlist" :key="item.userId">
              <img class="user_list_icon" :src="item.pic.substr(2)" alt="">
              <span class="nickname">{{item.nick}}</span>
            </li>
          </ul>
        </div>
        <div class="ibox">
          <div class="icon-func-container">
            <div><img class="pointer icon-func1" src="../../assets/img/icons/视频播放+习题图标/icon_60_flower_fill@2x.svg" alt="">
            <img class="pointer icon-func2" src="../../assets/img/icons/视频播放+习题图标/clap-hands.svg" alt=""></div>
            <div><img class="pointer icon-func3" src="../../assets/img/icons/视频播放+习题图标/emoticon.svg" alt=""></div>
          </div>
          <div>
            <textarea @focus="jj" name="name" placeholder="请输入文字，按enter键发送" class="msg-input" id="send"/>
            <!-- <el-button class="sendbtn" id="sendBtn" type="primary">发送</el-button> -->
          </div>
        </div>
      </div>
    </div>
    <!-- 聊天室e -->
    <div class="userwrap"></div>
  </div>
</template>
<style lang="scss">
  .toolbar {
    .icon {
      margin-left: 15px;
      font-size: 20px;
    }
  }

  .user_list_icon {
    height: 48px;
    width: 48px;
    border-radius: 50%;
    margin-right: 16px;
  }

  .ibox {
    .el-input {
      margin-left: 15px;
    }
  }

  .button-nav {
    height: 70px;
    background: #333742;
    line-height: 70px;
    position: relative;
    border-bottom: 1px solid #333742;
  }

  .chatButton {
    float: left;
    padding-left: 19px;
    width: 40%;
    height: 70px;
    box-sizing: border-box;
  }
  .button-item{
    height: 32px;
    line-height:32px;
    display: inline-block;
  }
  .onlinePeople {
    float: left;
    padding-left: 19px;
    width: 60%;
    height: 70px;
    box-sizing: border-box;
  }

  .activeButton {
    background: #535762;
  }

  .activeButton span {
    color: white
  }

  .button-nav .buttonIcon {
    font-size: 32px;
  }
  .icon-func-container{
    height: 80px;
    line-height: 80px;
    display: flex;
    justify-content: space-between;
  }
  .icon-func1{
    margin:0   28px 0    28px;
  }
  .icon-func2{
     margin:0 28px 0 0;
  }
  .icon-func3{
    margin-right:28px;
  }
  .msg-input{
    width:210px;
    padding-right:8px;
    position: relative;
    display: block;
    border: none;
    background: transparent;
    margin-left:28px;
    color: white;
    resize: none;
  }
  .msg-input :focus{
    outline: none;
  }
  .msg-input :placeholder{
    color: #A9ABB0;
  }
</style>
<style>
  @import "//at.alicdn.com/t/font_577305_itisanydxrxgk3xr.css";

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
        showChatRoom: true,
        showchat: true,
        showVideo: false,
        chatMsgList: [],
        baseParam: {
          chatHost: 'http://chat.polyv.net:80',
          chatHost2: "http://apichat.polyv.net:80",
          userId: '',
          number: '',
          userlist: [],
        }
      }
    },
    props: {

    },
    methods: {
      jj(event) {
        if (localStorage.nickname) return;
        event.target.blur();
        Bus.$emit('noActive', 'loginActive')
      },
      // 请求频道信息
      // 以下是直播
      liveVideo(id) {
        this.liveIdObj.id = id;
        this.showVideo = true;
        // 精髓。。。
        Vue.nextTick(function () {
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
      prettyTime(time) { //转换时间格式
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
      },
      // aaa
      formatEmotions(_html) { //表情转换：表情以'[微笑]'的形式发送和接受，可以根据需要自定义表情形式
        var $emotions = window.$('#emotions');
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
      },
      addList(data) {
        var obj = {};
        var content = data.content || data.values[0];
        obj.content = this.formatEmotions(content);
        obj.imgsrc = data.user.pic;
        obj.nickname = data.user.nick;
        obj.time = data.time;
        if (data.user.userId == this.baseParam.userId) {
          obj.self = true;
        }
        this.chatMsgList.push(obj)
        var str = '[{"msg":"' + content + '","fontSize":"16","fontColor":"0xffffff","fontMode":"roll"}]';
        // 这里会有报错信息，在初始化聊天列表的时候。但是不影响弹幕功能的使用，所以禁止报错了
        try {
          window.player.j2s_addBarrageMessage(str);
        } catch (err) {}
        // 接下来两行代码是为了每次有新消息到来之后使得滚动条在最下方
        Vue.nextTick(function (dom) {
          var container = window.$('.text-container')[0];
          $(".text-container").getNiceScroll().resize();
          $(".text-container").getNiceScroll(0).doScrollTop(container.scrollHeight, 0.2);
        })
      },
      getHistoryContent(start, end) { //获取过往的聊天内容
        var vue = this;
        var startIndex = start || 0,
          endIndex = end || startIndex + 9;
        var url = this.baseParam.chatHost2 + '/front/history?roomId=' + this.liveIdObj.id + '&start=' + startIndex +
          '&end=' + endIndex;
        window.$.ajax({
            url: url,
            type: 'get',
            dataType: 'jsonp'
          })
          .done(function (data) {
            window.$(data.reverse()).each(function (index, el) {
              // aaaa
              vue.addList(this); //生成dom添加到页面
            });
          });
      },
      getOnlineUserList() { //获取当前用户列表
        var chatHost2 = this.baseParam.chatHost2,
          roomId = this.liveIdObj.id,
          vue = this;
        window.$.ajax({
          url: chatHost2 + '/front/listUsers',
          dataType: 'jsonp',
          data: {
            roomId: roomId,
            page: 1,
            len: 1000 //获取用户数目
          },
          success: function (users) {
            vue.baseParam.number = users.count;
            vue.baseParam.userlist = users.userlist;
          }
        });
        window.$('.user_list_icon').niceScroll({
          cursorcolor: "#424242",
        })

      },
      sendMsg() {
        if (!this.$fn.getCookie('token')) {
          Bus.$emit('noActive', 'loginActive')
          return
        }
        var $that = $('#send');
        var value = $that.val().trim();
        if (value == "") {
          alert('内容为空');
          return;
        }
        // var str = '[{"msg":"' + value + '","fontSize":"16","fontColor":"0xffffff","fontMode":"roll"}]';
        // player.j2s_addBarrageMessage(str);
        var temp_user = {
          "nick": localStorage.nickname || '游客',
          "pic": this.baseParam.imgsrc,
          "userId": this.baseParam.userId
        }
        var obj = {
          'user': temp_user,
          'time': new Date().getTime(),
          'content': value
        }
        this.addList(obj);
        var data = JSON.stringify({
          'EVENT': 'SPEAK',
          'values': [value],
          'roomId': this.liveIdObj.id
        });
        this.socket.emit('message', data); //发送消息
        $that.val('');
      },
      main(obj) {
        var vue = this;
        this.showchat = true;
        Vue.nextTick(() => {
          // console.log(window.$('.text-container')[0].value)
          window.$('.text-container').niceScroll({
            cursorcolor: "#424242",
          })
          window.$('.msg-input').niceScroll({
            cursorcolor: "#424242",
          })
          $(".text-container").getNiceScroll().resize();
        })
        var that = this;
        var chatHost = 'http://chat.polyv.net:80', //socket连接地址
          chatHost2 = "http://apichat.polyv.net:80", //获取聊天内容地址
          chatToken = this.liveIdObj.token,
          roomId = this.liveIdObj.id,
          userId = Math.random(0, 1000 * 10000) * 1000 * 10000,
          nickname = localStorage.nickname || '游客', //自定义用户名
          // aaaa
          //此处的pic参数有保利威视的限制：有具体域名地址的形式
          pic = '//' + this.$myConst.httpUrl + (localStorage.avatar || '/media/custom_user_avatar/defaultUserIcon.png');
        // pic = '//livestatic.videocc.net/v_102/assets/wimages/missing_face.png';
        this.baseParam.userId = userId;
        var $ = window.$;
        var $talk = $('#talk');
        this.getHistoryContent();
        //每20秒刷新一次  
        // setInterval(vue.getOnlineUserList(), 2000); 
        //连接socket
        var socket = null;
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
        this.socket = socket;
        socket.on('connect', function () {
          //连接服务器成功
          console.info('success');
          vue.getOnlineUserList();
          socket.emit('message', JSON.stringify({ //用户登录
            'EVENT': 'LOGIN',
            'values': [localStorage.nickname || '游客', pic, userId], //昵称、头像地址、用户id
            'roomId': roomId
          }));
        });
        socket.on('message', (message) => { //接收信息事件
          var data = JSON.parse(message);
          console.log(data);
          if (data && data.EVENT) { //根据返回的不同事件类型作相应处理
            switch (data.EVENT) {
              case 'CLOSEROOM': // room closed
                break;
              case 'GONGGAO': //系统公告
                break;
              case 'SPEAK': // 用户发言
                this.addList(data); //将用户发言生成dom添加到页面
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
                window.$talk.empty();
                break;
              case 'CLOSE_DANMU': //关闭弹幕
                break;
              default:
                break;
            }
          }
        });

        $('#send').on('keypress', function (e) {
          if (e.which === 13) {
            vue.sendMsg();
          }
        });
        $('#sendBtn').on('click', function () {
          vue.sendMsg();
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
      window.$('body').niceScroll()
      this.height = window.innerHeight;
      // this.initLiveVideo()
    },
    mounted() {
      var that = this;
      setInterval(function () {
        that.getOnlineUserList()
      }, 2000);
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
      setTimeout(function(){
        window.$('body').niceScroll().doScrollTop(70,0.5)
      },1500)
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
    background: #535762;
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
    position: relative;
    z-index:10;
    height: 140px;
    background-color:#333742;
    box-shadow: 0 -5px 2px #333742;
  }

  .text-container {
    overflow-y: scroll;
    overflow-x: hidden;
  }

  .text-container .el-scrollbar__wrap {
    overflow-x: hidden;
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
    /* border-bottom: 1px solid #e5e5e5; */
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
    font-size: 14px;
    color: #a9abb0;
    font-family: 'PingFangSC-Regular', 'Microsoft YaHei';
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
