console.log("hello")
//get all star

const one=document.getElementById("one")
const two=document.getElementById('two')
const three=document.getElementById('three')
const four=document.getElementById('four')
const five=document.getElementById('five')

const form=document.querySelector('.rate-form')

const confirmBox=document.getElementById('confirm-box')

const csrf=document.getElementsByName('csrfmiddlewaretoken')

const handleStarselect=(size)=>{
    const children=form.children
    for(let i=0;i<children.length;i++){
        if(i<=size){
            children[i].classList.add('checked')
        }else{
            children[i].classList.remove('checked')
        }
    }
}


const handleSelect=(selection)=>{
    console.log(selection)
   switch(selection){
       case 'one':{
        handleStarselect(1)
           return
       }
       case 'two':{
        // one.classList.add('checked')
        // two.classList.add('checked')
        // three.classList.remove('checked')
        // four.classList.remove('checked')
        // five.classList.remove('checked')
        handleStarselect(2)
        return
    }
    case 'three':{
        // one.classList.add('checked')
        // two.classList.add('checked')
        // three.classList.add('checked')
        // four.classList.remove('checked')
        // five.classList.remove('checked')
        handleStarselect(3)
        return
    }
    case 'four':{
        // one.classList.add('checked')
        // two.classList.add('checked')
        // three.classList.add('checked')
        // four.classList.add('checked')
        // five.classList.remove('checked')
        handleStarselect(4)
        return
    }
    case 'five':{
        // one.classList.add('checked')
        // two.classList.add('checked')
        // three.classList.add('checked')
        // four.classList.add('checked')
        // five.classList.add('checked')
        handleStarselect(5)
        return
    }
   }
}

const getNumericValue=(stringValue)=>{
    let numericValue;
    if(stringValue=='one'){
        numericValue=1
    }
    else if(stringValue=='two'){
        numericValue=2
    }
    else if(stringValue=='three'){
        numericValue=3
    }
    else if(stringValue=='four'){
        numericValue=4
    }
    else if(stringValue=='five'){
        numericValue=5
    }
    else{
        numericValue=0
    }
    return numericValue
}

const arr=[one,two,three,four,five]

if(one){
    arr.forEach(item=>item.addEventListener('mouseover',(event)=>{
        handleSelect(event.target.id)
    }))
    arr.forEach(item=>item.addEventListener('click',(event)=>{
        const val=event.target.id
        alert(val)
        form.addEventListener('submit',e=>{
            e.preventDefault()
            const id =e.target.id
            console.log(id)
            const val_num=getNumericValue(val)
            $.ajax({
                type:'POST',
                url:'/rate/',
                data:{
                    'csrfmiddlewaretoken':csrf[0].value,
                    'el_id':id,
                    'val':val_num,
                },
                success: function(response){
                    console.log(response)
                    confirmBox.innerHTML=`<h1>Successfully ${response.score} </h1>`
                },
                error: function(error){
                    console.log(error)
                    confirmBox.innerHTML=`<h1> wrong </h1>`
                }
            })
        })
    }))
    
}



