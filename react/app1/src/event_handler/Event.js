import React, { Component } from 'react'
export default class event extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             changeValue:''
        }
    }
    

    Onclange=(e)=>{
       this.setState(
           {
               changeValue:e.target.value
           },()=>{
               console.log(this.state.changeValue)
           }
       )
    }
    render() {
        return (
            <div>
              <input type="text" onChange={this.Onclange}></input>
              <p>{this.state.changeValue}</p>
            </div>
        )
    }
}
