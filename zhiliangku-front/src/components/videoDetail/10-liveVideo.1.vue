<template>
  <div class=" incenter live-video-box" :style="{height:height+'px'}">
    <!-- <button @click="kk()">1231231321</button>
    <input type="text" v-model="test" @keydown.enter="sendAnwser(test)"> -->
    <!-- 播放器s -->
    <div class="video-box" :height="height">
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
      <div class="relative">
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
        <transition name="fade" >
        <div v-if="showAnswerSelect" class="answer-container">
          <el-button v-for="item in AnswerList" :key="item" @click="sendAnwser(item)" class="answer-item fontcenter pointer">{{item.label}}</el-button>
        </div>
        </transition>
        <div class="text-container " :style="{height:height-211+'px'}">
          <ol v-show="showChatRoom" class="talk" id="talk">
            <li v-for="(item,index) in chatMsgList" :key="index">
              <div v-if="item.type==1">
                <div class="nickname " :class="{'owner':item.selfMsg}">{{item.nickname}}</div>
                <!-- <div class="time">{{prettyTime(item.time)}}</div> -->
                <div class="content-msg font14prffffff">
                  <span v-for="(msgPice,index) in item.content" :key="index">
                    <span v-if="msgPice.type==2" v-text="msgPice.html"></span>
                    <span v-if="msgPice.type==1" v-html="msgPice.html"></span>
                  </span>
                </div>
              </div>
              <div v-if="[2,3].indexOf(item.type*1)+1" class="present-container fontcenter">
                <div>{{item.nickname}}</div>
                <div>
                  <svg v-if="item.type==2" class="present-icon" aria-hidden="true">
                    <use xlink:href="#icon-xianhua-"></use>
                  </svg>
                  <svg v-if="item.type==3" class="present-icon" aria-hidden="true">
                    <use xlink:href="#icon-car__easyicon"></use>
                  </svg>
                </div>
              </div>
            </li>
          </ol>
          <ul class="userlist_container" v-show="!showChatRoom">
            <li v-for="item in baseParam.userlist" :key="item.userId">
              <img class="user_list_icon" v-lazy="item.pic.substr(2)" alt="">
              <span class="nickname">{{item.nick}}</span>
            </li>
          </ul>
        </div>

        <div class="ibox">
          <div v-show="showEmoji" @click.stop="hh" class="emoji-container">
            <span @click.stop="selectEmoji(item)" class="emoji-inner pointer" v-for="item in emojiList" :key="item.className" v-html='item.htmlStr'>
            </span>
          </div>
          <div class="icon-func-container">
            <div>
              <img @click="sendMsg('%E9%80%81%E5%87%BA%E4%BA%86%E9%B2%9C%E8%8A%B1')" class="pointer icon-func1" src="../../assets/img/icons/视频播放+习题图标/icon_60_flower_fill@2x.svg"
                alt="">
              <!-- <img @click="sendMsg('%E7%BB%99%E5%87%BA%E4%BA%86%E7%83%AD%E7%83%88%E7%9A%84%E6%8E%8C%E5%A3%B0')" class="pointer icon-func2"
                src="../../assets/img/icons/视频播放+习题图标/clap-hands.svg" alt=""> -->
              <svg @click="sendMsg('%E7%BB%99%E5%87%BA%E4%BA%86%E7%83%AD%E7%83%88%E7%9A%84%E6%8E%8C%E5%A3%B0')" class="icon-paoche icon-func2 pointer"
                aria-hidden="true">
                <use xlink:href="#icon-qiche"></use>
              </svg>
            </div>
            <div>
              <img @click.stop="showEmoji=!showEmoji" class="pointer icon-func3" src="../../assets/img/icons/视频播放+习题图标/emoticon.svg" alt="">
            </div>
          </div>
          <div>
            <textarea @focus="jj" name="name" ref="sendMessage" placeholder="请输入文字，按enter键发送" class="msg-input" id="send" />
            <!-- <el-button class="sendbtn" id="sendBtn" type="primary">发送</el-button> -->
          </div>
        </div>
      </div>
    </div>
    <!-- 聊天室e -->
    <div class="userwrap"></div>
  </div>
</template>
<style scoped type="text/css">
.fade-enter-active, .fade-leave-active {
  transition: opacity .65s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
  .answer-container {
    box-sizing: border-box;
    position: absolute;
    height: 60px;
    display: flex;
    width:100%;
    z-index:10;
    justify-content: space-between;
    align-items: center;
  }
  .answer-container .el-button{
    padding: 0;
  }
  .answer-container .el-button+.el-button{
    margin: 0px;
  }
  .answer-item {
    height: 48px;
    width:48px;
    background: white;
    border-radius: 8px;
  }

</style>

<style type="text/css">
  .icon {
    width: 32px;
    height: 32px;
    vertical-align: middle;
    fill: currentColor;
    overflow: hidden;
  }

  .present-icon {
    width: 80px;
    height: 80px;
    vertical-align: middle;
    fill: currentColor;
  }

  .icon-paoche {
    width: 28px;
    height: 28px;
    /* vertical-align: middle; */
    fill: currentColor;
    overflow: hidden;
    margin-top: 3px;
  }

</style>
<style lang="scss">
  .present-container {
    width: 200px;
    background: #3f424b;
    border-radius: 5px;
    padding: 5px
  }

</style>

<style lang="scss">
  .emoji-container {
    box-sizing: border-box;
    padding-left: 8px;
    display: flex;
    width: 100%;
    flex-wrap: wrap;
    justify-content: flex-start;
    position: absolute;
    transform: translate(0, -100%);
    background: #333742;
    border-bottom: 1px solid #535762;
  }

  .emoji-inner {
    display: inline-block;
    margin: 5px;
  }

</style>

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

  .button-item {
    height: 32px;
    line-height: 32px;
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

  .icon-func-container {
    height: 80px;
    line-height: 80px;
    display: flex;
    justify-content: space-between;
  }

  .icon-func1 {
    margin: 0 28px 0 28px;
  }

  .icon-func2 {
    margin: 0 28px 0 0;
  }

  .icon-func3 {
    margin-right: 28px;
  }

  .msg-input {
    width: 210px;
    padding-right: 8px;
    position: relative;
    display: block;
    border: none;
    background: transparent;
    margin-left: 28px;
    color: white;
    resize: none;
  }

  .msg-input :focus {
    outline: none;
  }

  .msg-input :placeholder {
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
  import VueLazyLoad from 'vue-lazyload'
  Vue.use(VueLazyLoad, {})
  export default {
    data() {
      return {
        test:'',
        showEmoji: '',
        height: '',
        liveIdObj: {
          id: ''
        },
        showChatRoom: true,
        showchat: true,
        showVideo: false,
        showAnswerSelect: false,
        AnswerList: [],
        chatMsgList: [],
        baseParam: {
          chatHost: 'http://chat.polyv.net:80',
          chatHost2: "http://apichat.polyv.net:80",
          userId: '',
          number: '',
          userlist: [],
        },
        emojiList: [],
      }
    },
    props: {},
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
      formatEmotions(_html) {
        // 这个函数是不够完善的，希望有更好的办法进行修复
        var $emotions = window.$('#emotions');
        var contentArry = [],
          endArry = [];
        var arr = _html.split(/[[]/g)
        var brr;
        arr.forEach((item) => {
          item.split(/[\]]/g).forEach((item) => {
            contentArry.push(item)
          })
        })
        contentArry.forEach((item) => {
          if (item === '') {
            return
          }
          var obj = {},
            b;
          if (this.emojiList.some((el, index) => {
              if (el.name == item) {
                b = el;
                return true
              }
            })) {
            obj.type = 1;
            obj.html = "<svg class='icon' aria-hidden='true'><use xlink:href='#icon-emoji-" + b.index +
              "'></use></svg>";
          } else {
            obj.type = 2;
            obj.html = item
          }
          endArry.push(obj)
        })
        return endArry
      },
      addpresent(type, data) {
        var obj = {};
        obj.imgsrc = data.user.pic;
        obj.nickname = data.user.nick;
        obj.time = data.time;
        obj.type = type
        // 判断是否是自己发送的消息
        if (data.user.userId == this.baseParam.userId) {
          obj.self = true;
        }
        this.chatMsgList.push(obj)
        this.refreshScroll()
        // console.log(this.chatMsgList)
      },
      addList(data) {
        var content = data.content || data.values[0];
        if (content == '%E9%80%81%E5%87%BA%E4%BA%86%E9%B2%9C%E8%8A%B1') {
          this.addpresent(2, data)
          return
        }
        if (content == '%E7%BB%99%E5%87%BA%E4%BA%86%E7%83%AD%E7%83%88%E7%9A%84%E6%8E%8C%E5%A3%B0') {
          this.addpresent(3, data)
          return
        }
        var obj = {};

        obj.content = this.formatEmotions(content);
        obj.imgsrc = data.user.pic;
        obj.nickname = data.user.nick;
        obj.time = data.time;
        obj.type = '1'
        // 判断是否是自己发送的消息
        if (data.user.userId == this.baseParam.userId) {
          obj.self = true;
        }
        this.chatMsgList.push(obj)
        // console.log(this.chatMsgList)
        var str = '[{"msg":"' + content + '","fontSize":"16","fontColor":"0xffffff","fontMode":"roll"}]';
        // 这里会有报错信息，在初始化聊天列表的时候。但是不影响弹幕功能的使用，所以禁止报错了
        try {
          window.player.j2s_addBarrageMessage(str);
        } catch (err) {}
        // 接下来两行代码是为了每次有新消息到来之后使得滚动条在最下方
        this.refreshScroll()
      },
      refreshScroll() {
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
      sendMsg(othervalue) {
        if (!this.$fn.getCookie('token')) {
          Bus.$emit('noActive', 'loginActive')
          return
        }
        var $that = $('#send');
        var value = $that.val().trim();
        if (othervalue) {
          value = othervalue;
        }
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
        this.showEmoji = false;
      },
      main(obj) {
        var vue = this;
        this.showchat = true;
        Vue.nextTick(() => {
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
          console.log(message);
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
                this.getQuestion(data)
                break;
              case 'CLOSE_QUESTION':
                this.closeQuestion()
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
      },
      // 表情部分开始
      initEmojiList() {
        this.emojiList.push({
          className: 'icon-emoji-',
          name: 'emoji-1',
          htmlStr: "<svg class='icon' aria-hidden='true'><use xlink:href='#icon-emoji-'></use></svg>",
          index: ''
        })
        for (let i = 1; i <= 20; i++) {
          var obj = {};
          obj.name = 'emoji-' + (i + 1);
          obj.className = 'icon-emoji-' + i;
          obj.htmlStr = "<svg class='icon' aria-hidden='true'><use xlink:href='#icon-emoji-" + i + "'></use></svg>";
          obj.index = i;
          this.emojiList.push(obj)
        }
        // console.log(this.emojiList)
      },
      selectEmoji(item) {
        if (!this.$fn.getCookie('token')) {
          Bus.$emit('noActive', 'loginActive')
          return
        }
        window.$('#send')[0].value += ('[' + item.name + ']');
        this.$refs.sendMessage.focus();
      },
      // 进入页面之后延时滚动
      hh() {
        setTimeout(function () {
          if (window.scrollY) return;
          var body = $("html, body");
          body.stop().animate({
            scrollTop: 70
          }, 1000, 'swing', );
        }, 1000)
      },
      // 回答选择题功能
      getQuestion(data) {
        this.showAnswerSelect = true;
        if(data.question=='PD'){
          this.AnswerList=[{label:'正确',value:'correct'},{label:'错误',value:'error'}]
          return
        }
        var arr=[];
        data.question.split('').forEach((el,index)=>{
          var obj={};
          obj.value=el;
          obj.label=el;
          arr.push(obj)
        })
        this.AnswerList=arr;
      },
      sendAnwser(item) {
        var obj = {
          EVENT: 'ANSWER',
          roomId: this.liveIdObj.id,
          answer:item.value,
        }
        this.socket.emit('message', JSON.stringify(obj));
        this.showAnswerSelect=false
      },
      closeQuestion(){
        this.showAnswerSelect=false;
      },
      kk(){
        this.showAnswerSelect=true;
        this.AnswerList=['a','b','c','d','e']
      }
    },
    created() {
      this.initEmojiList();
      // window.$('body').niceScroll()
      this.height = window.innerHeight;
      // this.initLiveVideo()
    },
    mounted() {
      var that = this;
      setInterval(function () {
        that.getOnlineUserList()
      }, 2000);
      if (!window.scrollY) {
        this.hh()
      }
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
      document.addEventListener('click', (e) => {
        this.showEmoji = false
      })
    }
  }

</script>

<style scoped>
  .videoModule {
    background: red;
    width: 1152px;
  }

  .video-box {
    float: left;
    position: relative;
    overflow: hidden;
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
    z-index: 10;
    height: 140px;
    background-color: #333742;
    box-shadow: 0 -5px 2px #333742;
  }

  .text-container {
    overflow-y: scroll;
    overflow-x: hidden;
  }

  .text-container .el-scrollbar__wrap {
    overflow-x: hidden;
  }

  .live-video-box input {
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

  .live-video-box {
    overflow: hidden;
  }

  .live-video-box h2 {
    text-align: right;
    font-weight: 500;
  }

  .live-video-box li {
    margin: 10px;
    /* border-bottom: 1px solid #e5e5e5; */
    padding-bottom: 10px;
  }

  .live-video-box li>div {
    display: inline-block;
    margin-left: 20px;
  }

  .video-box li img {
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
