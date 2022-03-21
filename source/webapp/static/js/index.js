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
    console.log(url);
    let response = await fetch(url);
    console.log(response);
}

// button = document.getElementById("like_id");
//         button.addEventListener("click", onLikeClick);
