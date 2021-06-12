const url=window.location.href
const searchForm=document.getElementById('search-form')
const searchInput=document.getElementById('search-input')
const resultsBox=document.getElementById('results-box')

var csrf=document.getElementsByName('csrfmiddlewaretoken')[0].value

const sendSearchData=(game)=>{
    $.ajax({
        type:'POST',
        url:'search/',
        data:{
            'csrfmiddlewaretoken':csrf,
             'game':game,
        },
        success:(res)=>{
            console.log(res.data)
            const data=res.data
            if(Array.isArray(data)){
                resultsBox.innerHTML= ""
                data.forEach(rest=>{
                    for(var i=0;i<rest.length;i++){
                    resultsBox.innerHTML +=`
                    <a href="${url}${rest[i].pk}" class="item">
                    <div class="row mt-2 mb-2">
                    <div class="col-2">
                    <img src="${rest[i].image}" class="game-img" alt="ff">
                    </div>
                    <div class="col-10 control-name">
                    <h5>${rest[i].name}</h5>
                    <p class="text-muted">${rest[i].area}</p>
                    </div>
                    </div>
                    </a>
                    `
                }})
            }
            else{
                if(searchInput.value.length>0){
                    resultsBox.innerHTML=`<b> ${data} </b>`
                }else{
                    resultsBox.classList.add('d-none')
                }
            }
        },
        error:(err)=>{
            console.log(err)
        }
    })
}

searchInput.addEventListener('keyup',e=>{
    console.log(e.target.value)

    if(resultsBox.classList.contains('d-none')){
        resultsBox.classList.remove('d-none')
    }
    sendSearchData(e.target.value)
})