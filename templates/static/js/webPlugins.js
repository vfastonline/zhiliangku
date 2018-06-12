function openUpload() {
    var ids = [];
    $("input[name='_selected_action']").each(function () {
        if ($(this).is(":checked")) {
            ids.push($(this).val());
        }
    });
    if (ids.length === 0) {
        layer.msg('先勾选一条视频类型信息！', {icon: 7});
        return false
    }
    else if (ids.length > 1) {
        layer.msg('最多选择一条视频类型数据！', {icon: 7});
        return false
    }

    var extra_obj = JSON.stringify({
        //status: 200,
        state: ids[0],//自定义参数，可以通过回调通知接口抓取到该字段
        keepsource: '1'//源文件播放（不对源文件进行编码）
    });

    $.getJSON("/tracks/get-polyv", function (data) {
        var obj1 = {
            "uploadButtton": 'upload',//打开上传控件按钮id
            "cataid": 1,//上传目录id
            "luping": 1,//开启视频课件优化处理，对于上传录屏类视频清晰度有所优化
            "extra": extra_obj,
            response: function (json) {
                // console.log(json);
                var scriptdata = "<script>\n" +
                    "var player = polyvObject('#plv_" + json.data.vid + "').videoPlayer({\n" +
                    "'width':'690',\n" +
                    "'height':'385',\n" +
                    "'vid' : '" + json.data.vid + "'" +
                    "});\n<\/script>";

                // document.getElementById("textbody").value = document.getElementById("textbody").value + scriptdata;
                layer.open({
                    type: 1,
                    area: ['600px', '360px'],
                    shadeClose: true, //点击遮罩关闭
                    content: scriptdata
                });

                //if close window
                // upload.closeWrap();

            }
        };

        obj1.writeToken = data.writeToken;
        obj1.userid = data.userid;
        obj1.ts = data.ts;
        obj1.hash = data.hash;
        obj1.sign = data.sign;
        obj1.readToken = data.readToken;

        var upload = new PolyvUpload(obj1);

        setInterval(function () {

            $.getJSON("/tracks/get-polyv", function (data) {
                upload.update(data);

            });
        }, 3 * 60 * 1000);
    });
}

function PolyvUpload(obj) {
    this.obj = obj;
    this.uploadButton = document.getElementById(obj.uploadButtton);
    this.sign = obj.sign;
    this.hash = obj.hash;
    this.ts = obj.ts;
    this.userid = obj.userid;
    this.cataid = obj.cataid;
    this.extra = obj.extra;
    this._init();
    if (obj.response != undefined) {
        this.responseMessage(obj.response);
    }
}

PolyvUpload.prototype.addHander = function (ele, type, handler) {
    if (ele.addEventListener) {
        ele.addEventListener(type, handler, false);
    } else if (ele.attachEvent) {
        ele.attachEvent("on" + type, handler);
    } else {
        ele["on" + type] = handler;
    }
};

PolyvUpload.prototype._init = function () {
    var self = this;
    var uploadButton = this.uploadButton;
    var url = self.url = "https://v.polyv.net/file/plug-in2/index.html";
    self.param = {
        "sign": self.sign,
        "userid": self.userid,
        "hash": self.hash,
        "ts": self.ts,
        "url": location.href,
        "extra": self.extra,
        "status": self.status,
        "cataid": self.cataid
    };
    var wrapAll = document.createElement("div"),
        wrap = document.createElement("div"),
        frameWrap = document.createElement("div"),
        cancle = document.createElement("span"),
        iframe = document.createElement("iframe");
    self.wrap = wrapAll;
    wrapAll.setAttribute("id", "wrapAll");
    cancle.setAttribute("id", "cancle");
    cancle.innerHTML = "x";
    wrapAll.style.display = "none";
    wrap.style.cssText = "display: block;";
    wrap.style.cssText = "display: block;position: fixed;left: 0;top: 0;width: 100%;height: 100%;z-index: 1001;background-color: #000;-moz-opacity: 0.5;opacity: .50;filter: alpha(opacity=50);";
    frameWrap.style.cssText = "display: block;position: fixed;left: 50%;top: 50%;width: 1000px;height: 600px;margin-top: -300px;margin-left: -500px;z-index: 1002;box-shadow: 0 0 25px rgba(0,0,0,0.7);border-radius: 10px;";
    cancle.style.cssText = "width: 26px;height: 26px;position: absolute;top: 0px;right: 0px;cursor: pointer;background: #eee;text-align: center;line-height: 26px;color: #666;font-size: 16px;font-family: microsoft yahei;";
    iframe.setAttribute("src", url);
    iframe.setAttribute("id", "polyvFrame");
    iframe.setAttribute("width", "1000");
    iframe.setAttribute("height", "600");
    iframe.style.cssText = "width: 100%;height: 100%;z-index: 1002;border:none;border-radius: 10px";
    frameWrap.appendChild(iframe);
    frameWrap.appendChild(cancle);
    wrapAll.appendChild(wrap);
    wrapAll.appendChild(frameWrap);
    document.getElementsByTagName("body")[0].appendChild(wrapAll);
    var polyvFrame = document.getElementById('polyvFrame');
    frameMsg = self.frameMsg = polyvFrame.contentWindow;
    polyvFrame.onload = polyvFrame.onreadystatechange = function () {
        if (this.readyState && this.readyState != 'complete') {
            return;
        } else {
            self.update();
        }
    };
    wrapAll.style.display = "block";
    cancle.onclick = function () {
        wrapAll.style.display = "none";
    };
};

PolyvUpload.prototype.update = function () {
    if (typeof arguments[0] === "object") {
        for (var i in arguments[0]) {
            this.param[i] = arguments[0][i];
        }
    }
    this.frameMsg.postMessage(JSON.stringify(this.param), this.url);
};

PolyvUpload.prototype.responseMessage = function (func) {
    this.addHander(window, "message", function (event) {
        func(JSON.parse(event.data));
    });
};

PolyvUpload.prototype.closeWrap = function () {
    this.wrap.style.display = "none";
};

$(document).ready(function ($) {
    $(".object-tools").append('<input class="btn btn-success" type="button" id="upload" value="上传 视频" onclick="openUpload()"></input>');
});