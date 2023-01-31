<template>
    <nav
            class="shadow-none navbar navbar-main navbar-expand-lg border-radius-xl"
            v-bind="$attrs"
            id="navbarBlur"
            data-scroll="true"
    >
        <div class="px-3 py-1 container-fluid">
            <breadcrumbs :currentPage="currentRouteName" :textWhite="textWhite"/>
            <div
                    class="mt-2 collapse navbar-collapse mt-sm-0 me-md-0 me-sm-4"
                    :class="this.$store.state.isRTL ? 'px-0' : 'me-sm-4'"
                    id="navbar"
            >
                <div
                        class="pe-md-3 d-flex align-items-center"
                        :class="this.$store.state.isRTL ? 'me-md-auto' : 'ms-md-auto'"
                >
                    <div class="input-group">
            <span class="input-group-text text-body"
            ><i class="fas fa-search" aria-hidden="true"></i
            ></span>
                        <input
                                type="text"
                                class="form-control"
                                placeholder="Type here..."
                        />
                    </div>
                </div>
                <ul class="navbar-nav justify-content-end">
                    <li class="nav-item d-xl-none ps-3 d-flex align-items-center">
                        <a
                                href="#"
                                @click="toggleSidebar"
                                class="p-0 nav-link text-body"
                                id="iconNavbarSidenav"
                        >
                            <div class="sidenav-toggler-inner">
                                <i class="sidenav-toggler-line"></i>
                                <i class="sidenav-toggler-line"></i>
                                <i class="sidenav-toggler-line"></i>
                            </div>
                        </a>
                    </li>
                    <li class="px-3 nav-item d-flex align-items-center">
                        <a
                                class="p-0 nav-link"
                                @click="toggleConfigurator"
                                :class="textWhite ? textWhite : 'text-body'"
                        >
                            <i class="cursor-pointer fa fa-cog fixed-plugin-button-nav"></i>
                        </a>
                    </li>
                    <li
                            class="nav-item dropdown d-flex align-items-center"
                            :class="this.$store.state.isRTL ? 'ps-2' : 'pe-2'"
                    >
                        <a
                                href="#"
                                class="p-0 nav-link"
                                :class="[
                textWhite ? textWhite : 'text-body',
                showMenu ? 'show' : '',
              ]"
                                id="dropdownMenuButton"
                                data-bs-toggle="dropdown"
                                aria-expanded="false"
                                @click="showMenu = !showMenu"
                        >
                            <i class="cursor-pointer fa fa-bell"></i>
                        </a>
                        <ul
                                class="px-2 py-3 dropdown-menu dropdown-menu-end me-sm-n4"
                                :class="showMenu ? 'show' : ''"
                                aria-labelledby="dropdownMenuButton"
                        >
                            <li class="mb-2" v-for="notification in notifications" :key="notification.id">
                                <a class="dropdown-item border-radius-md" @click="notification_clicked(notification)">
                                    <div class="py-1 d-flex">
                                        <div class="d-flex flex-column justify-content-center">
                                            <h6 class="mb-1 text-sm font-weight-normal">
                                                <span class="font-weight-bold">{{notification.message}}</span>
                                            </h6>
                                            <p class="mb-0 text-xs text-secondary">
                                                <i class="fa fa-clock me-1"></i>
                                                {{format_date(notification.time)}}
                                            </p>
                                        </div>
                                    </div>
                                </a>
                            </li>

                            <li class="mb-2">
                                <a class="dropdown-item border-radius-md" @click="view_all_clicked(notification)">
                                    <div class="py-1 d-flex">
                                        <div class="d-flex flex-column justify-content-center">
                                            <h6 class="mb-1 text-sm font-weight-normal">
                                                <p class="mb-0 text-xs text-secondary">
                                                    View All
                                                </p>
                                            </h6>
                                        </div>
                                    </div>
                                </a>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>
<script>
    import Breadcrumbs from "../Breadcrumbs.vue";
    import {mapMutations, mapActions} from "vuex";
    import moment from "moment";

    export default {
        name: "navbar",
        data() {
            return {
                showMenu: false,
                notifications: []
            };
        },
        props: ["minNav", "textWhite"],
        created() {
            this.minNav;
            this.poll_notifications();
        },
        methods: {
            ...mapMutations(["navbarMinimize", "toggleConfigurator"]),
            ...mapActions(["toggleSidebarColor"]),
            notification_clicked(notification){
                alert(notification.extra)
            },
            view_all_clicked(){
                this.$router.push('/notifications')
            },
            format_date(dt){
                return moment.unix(dt).fromNow()
            },
            toggleSidebar() {
                this.toggleSidebarColor("bg-white");
                this.navbarMinimize();
            },

            on_poll_success(res) {
                this.notifications = res;
            },
            poll_notifications() {
                const this_ = this;
                this.$axios_loaderless
                    .post(this_.$store.state.api_url + 'notifications',{page : 5})
                    .then(response => {
                        var delayInMilliseconds = 60*1000;
                        this_.on_poll_success(response.data);
                        setTimeout(function() {
                            this_.poll_notifications();
                        }, delayInMilliseconds);
                    })
            },
        },
        components: {
            Breadcrumbs,
        },
        computed: {
            currentRouteName() {
                return this.$route.name;
            },
        },
        updated() {
            const navbar = document.getElementById("navbarBlur");
            window.addEventListener("scroll", () => {
                if (window.scrollY > 10 && this.$store.state.isNavFixed) {
                    navbar.classList.add("blur");
                    navbar.classList.add("position-sticky");
                    navbar.classList.add("shadow-blur");
                } else {
                    navbar.classList.remove("blur");
                    navbar.classList.remove("position-sticky");
                    navbar.classList.remove("shadow-blur");
                }
            });
        },
    };
</script>
