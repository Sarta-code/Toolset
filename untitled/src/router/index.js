import {createRouter,createWebHistory} from 'vue-router'


const router = createRouter({
    history:createWebHistory(),
    routes:[
    {
        name:'pdfsplit',
        path:'/pdfsplit',
        component:''
    }
]
})

export  const initrouter = (app)=>{
    app.use(router)
}
