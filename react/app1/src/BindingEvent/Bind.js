import React, { Component } from 'react'

export default class Bind extends Component {
 constructor(props){
     super(props)
     this.state={
         count:0
     }
 }
    HClick=()=>{
        this.setState({
            count:this.state.count+1
        })
    }
    render() {
        return (
            <div>
            <h1>{this.state.count}</h1>
            <button onClick={this.HClick}>increase</button>
            </div>
        )
    }
}
//function.bind(this)