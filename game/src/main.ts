import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import MusicPlayer from './components/Music.vue';


const app = createApp(App)
app.component('music-player', MusicPlayer);
app.use(createPinia())
app.use(router)

app.mount('#app')
