import React from 'react'

import Card from './component/Card'

import Header from './component/header'
import Card1 from './component/Card1'

function App(){
    return <div>
        <Header/>
        <Card card='showkatul islam' desc='I am not good student'/>
        <Card1 card='showkatul islam' desc='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Expedita omnis facilis perspiciatis dignissimos libero nemo minima at ex exercitationem velit!'/>
    </div>
}

export default App