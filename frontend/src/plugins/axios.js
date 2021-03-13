import Vue from "vue";
import axios from "axios";

axios.defaults.baseURL = "https://localhost:8000";

Vue.use({
  install(Vue) {
    Vue.prototype.$http = axios;
  }
});
