var percentColors = [
    { pct: 0.0, color: { r: 0xff, g: 0x00, b: 0 } },
    { pct: 0.5, color: { r: 0xff, g: 0xff, b: 0 } },
    { pct: 1.0, color: { r: 0x00, g: 0xff, b: 0 } } ];

var getColorForPercentage = function (pct) {
		return 'rgb(255,255,255)';
		//
        for (var i = 0; i < percentColors.length; i++) {
            if (pct <= percentColors[i].pct) {
                var lower = percentColors[i - 1] || {
                    pct: 0.1,
                    color: {
                        r: 0x0,
                        g: 0x00,
                        b: 0
                    }
                };
                var upper = percentColors[i];
                var range = upper.pct - lower.pct;
                var rangePct = (pct - lower.pct) / range;
                var pctLower = 1 - rangePct;
                var pctUpper = rangePct;
                var color = {
                    r: Math.floor(lower.color.r * pctLower + upper.color.r * pctUpper),
                    g: Math.floor(lower.color.g * pctLower + upper.color.g * pctUpper),
                    b: Math.floor(lower.color.b * pctLower + upper.color.b * pctUpper)
                };
                return 'rgb(' + [color.r, color.g, color.b].join(',') + ')';
            }
        }
    }


$(document).ready(function ($) {
    
	$.fn.extend({ 
        rotaterator: function(options) {
 
            var defaults = {
                fadeSpeed: 500,
                pauseSpeed: 100,
				child:null
            };
             
            var options = $.extend(defaults, options);
         
            return this.each(function() {
                  var o =options;
                  var obj = $(this);                
                  var items = $(obj.children(), obj);
				  items.each(function() {$(this).hide();})
				  if(!o.child){var next = $(obj).children(':first');
				  }else{var next = o.child;
				  }
				  $(next).fadeIn(o.fadeSpeed, function() {
						$(next).delay(o.pauseSpeed).fadeOut(o.fadeSpeed, function() {
							var next = $(this).next();
							if (next.length == 0){
									next = $(obj).children(':first');
							}
							$(obj).rotaterator({child : next, fadeSpeed : o.fadeSpeed, pauseSpeed : o.pauseSpeed});
						})
					});
            });
        }
    });
	
	$('div.polls').find('span.option').each(function () {
        $(this).css({
            backgroundColor: getColorForPercentage($(this).attr('title') / 100)
        });
    });
	
	window.setInterval(function(){
	  $.getJSON('/getresult.php', function(data) {
		 $.each(data.results, function (option, value) {
				$("td#vote_" + option).text(value.rates);
				
                $("p#option_" + option).find("span").show().animate({
                    width: value.percent + "%",
                    backgroundColor: getColorForPercentage(value.percent / 100),
                    opacity: 1
                }, "slow", "swing", function () {
                    $("p#option_" + option).find("em").text(value.rates +" (" + value.percent + "%)").fadeIn("slow");
                })
            });
		});
	}, 5000);

	$('#rotate').rotaterator({fadeSpeed:500, pauseSpeed:6000});
});