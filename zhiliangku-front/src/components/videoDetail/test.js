

    var showBtn = $("#showB");
    var hideBtn = $("#hideB");
    var sendBtn = $("#sendB");
    var input = $("#msgB");
    var playBtn = $("#play");

     var player = polyvObject('#player').livePlayer({
         'width':'100%',
         'height':'400',
         'flashvars':{"is_barrage":"on"},
         'uid':'efbb4ae8ac',
         'vid':'117882',
		 //'hideInput':'on',
         //'isBarrage':'off',
         //'hideControls':'2'
     });
	 
	 
	
     /**
      * [start barrage panel]
      * @return {[type]} [description]
      */
    function j2s_setBarrage()
    {
        return true;
    }

    /**
     * [show barrage panel]
     * @param  {[type]} e){                     player.j2s_showBarrage();    } [description]
     * @return {[type]}      [description]
     */
    showBtn.bind("click",function(e){
        player.j2s_showBarrage();
    });

    /**
     * [hide barrage panel]
     * @param  {[type]} e){                     player.j2s_hideBarrage();    } [description]
     * @return {[type]}      [description]
     */
    hideBtn.bind("click",function(e){
        player.j2s_hideBarrage();
    });

    /**
     * [send barrage message]
     * @param  {String} e){                     var str [description]
     * @return {[type]}      [description]
     */
    sendBtn.bind("click",function(e){
        var str = '[{"msg":"'+ input.val() +'","fontSize":"24","fontColor":"0xCCCC00","fontMode":"roll"}]';
        player.j2s_addBarrageMessage(str);
        input.val("");
    });
	window.s2j_broadcastBarrageMsg = function(e) {
		var str = '[{"msg":"'+ e +'","fontSize":"24","fontColor":"0xCCCC00","fontMode":"roll"}]';
		player.j2s_addBarrageMessage(str);
		input.val("");
	 };


