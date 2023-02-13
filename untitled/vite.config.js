import {defineConfig} from "vite"
import Vue from '@vitejs/plugin-vue'



export default defineConfig(({command,mode,ssrBuild})=>{

    return {
        server:{
            host:"127.0.0.1",
        },
        plugins:[
            Vue()
        ]
    }

})