import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import axios from 'axios'
import VCharts from 'v-charts'
import * as echarts from 'echarts'
import MyComponent from './App.vue'

const app = createApp(App)

app.use(ElementPlus)
app.use(VCharts)
app.use(router)
app.use(store)

app.component('MyComponent', MyComponent)

app.config.productionTip = false;
app.config.globalProperties.$echarts = echarts
app.config.globalProperties.$axios = axios

import { useStore } from "vuex"
const store1 = useStore();

axios.defaults.baseURL = '/api';
axios.interceptors.request.use(
    config => {
        const token = store1.state.token;
        if (token) {
            // config.headers.Authorization = token;
            // config.headers["token"] = token;
        }
        return config;
    },
    error => {
        console.log("[main.js -> axios] Error! ");
        return Promise.reject(error);
    }
);
axios.interceptors.response.use(
    res => {
        return res;
    },
    error => {
        if (error.response) {
            switch (error.response.status) {
                case 403:
                    store1.commit('clearUserInfo');
                    router.replace({
                        path: '/',
                        query: {
                            redirect: router.currentRoute.fullPath
                        }
                    });
            }
        }
        return Promise.reject(error.response.data);
    }
);

app.mount('#app')
