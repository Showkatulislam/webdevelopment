
function Card(props){
    const {card,desc}=props
    return <div className='card'>
      <h3 className='cardTitle'>{card}</h3>
      <p className='cardDese'>{desc}</p>
      <p className='cardFooter' >BGC trust University Bangladesh</p>
    </div>
  
  }
  export default Card