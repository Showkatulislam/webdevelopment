import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'
const name='Welcome to you'
const date=new Date()
const getdate=date.getDate()
const month=date.getMonth()
const year=date.getFullYear()

// const heading={
//   backgroundColor:'purple',
//   color:'red',
//   textAlign:'center',
//   padding:'10px'

// }
ReactDOM.render(
  <div>
    <h1 className='heading largetext'>hello react</h1>
    <h1>{name}</h1>
    <p>sssssssssssssssssssssssss</p>
    <p>{getdate+"-"+month+"-"+year}</p>
  </div>,
document.getElementById('root')
);


