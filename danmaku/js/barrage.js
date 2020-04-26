$(function(){
    $(".send").click(function(){
        var text=$(".input").val();
        var div="<div>"+text+"</div>";
        var width = $(".bottom").width();
        var height = Math.floor(Math.random()*$(".bottom").height());
        $(".show").append(div);
        var length = $('.show div').length;
        $('.show div').eq(length-1).css({'top':height,'width':$('.show div').eq(length-1).width()});
        $('.show div').eq(length-1).animate({right:width},6000);
    })
});