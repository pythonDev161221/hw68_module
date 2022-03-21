        async function onClick(event){
                let url = event.target.dataset.articlesUrl;
                console.log(url)
                let response = await fetch(url);
                let responseBody = await response.json();
                console.log(responseBody);
        }
        function onLoad(){
                let btn = document.getElementById("btn");
                btn.addEventListener("click", onClick);
        }
        window.onload = onLoad;
