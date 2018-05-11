function scrollToTop(scrollDuration) {
    const   scrollHeight = window.scrollY,
            scrollStep = Math.PI / ( scrollDuration / 15 ),
            cosParameter = scrollHeight / 2;
    var     scrollCount = 0,
            scrollMargin,
            scrollInterval = setInterval( function() {
                if ( window.scrollY != 0 ) {
                    scrollCount = scrollCount + 1;  
                    scrollMargin = cosParameter - cosParameter * Math.cos( scrollCount * scrollStep );
                    window.scrollTo( 0, ( scrollHeight - scrollMargin ) );
                } 
                else clearInterval(scrollInterval); 
            }, 15 );
    }

    function scrollToTop(scrollDuration) {
        var scrollStep = -window.scrollY / (scrollDuration / 15),
            scrollInterval = setInterval(function(){
            if ( window.scrollY != 0 ) {
                window.scrollBy( 0, scrollStep );
            }
            else clearInterval(scrollInterval); 
        },15);
    }