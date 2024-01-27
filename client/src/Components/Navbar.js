import React from "react";

function Navbar({onLogout}){
    function handlelogout(){
        fetch("/logout", {
            method: "DELETE",
        }).then(() => onLogout());
    }

    return (
        <header>
            <button onClick={handlelogout}>logout</button>
        </header>
    );
}

export default Navbar;