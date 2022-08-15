import "./Button.css";
import axios from "axios";
function Button ({query, sendQuery}){
    function handleClick(){
        sendQuery(query);
    }
    return(
        <button onClick={handleClick}>Submit</button>
    )
}

export default Button;