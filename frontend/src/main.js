import { createApp } from "vue";
import App from "./App.vue";
import store from "./store";
import router from "./router";
import "./assets/css/nucleo-icons.css";
import "./assets/css/nucleo-svg.css";
import SoftUIDashboard from "./soft-ui-dashboard";
import axios from 'axios'
import VueAxios from 'vue-axios'
import {vfmPlugin} from 'vue-final-modal'
import VueClipboard from 'vue3-clipboard'
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css'

const appInstance = createApp(App);

// plugins
appInstance.use(store);
appInstance.use(router);
appInstance.use(SoftUIDashboard);
appInstance.use(VueAxios, axios);
appInstance.use(vfmPlugin);
appInstance.use(VueClipboard);
appInstance.use(VueSweetalert2);

// global properties
appInstance.config.globalProperties.$axios = axios.create();
appInstance.config.globalProperties.$axios_loaderless = axios.create();

appInstance.mount("#app");
