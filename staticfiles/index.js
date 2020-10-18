window.onload = initAll;

var likeButton;
function initAll(){
    likeButton = document.getElementById('save_like')
    likeButton.onclick = saveLike;
}

function saveLike(){
    var post = document.getElementById('save_like').value;
    var url = '/like?post_id='+post;
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {

        }
    };
    req.open("GET",url , true);
    req.send();
}
