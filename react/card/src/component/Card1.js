import React,{Component} from 'react'
import Card from './Card'

class Card1 extends Component{
    render(){
        return(
            <div className='card'>
            <h3 className='cardTitle'>{this.props.card}</h3>
            <p className='cardDese'>{this.props.desc}</p>
            <p className='cardFooter' >BGC trust University Bangladesh</p>
             </div>
        )
    }
}
export default Card1