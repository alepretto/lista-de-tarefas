import Vue from "vue";
import Router from "vue-router";
import Dashboard from "./pages/dashboard/index.vue";
import AddTask from "./pages/addTask/index.vue";

Vue.use(Router);

export default new Router({
  routes: [
    { path: "/", component: Dashboard },
    { path: "/addTask", component: AddTask },
  ],
  mode: "history",
});
