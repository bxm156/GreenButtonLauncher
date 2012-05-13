$(function() {
	$('#presentAreaAbout').hide();
	$('#presentAreaUpload').hide();
	$('#presentAreaNews').hide();
	$('#presentAreaContact').hide();
});
function onAbout() {
	$('#presentAreaHome').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaUpload').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaNews').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaContact').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaAbout').show("slide", { direction: "left" }, 1000);
}
function onUpload() {
	$('#presentAreaHome').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaAbout').hide("slide", { direction: "right" }, 1000);
	$('#presentAreaNews').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaContact').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaUpload').show("slide", { direction: "left"}, 1000);
}
function onNews() {
	$('#presentAreaHome').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaAbout').hide("slide", { direction: "right" }, 1000);
	$('#presentAreaUpload').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaContact').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaNews').show("slide", { direction: "left"}, 1000);
}
function onContact() {
	$('#presentAreaHome').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaAbout').hide("slide", { direction: "right" }, 1000);
	$('#presentAreaUpload').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaNews').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaContact').show("slide", { direction: "left"}, 1000);
}


