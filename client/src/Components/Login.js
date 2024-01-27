import React, {useState} from 'react'

function Login({onLogin}){

    const [email, setEmail] = useState("")

    function handleSubmit(e){
        e.preventDefault()
        fetch("/login", {
            method:"POST",
            headers: {
                "Content-Type":"application/json",
            },
            body : JSON.stringify({email}),
        })
            .then((response)=> response.json())
            .then((user) => onLogin(user))
    }


    return(
        <form onSubmit={handleSubmit}>
            <input
                type='text'
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder='Email'
                />
            <input
                type = 'text'
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder='Password'
                />
            <button type='submit'>Login</button>
        </form>
    )

}

export default Login;