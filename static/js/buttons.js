$(function() {
	$('#presentAreaAbout').hide();
	$('#presentAreaUpload').hide();
	$('#presentAreaNews').hide();
	$('#presentAreaContact').hide();
	$('#chooseFileControl')
	$('#chooseFileButton').click(function() {
		$('#chooseFileControl').click();
	});
	$('#uploadFileButton').click(function() {
		$('#uploadFileControl').click();
	});
});
function onAbout() {
	$('#presentAreaHome:visible').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaUpload:visible').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaNews:visible').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaContact:visible').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaAbout:hidden').show("slide", { direction: "left" }, 1000);
}
function onUpload() {
	$('#presentAreaHome:visible').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaAbout:visible').hide("slide", { direction: "right" }, 1000);
	$('#presentAreaNews:visible').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaContact:visible').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaUpload:hidden').show("slide", { direction: "left"}, 1000);
}
function onNews() {
	$('#presentAreaHome:visible').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaAbout:visible').hide("slide", { direction: "right" }, 1000);
	$('#presentAreaUpload:visible').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaContact:visible').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaNews:hidden').show("slide", { direction: "left"}, 1000);
}
function onContact() {
	$('#presentAreaHome:visible').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaAbout:visible').hide("slide", { direction: "right" }, 1000);
	$('#presentAreaUpload:visible').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaNews:visible').hide("slide", { direction: "right"}, 1000);
	$('#presentAreaContact:hidden').show("slide", { direction: "left"}, 1000);
}