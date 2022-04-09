import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/LoginView.vue";

const routes = [
  {
    path: "/",
    name: "login",

    component: () => import("../views/LoginView.vue"),
  },
  {
    path: "/signup",
    name: "signup",

    component: () => import("../views/SignupView.vue"),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
