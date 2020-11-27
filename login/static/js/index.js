$(window).on("hashchange", function(){
if(location.hash.slice(1)=="register"){
$(".card").addClass("extend");
$("#login").removeClass("selected");
$("#register").addClass("selected");
} else {
$(".card").removeClass("extend");
$("#login").addClass("selected");
$("#register").removeClass("selected");
}
});
$(window).trigger("hashchange");