
function Card(props){
  const {name,desc}=props
    return     <div className='card'>
    <h1 className='card-title'>{name}</h1>
    <p className='card-body'>{desc}</p>
    <h3 className='card-footer'>Student of BGC</h3>
  </div>
  }
  export default Card