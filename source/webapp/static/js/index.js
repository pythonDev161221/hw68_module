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
    console.log(responseBody)
    let id = responseBody.article_id
    console.log(id)
    div_like = document.getElementById(`${id}count`)
    console.log(div_like)
    div_like.innerText = `likes: ${responseBody.like}`

}
