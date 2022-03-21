        async function onClick(event){
                let url = event.target.dataset.articlesUrl;
                let response = await fetch(url);
                let responseBody = await response.json();
        }
        function onLoad(){
                let btn = document.getElementById("btn");
                btn.addEventListener("click", onClick);
        }
        window.onload = onLoad;


async function onLikeClick(event){
    let url = event.target.dataset.likesUrl;
    let response = await fetch(url);
    let responseBody = await response.json()
    let id = responseBody.article_id
    div_like = document.getElementById(`${id}count`)
    div_like.innerText = `likes: ${responseBody.like}`
    document.getElementById(`${id}like_button`).style.display = "none"
    document.getElementById(`${id}unlike_button`).style.display = "block"

}

async function onUnLikeClick(event){
    let url = event.target.dataset.likesUrl;
    let response = await fetch(url);
    let responseBody = await response.json();
    let id = responseBody.article_id;
    let div_like = document.getElementById(`${id}count`);
    div_like.innerText = `likes: ${responseBody.like}`;
    document.getElementById(`${id}unlike_button`).style.display = 'none';
    document.getElementById(`${id}like_button`).style.display = 'block';

}

async function commentLikeLikeClick(event){
    let url = event.target.dataset.likesUrl;
    console.log(url);
    let response = await fetch(url);
    let responseBody = await response.json();
    console.log(responseBody)
    let id = responseBody.comment_id;
    let div_comment_like = document.getElementById(`${id}likes`);
    console.log(div_comment_like)
    div_comment_like.innerText = `likes: ${responseBody.like}`;

     document.getElementById(`${id}like_button`).style.display = 'none';
    document.getElementById(`${id}unlike_button`).style.display = 'block';
}
async function commentUnLikeClick(event){
    let url = event.target.dataset.likesUrl;
    let response = await fetch(url);
    let responseBody = await response.json();
    let id = responseBody.comment_id;
    let div_comment_like = document.getElementById(`${id}likes`);
    div_comment_like.innerText = `likes: ${responseBody.like}`;

     document.getElementById(`${id}unlike_button`).style.display = 'none';
    document.getElementById(`${id}like_button`).style.display = 'block';
}
