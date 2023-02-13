import request from "../utils/request.js";

export const uplodafile = (data)=>{
    return request({url:'index/',method:'post',data})
}