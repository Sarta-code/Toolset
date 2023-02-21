import request from "../utils/request.js";

export const uplodafile = (data)=>{
    return request({url:'upload/',method:'post',data})
}