import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "@/views/Dashboard.vue";
import Tables from "@/views/Tables.vue";
import Notifications from "@/views/Notifications.vue";
import FileExplorer from "@/views/FileExplorer.vue";
import ScriptStore from "@/views/ScriptStore.vue";

const routes = [
  {
    path: "/",
    name: "/",
    redirect: "/dashboard",
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
  },
  {
    path: "/tables",
    name: "Tables",
    component: Tables,
  },
  {
    path: "/notifications",
    name: "Notifications",
    component: Notifications,
  },
  {
    path: "/file-explorer",
    name: "File Explorer",
    component: FileExplorer,
  },
  {
    path: "/script-store",
    name: "Script Store",
    component: ScriptStore,
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  linkActiveClass: "active",
});

export default router;
