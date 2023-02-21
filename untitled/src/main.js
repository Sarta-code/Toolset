import '../style.css'
import javascriptLogo from '../javascript.svg'
import App from './App.vue'
import {createApp} from 'vue'
import {initrouter} from './router/index.js'

const app = createApp(App)
initrouter(app)
app.mount('#app')

