$(document).ready(function($){ 
 $("#another").on("click",function(q){
      q.preventDefault();
    $.ajax ({
    url: "https://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1&callback=",
  success:function(data) {
var quote = data.shift();
   var quoteAnimate=$("#quoteText, #author, #linkSpace");
    var animTime=600;
  quoteAnimate.fadeOut(animTime,function(){
    quoteAnimate.html("");
  $("#quoteText").append(quote.content);
 $("#author").text("- " +quote.title);
$("#linkSpace").html("source: " + quote.link);
      quoteAnimate.fadeIn(animTime)
      });
  },
      cache:false
      
    });
});

});