<template>
    <sidenav
            :custom_class="this.$store.state.mcolor"
            :class="[
      this.$store.state.isTransparent,
      this.$store.state.isRTL ? 'fixed-end' : 'fixed-start',
    ]"
            v-if="this.$store.state.showSidenav"
    />
    <main
            class="main-content position-relative max-height-vh-100 h-100 border-radius-lg"
            :style="this.$store.state.isRTL ? 'overflow-x: hidden' : ''"
    >
        <!-- nav -->
        <navbar
                :class="[navClasses]"
                :textWhite="this.$store.state.isAbsolute ? 'text-white opacity-8' : ''"
                :minNav="navbarMinimize"
                v-if="this.$store.state.showNavbar"
        />
        <router-view/>
        <app-footer v-show="this.$store.state.showFooter"/>
        <configurator
                :toggle="toggleConfigurator"
                :class="[
        this.$store.state.showConfig ? 'show' : '',
        this.$store.state.hideConfigButton ? 'd-none' : '',
      ]"
        />
    </main>
    <loader :is-visible="isLoading"></loader>
</template>
<script>
    import Sidenav from "./ccmp/Sidenav";
    import Loader from "./ccmp/Loader";
    import Configurator from "@/ccmp/Configurator.vue";
    import Navbar from "@/ccmp/Navbars/Navbar.vue";
    import AppFooter from "@/ccmp/Footer.vue";
    import {mapMutations} from "vuex";

    export default {
        name: "App",
        components: {
            Sidenav,
            Configurator,
            Navbar,
            AppFooter,
            Loader
        },

        created() {
            this.enableInterceptor();
        },
        data() {
            return {
                isLoading: false,
                axiosInterceptor: null,
            }
        },

        methods: {
            ...mapMutations(["toggleConfigurator", "navbarMinimize"]),

            enableInterceptor() {
                const this_ = this;
                this.axiosInterceptor = this_.$axios.interceptors.request.use((config) => {
                    this_.isLoading = true
                    return config
                }, (error) => {
                    this.isLoading = false
                    return Promise.reject(error)
                })

                this_.$axios.interceptors.response.use((response) => {
                    this_.isLoading = false
                    return response
                }, function (error) {
                    this_.isLoading = false
                    this_.$swal.fire({
                        icon: 'error',
                        title: 'HTTP Request Error',
                        text: 'Something went wrong!',
                    });
                    return Promise.reject(error)
                })
            },

            disableInterceptor() {
                this.$axios.interceptors.request.eject(this.axiosInterceptor)
            },
        },
        computed: {
            navClasses() {
                return {
                    "position-sticky blur shadow-blur mt-4 left-auto top-1 z-index-sticky": this
                        .$store.state.isNavFixed,
                    "position-absolute px-4 mx-0 w-100 z-index-2": this.$store.state
                        .isAbsolute,
                    "px-0 mx-4 mt-4": !this.$store.state.isAbsolute,
                };
            },
        },
        beforeMount() {
            this.$store.state.isTransparent = "bg-transparent";
        },
    };
</script>
