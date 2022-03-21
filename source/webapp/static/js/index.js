        async function onClick(event){
                let url = event.target.dataset.articlesUrl;
                // console.log(url)
                let response = await fetch(url);
                let responseBody = await response.json();
                // console.log(responseBody);
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
    document.getElementById(`${id}like_button`).style.visibility = "hidden"
    document.getElementById(`${id}unlike_button`).style.visibility = "visible"
    console.log(button_like)
    button_like.style.display = 'toggle'
}

async function onUnLikeClick(event){
    let url = event.target.dataset.likesUrl;
    let response = await fetch(url);
    let responseBody = await response.json()
    let id = responseBody.article_id
    div_like = document.getElementById(`${id}count`)
    div_like.innerText = `likes: ${responseBody.like}`
    document.getElementById(`${id}unlike_button`).style.visibility = 'hidden'
    document.getElementById(`${id}like_button`).style.visibility = 'visible'

}

