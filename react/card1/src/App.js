import React from 'react'
import Card from './components/Card'
import Data from './data.json'
 function App(){
    // let items=[];
    // for(let i=0;i<Data.length;i++){
    //     items.push(<Card name={Data[i].title} desc={Data[i].desC} />)
    // }
    // items=Data.map((item)=><Card name={item.title} desc={item.desC}/>);
    return <div>
        <h1 className='heading largetext'>Welcome to you react</h1>
       {Data.map((item,k)=><Card key={k} name={item.title} desc={item.desC}/>)}
    </div>
}

export default App;