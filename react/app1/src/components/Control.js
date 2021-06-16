
import React, { Component } from 'react'
import '../index.css'
import Home from './Home'
import Login from './Login'
export default class Control extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             islogin:false
        }
    }
    
    render() {
        const {log}=this.state.islogin

        let element;
        element=log?<Home/>:<Login/>
        return(
            <div>{element}</div>
        )
           // condition statement
        // if(log){
        //     element=<Home/>
        // }
        // else{
        //     element=<Login/>
        // }
        // return(
        //     <div>{element}</div>
        // )

        // if(this.state.islogin){
        //     return  <Home/>
        // }
        // else{
        //     return  <Login/>
        // }
        // return (
        //     <div>
        //        <Home/>
        //     </div>
        // )
    }
}
