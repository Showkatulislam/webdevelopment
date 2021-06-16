import React from 'react';
import  './form.css';
export default function Form() {
   const HName=(e)=>{
        console.log(e.target.value)
    }
    const HEmail=(e)=>{
        console.log(e.target.value)
    }
    const HPassword=(e)=>{
        console.log(e.target.value)
    }
    return (
        <div>
            <h1>Registration</h1>
            <form>
                <div>
                <label htmlFor="name">Name: </label>
                <input type="text" name="name" id="name" onChange={HName} required></input>
                </div>

                <div>
                <label htmlFor="email">Email: </label>
                <input type="email" name="email" id="email" onChange={HEmail} required></input>
                </div>

                <div>
                <label htmlFor="password">Password: </label>
                <input type="password" name="password" id="password" onChange={HPassword} required></input>
                </div>

                <button type="submit">Register</button>
            </form>
        </div>
    )
}
