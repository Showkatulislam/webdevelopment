import React,{useState} from 'react'

export default function Hook1() {
    const [count,setCount]=useState(0)
    const Hin=()=>{
      setCount(count+1);
    }
    return (
        <div>
            <h1>Count: {count}</h1>
            <button onClick={Hin}>incerement</button>
        </div>
    )
}
