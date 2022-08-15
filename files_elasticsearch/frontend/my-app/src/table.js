import "./table.css"
import React from 'react';

const Table = React.memo(({searchResult}) => {
    let tableReturn;
    if(searchResult && searchResult.files)
    {
    let tableReturn = searchResult.files.map((item)=>{
             return(<tr id={item.url}>
                <td>{item.file_name}</td>
                <td><a target="_blank" href={item.url}>{item.url}</a></td>
            </tr>)
        })
        return <table><tbody><tr><th>File name</th><th>File URL</th></tr>{tableReturn}</tbody></table>;
    }
    return <table><tbody>{tableReturn}</tbody></table>
})

export default Table;