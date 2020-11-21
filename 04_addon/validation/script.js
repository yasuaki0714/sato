const sorce = document.doctype.valueOf() + "\n" + document.documentElement.outerHTML;

chrome.extension.onMessage.addListener(function(request, sender, sendResponse) {
	if (request == "Action") {
		console.log("<!DOCTYPE html>" + sorce);
	}
});
